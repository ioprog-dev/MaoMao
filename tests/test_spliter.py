import unittest
from string_spliter import spliter  # Убедитесь, что этот импорт соответствует вашей структуре файлов

class TestSpliter(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spliter('ABC', 1), ['A', 'B', 'C'])

    def test_2(self):
        with self.assertRaises(ValueError):
            spliter('ABCDEFG', 2)  # Длина не кратна 2

    def test_3(self):
        self.assertEqual(spliter('HelloWorld', 2), ['He', 'll', 'oW', 'or', 'ld'])

    def test_4(self):
        self.assertEqual(spliter('123456', 3), ['123', '456'])

    def test_5(self):
        with self.assertRaises(ValueError):
            spliter('ABC', 2)  # Длина не кратна 2

    def test_6(self):
        with self.assertRaises(ValueError):
            spliter('Hello', 3)  # Длина не кратна 3

    def test_type_error_string(self):
        with self.assertRaises(TypeError):
            spliter(123, 2)  # Первый аргумент не строка

    def test_type_error_integer(self):
        with self.assertRaises(TypeError):
            spliter('Hello', '2')  # Второй аргумент не целое число

if __name__ == '__main__':
    unittest.main()
