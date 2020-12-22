import os, sys, time, logging, traceback


class Logger():

    '''
    Created logger class with Python's logging facility, for convenient log handling.
    '''

    __logger = None
    __log_handler = None
    __root_dir = os.getcwd()

    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG) #Can be set to other levels


    def add_log_handler(self, log_file):
        
        log_dir = os.path.join(os.path.join(self.__root_dir, 'log/'))
        if (not os.path.exists(log_dir)):
            os.makedirs(log_dir)

        log_file = os.path.join(log_dir, log_file)
        self.__log_handler = logging.FileHandler(filename=log_file, encoding=None) 
        self.__log_handler.setFormatter(logging.Formatter(fmt='%(asctime)s|%(levelname)s|%(message)s'))
        self.__logger.addHandler(self.__log_handler)


    def remove_log_handler(self):
        if (self.__log_handler):
            self.__logger.removeHandler(self.__log_handler)
            self.__log_handler.close()
            self.__log_handler = None

    def info(self, *args, **kwargs):
        self.__logger.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        self.__logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        self.__logger.debug(*args, **kwargs)

    def error(self, *args, **kwargs):
        self.__logger.error(*args, **kwargs)