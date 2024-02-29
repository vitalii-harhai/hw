import csv
import sys


def sizeof_func(log_file='sizeof_func_log.csv'):
    """
    Calculates the memory size of the function
    :param log_file: log file name in csv format <function name>, <args>, <kwargs>, <size>
    :return: size in bytes
    """
    def wrapper(func):
        def inner(*args, **kwargs):
            size = sys.getsizeof(func(*args, **kwargs)) if args or kwargs else sys.getsizeof(func)
            with open(log_file, 'a') as file:
                csv.writer(file).writerow([func.__name__, args, kwargs, size])
            return func(*args, **kwargs)
        return inner
    return wrapper


@sizeof_func()
def my_func(a, b):
    return a + b
