import os

from src.exception import custom_exception
import sys
from src.utils import load_object
import pandas as pd

class prediction_pipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
           model_path = os.path.join("artifects","model_trainer.pkl")
           preprocessor_path = os.path.join("artifects","preprocessor.pkl")
           model = load_object(file_path=model_path)
           preprocessor = load_object(file_path=preprocessor_path)
           scaled_data = preprocessor.transform(features)
           prediction = model.predict(scaled_data)
           return prediction

        except Exception as e:
            raise custom_exception(e,sys)

class custom_data:
  def __init__(self,gender:str,race_ethnicity:str,
                    parental_level_of_education:str,
                    lunch:str,test_preparation_course:str,
                    reading_score:int,writing_score:int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

  def raw_data_to_dataframe(self):
      try:
          dataframe_dict = {
              'gender': [self.gender],
              'race_ethnicity': [self.race_ethnicity],
              'parental_level_of_education': [self.parental_level_of_education],
              'lunch': [self.lunch],
              'test_preparation_course': [self.test_preparation_course],
              'reading_score': [self.reading_score],
              'writing_score': [self.writing_score]
          }
          return pd.DataFrame(dataframe_dict)

      except Exception as e:
          raise custom_exception(e,sys)
