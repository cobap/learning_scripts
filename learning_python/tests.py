# Importamos Unittest
import unittest

# Temos uma função específica
def fun(x):
    return x + 1

# Criamos uma classe para testar meus testes, que herda de TestCase
class MyTest(unittest.TestCase):
    # A função test chama a função fun para 3 e precisa resultar 4
    def test(self):
        self.assertEqual(fun(3), 4)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
