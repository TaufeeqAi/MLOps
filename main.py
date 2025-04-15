from src.MLOps import logger
from src.MLOps.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.MLOps.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.MLOps.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.MLOps.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.MLOps.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

STAGE_NAME= "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME}<<<<<<<")
    obj=DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME= "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME}<<<<<<<")
    obj=DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME= "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME}<<<<<<<")
    obj=DataTransformationTrainingPipeline()
    obj.initiate_data_transformation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME= "Model Trainnig Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME}<<<<<<<")
    obj=ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME= "Model Evaluation Stage"

try:
    logger.info(f">>>>>> Stage: {STAGE_NAME}<<<<<<<")
    obj=ModelEvaluationPipeline()
    obj.initiate_model_evaluation()
    logger.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx=========x")

except Exception as e:
        logger.exception(e)
        raise e