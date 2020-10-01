import unittest
import time
import platform

import pypigeonhole_utils.simple.simple_os as simple_os


class SimpleOsTest(unittest.TestCase):
    def test_run_cmd_to_string_output(self):
        if platform.system() != 'Windows':
            return

        code, result = simple_os.run_exe('cmd /c dir')
        self.assertTrue(code == 0)
        print('result: ' + result)
        print('-------------------------------------------------------------------------')

        code, result = simple_os.run_exe('non_exist')
        self.assertTrue(code == -1)
        print('result: ' + str(result))

    def test_timeout(self):
        # sleep is in anaconda Scripts folder, otherwise, install unxtools from anaconda
        now = time.time()
        code, result = simple_os.run_exe('sleep 5', timeout=2)  # sleep for 5, but timeout in 2 seconds
        print('done: {}'.format(code))
        dur = time.time() - now
        print('duration: {} seconds'.format(dur))
        self.assertTrue(dur < 3)
        self.assertTrue(code != 0)  # is 1, not zero.
        print(result)  # empty

    def test_run_proc(self):
        if platform.system() != 'Windows':
            return

        code, res = simple_os.run_proc('java -version')
        self.assertTrue(code == 0)
        print(code)
        print(res)

        code, res = simple_os.run_proc('cmd /c dir')
        self.assertTrue(code == 0)
        print(code)
        print(res)
