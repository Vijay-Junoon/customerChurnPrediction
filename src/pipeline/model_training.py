from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os
import yaml


params = yaml.safe_load(open("params.yaml"))['model_train']


class ModelTrainer:

  def __init__(self):
    pass


  def splitData(self,features,target):
    X_train,X_test,y_train,y_test = train_test_split(features,target,random_state = 42, test_size = 0.2)
    print("Splitting of data completed!")
    return X_train,X_test,y_train,y_test

  def logisticRegression(self,X_train,X_test,y_train,y_test):

      regressor = LogisticRegression()
      regressor.fit(X_train,y_train)
      y_pred = regressor.predict(X_test)
      accuracy = accuracy_score(y_test,y_pred)
      model_path = params['model_path']
      os.makedirs(os.path.dirname(model_path),exist_ok = True)


      joblib.dump(regressor,model_path)
      print("Saved model to model")


      
