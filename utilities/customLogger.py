import logging

class logGen:

    @staticmethod
    def loggen():

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler('.//Logs//automation.log')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger