import unittest
from solve import check_amount

class test_check_amount(unittest.TestCase):
    def template(self, raw, spell):
        ca = check_amount(raw)
        self.assertEqual(str(ca), spell)

    def test_zero(self):
        self.template(0, 'Zero dollar')
    def test_one(self):
        self.template(1, 'One dollar')
    def test_one_cent(self):
        self.template(0.01, '01/100 dollar')

    def test_cents(self):
        self.template(0.04, '04/100 dollars')

    def test_ones_1(self):
        self.template(5, 'Five dollars')
    def test_ones_2(self):
        self.template(1.1, 'One and 10/100 dollars')

    def test_tens_1(self):
        self.template(15, 'Fifteen dollars')
    def test_tens_2(self):
        self.template(12.24, 'Twelve and 24/100 dollars')
    def test_tens_3(self):
        self.template(10.04, 'Ten and 04/100 dollars')

    def test_dec_1(self):
        self.template(20, 'Twenty dollars')
    def test_dec_2(self):
        self.template(70, 'Seventy dollars')
    def test_dec_3(self):
        self.template(63, 'Sixty-three dollars')
    def test_dec_4(self):
        self.template(97.2, 'Ninety-seven and 20/100 dollars')


if __name__ == '__main__':
    unittest.main()
