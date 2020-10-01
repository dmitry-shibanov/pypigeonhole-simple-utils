import unittest
import os

import pypigeonhole_utils.simple.simple_timer as simple_timer
import pypigeonhole_utils.simple.simple_log as simple_log


class SimpleTimerTest(unittest.TestCase):
    def test_console_print(self):
        with simple_timer.perf_bm('test') as pbm:
            pbm.print('first step')
            print('-----I am doing first step')
            pbm.print('2nd step')
            print('-----I am doing first step')

    def test_log_file_print(self):
        file_handler = simple_log.log_to_file('pbm', '/tmp')
        logger = simple_log.get_logger(__name__)
        with simple_timer.perf_bm('logging_test', logger.info) as pbm:
            pbm.print('first step')
            print('-----I am doing first step')
            pbm.print('2nd step')
            print('-----I am doing first step')
            self.assertTrue(os.path.exists(file_handler.baseFilename))
