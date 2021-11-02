import unittest
import temperature_utils_v2
import pytest


class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_celsius(temp_in))

    def test_convert_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_v2.convert_to_fahrenheit(temp_in))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "f")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils_v2.temperature_tuple(temps_input, "c")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_v2.temperature_tuple(temps_input, "a"))

    def test_temperature_converter(self):
        temps_input = (0, 32, 100, 212, 273, 373)
        expected_f_k = (255.372, 273.15, 310.93, 373.15, 407.04)
        expected_f_c = (-17.78, 0.0, 37.78, 100.0, 133.89)
        expected_c_k = (273.15, 305.15, 373.15, 485.15, 546.15)
        expected_c_f = (32.0, 89.6, 212.0, 413.6, 523.4)
        expected_k_f = (-459.67, -402.07, -279.67, -78.07, 31.73)
        expected_k_c = (-255.37, -241.15, -173.15, -61.15, -.15)
        conversion_order = (("f","k"),("f","c"),("c","k"),("c","f"),("k","f"),("k","c"))
        for expected
        expected_tuples = expected_f_k, expected_f_c, expected_c_k, expected_c_f, expected_k_f, expected_k_c)
        for expected_tuple in expected_tuples
            zip(temps_input, expected_tuple)
        f_k_pairs = zip(temps_input, expected_f_k)
        f_c_pairs = zip(temps_input, expected_f_c)
        c_k_pairs = zip(temps_input, expected_c_k)
        c_f_pairs = zip(temps_input, expected_c_f)
        k_f_pairs = zip(temps_input, expected_k_f)
        k_c_pairs = zip(temps_input, expected_k_c)
        for input_temperature, expected_output in f_k_pairs:
            assert expected_output == pytest.approx(
                temperature_utils_v2.temperature_converter(input_temperature, "f", "k"), .005)
            print(f"Expected  (+/- .005): {expected_output:<7} result: {temperature_utils_v2.temperature_converter(input_temperature, 'f', 'k')}")
