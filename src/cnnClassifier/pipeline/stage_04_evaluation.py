from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.evaluation import Evaluation
from cnnClassifier import logger


STAGE_NAME = "Model Evaluation Stage"
class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            eval_config = config.get_evaluation_config()
            evaluation = Evaluation(config=eval_config)
            evaluation.evaluation()
            evaluation.save_score()
            logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
        except Exception as e:
            logger.exception(e)
            raise e
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\n")
    except Exception as e:
        logger.exception(e)