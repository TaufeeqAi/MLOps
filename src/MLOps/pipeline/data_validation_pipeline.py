from src.MLOps.config.configuration import ConfigurationManager
from src.MLOps.components.data_validation import DataValidation
from src.MLOps import logger 

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config= ConfigurationManager()
        data_validation_config= config.get_data_validation_config()
        data_validation= DataValidation(data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME}<<<<<<<")
        obj=DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")

    except Exception as e:
        logger.exception(e)
        raise e