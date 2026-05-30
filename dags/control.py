import sys
import os
BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(BASE_DIR)

from src.pipeline.data_ingestion import DataIngestion
from src.pipeline.ETL import ETL_Pipeline
from src.pipeline.model_training import ModelTrainer
import yaml
from src.database.engine import engine
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


params = yaml.safe_load(open(os.path.join(
            BASE_DIR,"params.yaml")))

def ETL():
  # * ETL Pipeline
  etl = ETL_Pipeline()

  etl.extract()
  etl.transform(params['etl_transform']['input'],params['etl_transform']['output'])
  etl.load(params['etl_load']['input'])


def train_model():
  ingester = DataIngestion()
  Features,target = ingester.ingest_data(engine=engine)

  trainer = ModelTrainer()
  X_train,X_test,y_train,y_test = trainer.splitData(Features,target)
  trainer.logisticRegression(X_train,X_test,y_train,y_test)

with DAG(
  dag_id = "customer_churn_pipeline",
  start_date = datetime(2025,1,1),
  schedule="@daily",
  catchup = False
)as dag:
  
  etl_task = PythonOperator(task_id="etl-pipeline",python_callable = ETL)
  train_task = PythonOperator(task_id = "train_model",python_callable = train_model)


  etl_task >> train_task