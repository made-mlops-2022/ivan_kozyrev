import logging
import logging.config


def get_logger():
    console_formatter = logging.Formatter(
        '"%(asctime)s - [%(levelname)s]\t- %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    logger = logging.getLogger()
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)

    return logger
