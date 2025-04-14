from src.MLOps.config.configuration import ConfigurationManager
from src.MLOps.components.model_trainer import ModelTrainer
from src.MLOps import logger 

STAGE_NAME = "Model Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()