from src.pipeline.data_ingestion import DataIngestion
from src.pipeline.ETL import ETL_Pipeline
from src.pipeline.model_training import ModelTrainer
import yaml
from src.database.engine import engine


def run_pipeline():


  #* Load params file for parameters
  params = yaml.safe_load(open("params.yaml"))
  print("Loaded params.yaml file")


  # * ETL Pipeline
  etl = ETL_Pipeline()

  etl.extract()
  etl.transform(params['etl_transform']['input'],params['etl_transform']['output'])
  etl.load(params['etl_load']['input'])

  #* Data Ingestion
  ingester = DataIngestion()
  Features,target = ingester.ingest_data(engine=engine)

  #* Model Training
  trainer = ModelTrainer()
  X_train,X_test,y_train,y_test = trainer.splitData(Features,target)
  trainer.logisticRegression(X_train,X_test,y_train,y_test)

  #* Model Evaluation


if __name__ == "__main__":
    run_pipeline()