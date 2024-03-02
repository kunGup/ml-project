import sys
import pandas as pd
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(TrainPipeline, cls).__new__(cls)

        return cls.instance

    def __init__(self) -> None:
        pass

    def train(self):
        try:
            obj=DataIngestion()

            train_data,test_data=obj.initiate_data_ingestion()

            data_transformation=DataTransformation()

            train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

            modeltrainer = ModelTrainer()

            modeltrainer.initiate_model_trainer(train_arr,test_arr)

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":

    TrainPipeline().train()