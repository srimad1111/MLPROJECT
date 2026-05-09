import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from MLPROJECT.logger import logging
from MLPROJECT.exception import CustomException

if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        a = 1 / 0

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)