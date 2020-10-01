import unittest
import os
import datetime

import yaml

import pypigeonhole_utils.extra.simple_yaml as simple_yaml


class YamlVarTest(unittest.TestCase):
    def test_env_var(self):
        os.environ['HOST'] = '1.2.3.4'

        curr_folder = os.path.dirname(os.path.abspath(__file__))
        settings = simple_yaml.load_file(os.path.join(curr_folder, 'env_var_test.yaml'), {})
        server = settings['server']
        print(server['host'])
        self.assertTrue(server['host'] == '1.2.3.4')  # from env
        print(server['path'])
        self.assertTrue(server['path'] == '/tmp/folder1')  # from default
        print(server['url'])
        self.assertTrue(server['url'] == 'https://1.2.3.4/welcome')  # from default
        print(server['nested'])
        self.assertTrue(server['nested'] == '1.2.3.4/folder1/1.2.3.4/folder2')

    def test_date_time(self):
        kvp = yaml.load("""dt: !!timestamp '2010-11-17 13:12:11'""", yaml.FullLoader)
        print(kvp)
        print(type(kvp['dt']))
        self.assertTrue(kvp['dt'] == datetime.datetime(2010, 11, 17, 13, 12, 11))
