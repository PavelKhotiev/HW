import functools
import logging
import sys


def log(filename=None):
    """декоратор log - логирует вызов функции и ее результат в файл или в консоль.
    Принимает один необязательный аргумент filename, который определяет путь к файлу,
    в который будут записываться логи. Если filenameне задан, то логи будут выводиться в консоль.
     Если вызов функции закончился ошибкой, то записывается
      сообщение об ошибке и входные параметры функции.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

            if filename:
                handler = logging.FileHandler(filename)
            else:
                handler = logging.StreamHandler(sys.stdout)

            handler.setFormatter(formatter)
            logger.addHandler(handler)

            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise
            finally:
                logger.removeHandler(handler)

        return wrapper

    return decorator
