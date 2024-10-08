import pandas as pd
import os
from src.logger import logging
from src.exception import custom_exception
import sys
from sklearn.model_selection import train_test_split
from  dataclasses import dataclass
from src.Components.data_transformation import DataTransformation
from src.Components.data_transformation import DataTransformationconfig
from src.Components.model_trainer import ModelTrainer
import mysql.connector

@dataclass
class DataIngestionconfig:
    train_data_path : str= os.path.join('artifects', 'train.csv')
    test_data_path : str= os.path.join('artifects', 'test.csv')
    raw_data_path : str = os.path.join('artifects', 'data.csv')

class DataIngestion:
 def __init__(self):
   self.ingestion_config = DataIngestionconfig()

 def initiate_data_ingestion(self) -> object:
   logging.info("Data Ingestion initiated")
   try:
       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           password="#G4Great",
           database="my_database"
       )
       query = 'SELECT * FROM stud'
       df = pd.read_sql(query, connection)
       connection.close()


       # df = pd.read_csv(r'D:\python\pythonProject\ml_project\notebook\data\stud.csv')
       logging.info('Read the dataset as dataframe')

       os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
       df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

       logging.info('Train test split initiated')
       train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)

       train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)
       test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)
       logging.info('Train test split completed')

       return (  self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path )

   except Exception as e:
       custom_exception(e,sys)

if __name__ == '__main__':
  obj = DataIngestion()
  train_data,test_data = obj.initiate_data_ingestion()

  data_transformation = DataTransformation()
  train_arr,test_arr,_= data_transformation.initiate_data_transformation(train_data,test_data)

  model_trainer = ModelTrainer()
  print(model_trainer.initiate_model_trainer(train_arr,test_arr))