import os
from src.MLOps import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from src.MLOps.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets (75% and 25% split)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index= False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)