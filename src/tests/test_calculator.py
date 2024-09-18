import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_valid_time_format(self):
        self.assertTrue(self.calculator.is_valid_time_format('08:30'))
        self.assertFalse(self.calculator.is_valid_time_format('0830'))
        self.assertFalse(self.calculator.is_valid_time_format('8:30'))

    def test_format_time(self):
        self.assertEqual(self.calculator.format_time('0830'), '08:30')
        self.assertEqual(self.calculator.format_time('08:30'), '08:30')
        self.assertEqual(self.calculator.format_time('8:30'), '8:30')

    def test_calculate_hours_no_break(self):
        result = self.calculator.calculate_hours('08:00', '17:00')
        self.assertEqual(result, '9 horas 0 minutos')

    def test_calculate_hours_with_break(self):
        result = self.calculator.calculate_hours('08:00', '17:00', '01:00')
        self.assertEqual(result, '8 horas 0 minutos')

    def test_calculate_hours_invalid_format(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_hours('08:00', '17:00', '01')

    def test_calculate_hours_with_inverted_times(self):
        result = self.calculator.calculate_hours('22:00', '06:00')
        self.assertEqual(result, '8 horas 0 minutos')

if __name__ == '__main__':
    unittest.main()
