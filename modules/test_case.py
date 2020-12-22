import unittest, sys, collections
import logging, os, time, re
from datetime import datetime

from .logger import Logger


class TestUnit(unittest.TestCase):

    __root_dir = os.getcwd()

    def __init__(self, *args, **kwargs):
        super(TestUnit, self).__init__(*args, **kwargs)
        self.__logger = Logger()


    def setUp(self):
        '''
        SetUp method. The test runner invokes this after every test is called.
        '''
        self.info('Test case started.')
        self.__init_logger()


    def tearDown(self):
        '''
        TearDown method. The test runner invokes this after every test is called.
        Logs the results of the test case.
        '''

        if hasattr(self, '_outcome'):  
            result = self.defaultTestResult()  
            self._feedErrorsToResult(result, self._outcome.errors)
        error = self.get_message(result.errors)
        failure = self.get_message(result.failures)
        ok = not error and not failure
        if not ok:
            if error:
                msg =  [x for x in error.split('\n')[1:] if not x.startswith(' ')][0]
                typ = 'ERROR'
                self.error("%s: \n %s, \n %s" % (typ, self.id(), msg))
                self.info("Test result: ERROR")
                #self.__update_test_report('Error')
            else:
                msg = [x for x in failure.split('\n')[1:] if not x.startswith(' ')][0]
                typ = 'FAIL'
                self.warning("%s: \n %s, \n %s" % (typ, self.id(), msg))
                self.info("Test result: FAILURE")
                #self.__update_test_report('Fail')
        else:
            self.info("Test result: SUCCESS")
            #self.__update_test_report('Pass')

        # Remove the test case-specific log handler
        self.__deinit_logger()
        super(TestUnit, self).tearDown()

    def get_message(self, exc_list):
        if exc_list and exc_list[-1][0] is self:
            return exc_list[-1][1]

    def exception(self, *args, **kwargs):
        '''Log an exception.'''
        self.__logger.exception(*args, **kwargs)

    def error(self, *args, **kwargs):
        '''Log an error message.'''
        self.__logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        '''Log a warning message.'''
        self.__logger.warning(*args, **kwargs)

    def info(self, *args, **kwargs):
        '''Log an informational message.'''
        self.__logger.info(*args, **kwargs)

    def debug(self, *args, **kwargs):
        '''Log a debug message.'''
        self.__logger.debug(*args, **kwargs)

    
    def __init_logger(self):
        self.__logger = Logger()
        log_file_format = datetime.fromtimestamp(time.time()).strftime('{}-%d%B%Y-%I%M%S%p'.format(self.id().split('.').pop(2)))
        self.__log_file = '{}.log'.format(log_file_format)
        self.__logger.add_log_handler(self.__log_file)

    def __deinit_logger(self):
        if (self.__logger):
            self.__logger.remove_log_handler()

if __name__ == "__main__":
    unittest.main()