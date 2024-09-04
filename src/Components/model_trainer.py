import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from src.exception import custom_exception
from src.logger import logging

from src.utils import save_object,evaluate_models


@dataclass
class ModelTrainerConfig:
     model_trainer_path = os.path.join('artifects', "model_trainer.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    def initiate_model_trainer(self,train_arr,test_arr):
     try:
      models = {
      "LinearRegression": LinearRegression(),
      "RandomForestRegressor": RandomForestRegressor(),
      "XGBRegressor": XGBRegressor(),
      "DecisionTreeRegressor": DecisionTreeRegressor(),
      "AdaBoostRegressor": AdaBoostRegressor(),
      "GradientBoostingRegressor": GradientBoostingRegressor(),
      "KNeighborsRegressor": KNeighborsRegressor(),
        }

      x_train,x_test,y_train,y_test =(train_arr[:,:-1],test_arr[:,:-1],train_arr[:,-1],test_arr[:,-1])


      model_report:dict = evaluate_models(x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test,models=models)
      best_model_score = max(sorted(model_report.values()))
      best_model_name = list(model_report.keys())[
                    list(model_report.values()).index(best_model_score)]
      best_model = models[best_model_name]
      save_object(
          file_path=self.model_trainer_config.model_trainer_path,
          obj=best_model
       )
      predicted = best_model.predict(x_test)
      r2_square = r2_score(y_test, predicted)

      return best_model,r2_square

     except Exception as e:
         raise custom_exception(e,sys)

