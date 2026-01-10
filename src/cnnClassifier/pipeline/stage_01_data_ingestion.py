from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.exception(e)
            raise e

if __name__ == "__main__":
    try:
        logger.info(f"********** Starting {STAGE_NAME} **********")
        data_ingestion_pipeline = DataIngestionTrainPipeline()
        data_ingestion_pipeline.main()  
        logger.info(f"********** Completed {STAGE_NAME} **********\n\n")
    except Exception as e:  
        logger.exception(e)
        raise e