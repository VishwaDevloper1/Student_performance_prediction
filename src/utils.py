import pandas as pd
import os
import sys
from src.exception import custom_exception
import dill
import pickle
from sklearn.metrics import r2_score
def save_object(file_path,obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj,f)

    except Exception as e:
     raise custom_exception(e,sys)
def evaluate_models(x_train,x_test,y_train,y_test,models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(x_train,y_train)
            y_train_pred = model.predict(x_train)

            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise custom_exception(e,sys)

