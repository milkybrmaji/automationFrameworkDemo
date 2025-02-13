import logging
import os

class logGen:

    @staticmethod
    def loggen():
        logger_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../Logs/automation.log")
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(logger_path)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger