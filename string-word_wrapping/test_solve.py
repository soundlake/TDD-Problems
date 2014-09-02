import unittest
from solve import word_wrapper

class TestTDDProblems(unittest.TestCase):
    def test_long_enough(self):
        ww = word_wrapper(60)
        self.assertEqual(ww.wrapIt('abcdefghijklmnopqrsturvwxyz'), 'abcdefghijklmnopqrsturvwxyz')

    def test_simple_wrap(self):
        ww = word_wrapper(3)
        self.assertEqual(ww.wrapIt('abcdef'), ['abc', 'def'])

    def test_wrap_with_space(self):
        ww = word_wrapper(3)
        self.assertEqual(ww.wrapIt('abc def'), ['abc', 'def'])

    def test_simple_and_space(self):
        ww = word_wrapper(3)
        self.assertEqual(ww.wrapIt('abcdef abc'), ['abc', 'def', 'abc'])

    def test_many_space(self):
        ww = word_wrapper(3)
        self.assertEqual(ww.wrapIt('a b c d e f'), ['a b', 'c d', 'e f'])


if __name__ == '__main__':
    unittest.main()
