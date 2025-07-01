# purpose is that if any execution that happens we should be able to log all those information execution and everything in some files so we will be able to track if there are some errors 
import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)

# if __name__=="__main__":
#     logging.info("logging has started")
# for checking the working 