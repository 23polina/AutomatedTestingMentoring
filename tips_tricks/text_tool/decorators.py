import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def calculate_func_execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        time_before_func = datetime.now()
        func_result = func(*args, **kwargs)
        time_after_execution = datetime.now()
        func_execution_time = time_after_execution - time_before_func
        logger.info("Function execution time is calculated %s %s" , func.__name__ , func_execution_time)
        return func_result
    return wrapper
