import logging


def get_and_set_logger():
    logger = logging.getLogger('basic')
    logger.setLevel(logging.DEBUG)

    formatter_1 = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', "%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler('api.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter_1)

    logger.addHandler(file_handler)
