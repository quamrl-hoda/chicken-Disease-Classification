from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline 
from src.cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"********** Starting {STAGE_NAME} **********")
    data_ingestion_pipeline = DataIngestionTrainPipeline()
    data_ingestion_pipeline.main()  
    logger.info(f"********** Completed {STAGE_NAME} **********\n\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f"********** Starting {STAGE_NAME} **********")
    prepare_base_model_pipeline = PrepareBaseModelTrainingPipeline()
    prepare_base_model_pipeline.main()  
    logger.info(f"********** Completed {STAGE_NAME} **********\n\n")
except Exception as e:
    logger.exception(e)
    raise e