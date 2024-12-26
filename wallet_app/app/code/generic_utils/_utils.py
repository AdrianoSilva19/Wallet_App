import logging
from functools import wraps
logger = logging.getLogger(__name__)

def logging_decorator_factory(severity,message,exception=TypeError,service=None):
    def logger_decorator(original_function):
        @wraps(original_function)
        def new_function(*args,**kwargs):
            try:
                return original_function(*args,**kwargs)
                
            except Exception as e:
                logger.error(
                            f"Function name: {original_function.__name__:} \n"
                            f"Severity: {severity} \n"
                            f"Message: {message} \n"
                            f"Exception: {exception}\n"
                            f"Service name: {service}\n")               
        return new_function
    return logger_decorator