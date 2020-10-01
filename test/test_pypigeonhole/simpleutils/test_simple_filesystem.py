import unittest
import os
import shutil

import pypigenhole.simpleutils.simple_filesystem as simple_filesystem


class SimpleFilesystemTest(unittest.TestCase):
    def test_zip(self):
        tmp_file = '/tmp/tmp.txt'
        del_file(tmp_file)

        gzip_file = tmp_file + '.gz'
        del_file(gzip_file)

        unzip_file = '/tmp/tmp_unzip.txt'
        del_file(unzip_file)

        # test starts
        with open(tmp_file, 'w') as f:
            f.write('abc ' * 3)

        simple_filesystem.zip_file(tmp_file, gzip_file)
        simple_filesystem.unzip_file(gzip_file, unzip_file)

        with open(unzip_file, 'r') as f:
            lines = f.readlines()
            self.assertTrue(lines[0] == 'abc abc abc ')

    def test_latest_file(self):
        test_file = '/tmp/latest_test_file.txt'
        del_file(test_file)
        with open(test_file, 'w') as f:
            f.write('abc ' * 3)

        latest = simple_filesystem.latest_file_in('/tmp', pattern='*')
        print(latest)
        self.assertTrue(latest.replace('\\', '/') == test_file)

    def test_latest_folder(self):
        test_folder = '/tmp/latest_test_folder'
        if os.path.exists(test_folder):
            shutil.rmtree(test_folder)
        os.makedirs(test_folder)

        latest = simple_filesystem.latest_folder_in('/tmp', pattern='*/')  # this / means folder
        print(latest)
        self.assertTrue(latest.replace('\\', '/')[:-1] == test_folder)  # remove last /


def del_file(file: str):
    if os.path.exists(file):
        os.remove(file)
