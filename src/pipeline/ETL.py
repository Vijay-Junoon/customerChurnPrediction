import yaml
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder
from sklearn.preprocessing import StandardScaler
import os
from src.database.engine import engine

class ETL_Pipeline:
  def __init__(self):
    pass


  def extract(self):
    # API, web scraping logic
    # Currently using csv
    print("Extracted data!")
    pass


  def transform(self,input_path,output_path):
    data = pd.read_csv(input_path)
    target = data['Exited']
    data = data.drop(['RowNumber','CustomerId','Surname','Exited'],axis=1)
    categorical_columns = ["Geography", "Gender"]
    numerical_columns = ["CreditScore","Age","Tenure","Balance","NumOfProducts","HasCrCard","IsActiveMember","EstimatedSalary","Complain","Satisfaction Score","Point Earned"]
    ct = ColumnTransformer(transformers=[('simple-encoder',OneHotEncoder(drop = "first"),categorical_columns),('num',StandardScaler(),numerical_columns),('ord-encoder',OrdinalEncoder(categories=[["SILVER",'GOLD','PLATINUM','DIAMOND']]),['Card Type'])],remainder='passthrough',verbose_feature_names_out=False)
    data = pd.DataFrame(ct.fit_transform(data),columns=ct.get_feature_names_out())
    data['Exited'] = target
    os.makedirs(os.path.dirname(output_path),exist_ok = True)
    data.to_csv(output_path,index=False)
    print("Processed data transformed!")

  def load(self,data_path):
    data = pd.read_csv(data_path)

    data.to_sql(
      name = "customer_churn",
      con = engine,
      if_exists="replace",
      index = False
    )

    print(f"Data loaded to the database!")