import logging
logger = logging.getLogger(__name__)

def logging_decorator_factory(severity,message,exception=TypeError,service=None):
    def logger_decorator(original_function):
        def new_function(*args,**kwargs):
            try:
                return original_function(*args,**kwargs)
                
            except:
                logger.error(f"This Error Works \n"
                            f"Function name: {original_function.__name__:} \n"
                            f"Severity:{severity} \n"
                            f"Message:{message} \n"
                            f"Exception: {exception}\n"
                            f"Service name:{service}")
               
        return new_function
    return logger_decorator