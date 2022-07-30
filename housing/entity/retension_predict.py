import os
import sys

from housing.exception import HousingException
from housing.util.util import load_object

import pandas as pd


class RetensionData:

    def __init__(self,
                 satisfaction_level: float,
                 last_evaluation: float,
                 number_project: float,
                 average_montly_hours: int,
                 time_spend_company: int,
                 Work_accident: int,
                 promotion_last_5years: int,
                 sales: str,
                 salary: str,
                 left: int = None
                 ):
        try:
            self.satisfaction_level = satisfaction_level
            self.last_evaluation = last_evaluation
            self.number_project = number_project
            self.average_montly_hours = average_montly_hours
            self.time_spend_company = time_spend_company
            self.Work_accident = Work_accident
            self.promotion_last_5years = promotion_last_5years
            self.sales = sales
            self.salary = salary
            self.left = left
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_housing_input_data_frame(self):

        try:
            housing_input_dict = self.get_housing_data_as_dict()
            return pd.DataFrame(housing_input_dict)
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_housing_data_as_dict(self):
        try:
            input_data = {
                "satisfaction_level": [self.satisfaction_level],
                "last_evaluation": [self.last_evaluation],
                "number_project": [self.number_project],
                "average_montly_hours": [self.average_montly_hours],
                "time_spend_company": [self.time_spend_company],
                "Work_accident": [self.Work_accident],
                "promotion_last_5years": [self.promotion_last_5years],
                "sales": [self.sales],
                "salary": [self.salary]}
            return input_data
        except Exception as e:
            raise HousingException(e, sys)


class RetensionPredictor:

    def __init__(self, model_dir: str):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_latest_model_path(self):
        try:
            folder_name = list(map(int, os.listdir(self.model_dir)))
            latest_model_dir = os.path.join(self.model_dir, f"{max(folder_name)}")
            file_name = os.listdir(latest_model_dir)[0]
            latest_model_path = os.path.join(latest_model_dir, file_name)
            return latest_model_path
        except Exception as e:
            raise HousingException(e, sys) from e

    def predict(self, X):
        try:
            model_path = self.get_latest_model_path()
            model = load_object(file_path=model_path)
            left = model.predict(X)
            return left
        except Exception as e:
            raise HousingException(e, sys) from e