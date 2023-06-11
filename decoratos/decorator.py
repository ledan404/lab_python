"""Decorator that logs exceptions"""
import logging


def logged(arg_exception, arg_mode):
    """Logger decorator functio"""

    def logger(func):
        """logger"""
        def inner(*args, **kwargs):
            res = None
            try:
                res = func(*args, **kwargs)
            except arg_exception:
                if arg_mode == "file":
                    logging.basicConfig(filename="result.log",
                                        format="%(asctime)s:%(levelname)s:%(message)s")
                    logging.error(arg_exception())
                if arg_mode == "console":
                    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s")
                    logging.error(arg_exception())
            return res

        return inner

    return logger
