import logging
import os
from datetime import datetime

import logger

class CustomLogger:
    def __init__(self,log_dir = 'logs'):
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)
        self.log_file = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, self.log_file)
        logging.basicConfig(
            filename=self.log_file_path,
            format = "[%(asctime)s] [%(levelname)s] - %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))
    

if __name__ == "__main__":
    logger = CustomLogger().get_logger(__file__)
    logger.info("This is a test log message.")
