import os
import logging
from datetime import datetime

class customlogger:
    def __init__(self,log_dir="logs"):
         # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # create timestamp logfile name
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        LOG_FILE_PATH = os.path.join(self.logs_dir, log_file)

        logging.basicConfig(
            filename=LOG_FILE_PATH,
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,
        )
    def get_logger(self,name=__file__):
        return logging.getLogger(os.path.basename(name))
    
if __name__== "__main__":
    logger = customlogger()
    logger.get_logger(__file__)
    logger.info("")