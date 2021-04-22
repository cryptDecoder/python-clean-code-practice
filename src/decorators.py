# This is the example of python decorators
from src.Logger import logMethod

log = logMethod()


def operations(function):
    def wrapper(*args, **kwargs):
        try:
            log.info("User input numbers: {0}".format(*args))
            response = function(*args, **kwargs)
            log.info("Result: {0}".format(response))
            return response

        except Exception as err:
            log.error(err)

    return wrapper


# Using decorator
@operations
def substraction(a, b):
    return a - b


@operations
def addition(a, b):
    return a + b


substraction(12, 34)
addition(45, 67)
