import unittest
from solve import MissingValueError
from solve import map_of_vars
from solve import template_engine

class test_template_engine(unittest.TestCase):
    def test_single_variable_expression(self):
        map_of_vars.put('name', 'Cenk')
        r = template_engine.evaluate('Hello {$name}', map_of_vars)
        self.assertEqual(r, 'Hello Cenk')

    def test_multiple_variable_expression(self):
        map_of_vars.init()
        map_of_vars.put('first_name', 'Cenk')
        map_of_vars.put('last_name', 'Civici')
        r = template_engine.evaluate('Hello {$first_name} {$last_name}', map_of_vars)
        self.assertEqual(r, 'Hello Cenk Civici')

    def test_var_not_exist_exception(self):
        map_of_vars.init()
        self.assertRaises(MissingValueError, template_engine.evaluate, 'Hello {$first_name}', map_of_vars)

    def test_complex_cases(self):
        map_of_vars.init()
        map_of_vars.put('name', 'Cenk')
        r = template_engine.evaluate('Hello {${$name}}', map_of_vars)
        self.assertEqual(r, 'Hello {$Cenk}')

if __name__ == '__main__':
    unittest.main()
