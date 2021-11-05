import itertools
import unittest
import temperature_utils_v2
import pytest


class TemperatureUtilsTest(unittest.TestCase):



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
        expected_k_c = (-273.15, -241.15, -173.15, -61.15, -.15)
        conversion_order = (("f","k"),("f","c"),("c","k"),("c","f"),("k","f"),("k","c"))
        expected_tuples = (expected_f_k, expected_f_c, expected_c_k, expected_c_f, expected_k_f, expected_k_c)
        # print(tuple(zip(expected_tuples,temps_input,conversion_order)))
        for expected_tuple, conversion in tuple(zip(expected_tuples,conversion_order)):
            print(f"-------Starting {conversion}")
            for expected, temp_input in zip(expected_tuple, temps_input):
                args = (temp_input,) + conversion
                print(args)
                assert expected == pytest.approx(
                    temperature_utils_v2.temperature_converter(*args), .005)
                print(
                    f"Expected  (+/- .005): {expected:<7} result: {temperature_utils_v2.temperature_converter(*args)}")

    def test_temperature_tuple_versatile(self):
        temps_input = (0, 32, 100, 212, 273)
        expected_f_k = (255.37, 273.15, 310.93, 373.15, 407.04)
        expected_f_c = (-17.78, 0.0, 37.78, 100.0, 133.89)
        expected_c_k = (273.15, 305.15, 373.15, 485.15, 546.15)
        expected_c_f = (32.0, 89.6, 212.0, 413.6, 523.4)
        expected_k_f = (-459.67, -402.07, -279.67, -78.07, 31.73)
        expected_k_c = (-273.15, -241.15, -173.15, -61.15, -.15)
        conversion_order = (("f", "k"), ("f", "c"), ("c", "k"), ("c", "f"), ("k", "f"), ("k", "c"))
        expected_tuples = (expected_f_k, expected_f_c, expected_c_k, expected_c_f, expected_k_f, expected_k_c)
        expected_tuples_with_conversion = (tuple(zip(expected_tuples,conversion_order)))
        # print(expected_tuples_with_conversion)
        # print(expected_tuples_with_conversion)
        for expected_out_temps, conversion in expected_tuples_with_conversion:
            input_unit, output_unit = conversion
            args = (temps_input, input_unit,output_unit)
            output_input_tup = tuple(zip(expected_out_temps, temps_input))
            test_out_tup = ()
            print(output_input_tup)
            for single_out, single_in in output_input_tup:
                test_out_tup += ((single_in, single_out, input_unit, output_unit),)



            print(f"-------Starting {input_unit} -> {output_unit}")
            print(args)
            print(f"Expected: {test_out_tup} result: {temperature_utils_v2.temperature_tuple_versitale(*args)}")
            self.assertEqual(test_out_tup, temperature_utils_v2.temperature_tuple_versitale(*args))
