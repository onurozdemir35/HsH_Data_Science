import unittest

class TemperaturUmrechner:
    __einheit = "celsius"
    @staticmethod
    def celsius_zu_fahrenheit(c):
        return (c * 9/5) + 32

    @staticmethod
    def fahrenheit_zu_celsius(f):
        return (f - 32) * 5/9
    
class TestTemperaturUmrechner(unittest.TestCase):
    def test_celsius_zu_fahrenheit(self):
            self.assertEqual(TemperaturUmrechner.celsius_zu_fahrenheit(0), 32.0 )
            self.assertEqual(TemperaturUmrechner.celsius_zu_fahrenheit(100), 212.0)

    def test_fahrenheit_zu_celsius(self):
            self.assertEqual(TemperaturUmrechner.fahrenheit_zu_celsius(32), 0.0)
            self.assertEqual(TemperaturUmrechner.fahrenheit_zu_celsius(212), 100.0)

    def test_standart_einheit(self):
            TemperaturUmrechner.set_standard_einheit("fahrenheit")
            self.assertEqual(TemperaturUmrechner.get_standard_einheit(), "fahrenheit")