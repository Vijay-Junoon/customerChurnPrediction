
import pandas as pd
import numpy as np

class DataIngestion:

  def __init__(self):
    pass

  def ingest_data(self,engine):

    query = "SELECT * FROM customer_churn"
    data = pd.read_sql(sql = query, con = engine)

    X = data.iloc[:,:-1].values
    y = data.iloc[:,-1]

    print("Data Ingestion Completed!")
    return X,y


