import unittest
import logging
import os
import shutil

import pypigenhole.simpleutils.simple_log as simple_log


# Need to set up the log in the main() method, then in each module/file, import
# simple_log and call logger = simple_log.get_logger(__name__).
class SimpleLogTest(unittest.TestCase):
    def test_level(self):
        simple_log.set_log_level(logging.WARN)
        simple_log.log_to_console()

        logger = simple_log.get_logger(__name__)
        logger.info('This is info - invisible')
        logger.error('This is error - visible')
        self.assertTrue(logger.parent.level == logging.WARN)

    def test_log_to_file(self):
        log_dir = '/tmp/my_test_log/'  # last / is for test only, normally do it without /
        if os.path.exists(log_dir):
            shutil.rmtree(log_dir)  # clean up this.

        simple_log.set_log_level(logging.WARN)
        file_handler = simple_log.log_to_file('test', log_dir)  # if log_dir not exist, it will be created.

        logger = simple_log.get_logger(__name__)
        logger.info('This is info - invisible')
        logger.error('This is error - visible')
        self.assertTrue(logger.parent.level == logging.WARN)
        self.assertTrue(os.path.exists(file_handler.baseFilename))
