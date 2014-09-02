import unittest
from solve import infix_to_postfix

class test_infix_to_postfix(unittest.TestCase):
    def test_simple_add(self):
        exp = infix_to_postfix('3 + 2')
        self.assertEqual(exp, '3 2 +')

    def test_simple_sub(self):
        exp = infix_to_postfix('3 - 2')
        self.assertEqual(exp, '3 2 -')

    def test_simple_mul(self):
        exp = infix_to_postfix('3 * 2')
        self.assertEqual(exp, '3 2 *')

    def test_simple_div(self):
        exp = infix_to_postfix('3 / 2')
        self.assertEqual(exp, '3 2 /')

    def test_comb_add_add(self):
        exp = infix_to_postfix('3 + 2 + 1')
        self.assertEqual(exp, '3 2 + 1 +')

    def test_comb_mul_mul(self):
        exp = infix_to_postfix('3 * 2 * 1')
        self.assertEqual(exp, '3 2 * 1 *')

    def test_precedence(self):
        exp = infix_to_postfix('3 - 2 * 1')
        self.assertEqual(exp, '3 2 1 * -')

    def test_parenthesis(self):
        exp = infix_to_postfix('3 + (2 + 1)')
        self.assertEqual(exp, '3 2 1 + +')

    def test_complex(self):
        exp = infix_to_postfix('3 + (2 + 1) * 4')
        self.assertEqual(exp, '3 2 1 + 4 * +')

    def test_deeper_parenthesis(self):
        exp = infix_to_postfix('3 + (2 / (1 + 5)) * 4')
        self.assertEqual(exp, '3 2 1 5 + / 4 * +')


if __name__ == '__main__':
    unittest.main()
