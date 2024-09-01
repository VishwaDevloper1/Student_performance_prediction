import logging
from _datetime import datetime
import os

LOG_FILE = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,
                    format= "[%(asctime)s] - %(message)s",
                    level=logging.INFO,)
