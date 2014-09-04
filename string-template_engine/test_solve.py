import unittest
from solve import map_of_vars
from solve import template_engine

class test_template_engine(unittest.TestCase):
    def test_single_variable_expression(self):
        map_of_vars.put('name', 'Cenk')
        r = template_engine.evaluate('Hello {$name}', map_of_vars)
        self.assertEqual(r, 'Hello Cenk')

if __name__ == '__main__':
    unittest.main()
