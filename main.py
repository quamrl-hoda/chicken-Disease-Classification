from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline 


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"********** Starting {STAGE_NAME} **********")
    data_ingestion_pipeline = DataIngestionTrainPipeline()
    data_ingestion_pipeline.main()  
    logger.info(f"********** Completed {STAGE_NAME} **********\n\n")
except Exception as e:
    logger.exception(e)
    raise e