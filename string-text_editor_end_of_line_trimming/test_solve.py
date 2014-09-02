import unittest
from solve import trimmer

class test_trimmer(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(trimmer('abc '), 'abc')

    def test_simple_double(self):
        self.assertEqual(trimmer('abc  '), 'abc')

    def test_tap(self):
        self.assertEqual(trimmer('abc\t'), 'abc')

    def test_not_trim_beginning(self):
        self.assertEqual(trimmer(' abc'), ' abc')

    def test_around_new_line(self):
        self.assertEqual(trimmer('ab\n cd \n'), 'ab\ncd\n')

    def test_cross_platform(self):
        self.assertEqual(trimmer('ab\r\ncd\n'), 'ab\r\ncd\n')

if __name__ == '__main__':
    unittest.main()
