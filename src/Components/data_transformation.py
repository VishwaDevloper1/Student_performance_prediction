import numpy as np
import pandas as pd
import os

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.exception import custom_exception
import sys
from  dataclasses import dataclass
from src.utils import save_object
@dataclass
class DataTransformationconfig:
   Preprocessor_file_path = os.path.join("artifects", "preprocessor.pkl")

class DataTransformation:
   def __init__(self):
    self.Transformation_config = DataTransformationconfig

   def get_transformer_obj(self):
     logging.info("Data Transformation Started")
     try:
        num_col = ["reading_score","writing_score"]
        cat_col = ['gender','race_ethnicity','parental_level_of_education','lunch','test_preparation_course']

        num_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('std_scaler', StandardScaler())
            ]
        )
        logging.info("Num columns standardization completed")
        cat_pipeline = Pipeline(
         steps=[
             ('imputer', SimpleImputer(strategy='most_frequent')),
             ("onehot", OneHotEncoder()),
             ('scaler', StandardScaler(with_mean=False))
         ]
        )
        logging.info("cat columns encoding completed")

        preprocessor_pipeline = ColumnTransformer(
            [('num_pipeline', num_pipeline, num_col),
             ('cat_pipeline',cat_pipeline,cat_col)]
            )

        return preprocessor_pipeline

     except Exception as e:
         raise custom_exception(e, sys)

   def initiate_data_transformation(self,train_path,test_path):
       try:
          train_df = pd.read_csv(train_path)
          test_df = pd.read_csv(test_path)

          logging.info("Reading train and test data completed")
          logging.info("obtaining preprocessor object")
          preprocessor_obj = self.get_transformer_obj()

          target_column = ["math_score"]
          numerical_columns = ["reading_score","writing_score"]
          input_feature_data_train = train_df.drop(target_column, axis=1)
          target_feature_train = train_df[target_column]

          input_feature_data_test = test_df.drop(target_column, axis=1)
          target_feature_test = test_df[target_column]

          logging.info("Applying preprocessing object on train and test data")
          input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_data_train)
          input_feature_test_arr = preprocessor_obj.transform(input_feature_data_test)

          train_arr = np.c_[input_feature_train_arr, target_feature_train]
          test_arr = np.c_[input_feature_test_arr, target_feature_test]
          logging.info(f"Saved preprocessing object.")
          save_object(
              file_path = self.Transformation_config.Preprocessor_file_path,
              obj = preprocessor_obj,
          )

          return train_arr, test_arr,self.Transformation_config.Preprocessor_file_path

       except Exception as e:
           raise custom_exception(e, sys)