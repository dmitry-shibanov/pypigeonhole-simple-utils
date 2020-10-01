import unittest

import pypigeonhole_utils.simple.simple_str as simple_str


class SimpleStrTest(unittest.TestCase):
    def test_camel_snake(self):
        s = 'MyCamelString'
        s1 = simple_str.camel2snake(s)
        self.assertTrue(s1 == 'my_camel_string')

        s2 = simple_str.snake2camel(s1)
        self.assertTrue(s2 == s)

    def test_chain_with(self):
        s = simple_str.chain_with('#', 'mickey', 'mouse')
        self.assertTrue(s == 'mickey#mouse')

        s1 = simple_str.chain_with('#', '', 'pluto')
        self.assertTrue(s1 == 'pluto')

    def test_underscore(self):
        s = 'My_Brilliant_Tile'
        s1 = simple_str.underscore2space(s)
        self.assertTrue(s1 == 'My Brilliant Tile')

    def test_unique_id(self):
        s = simple_str.unique_id(4)
        print('ID: ' + s)
        self.assertTrue(len(s) == 8)

    def test_str_hash(self):
        s1 = simple_str.hash_str('This is to be hashed')
        print(s1)
        s2 = simple_str.hash_str('This is to be hashed too')
        print(s2)
        self.assertTrue(s1 != s2)
