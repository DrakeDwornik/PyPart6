from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    celsius_temp = (fahrenheit_temp - 32) / 1.8
    celsius_temp = round(celsius_temp, 2)
    return celsius_temp


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit_temp = celsius_temp * 1.8 + 32
    fahrenheit_temp = round(fahrenheit_temp, 2)
    return fahrenheit_temp


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    converted_temperatures = []
    for temperature in temperatures:
        if input_unit_of_measurement == "c":
            converted_temperatures.append(convert_to_fahrenheit(temperature))
        elif input_unit_of_measurement == "f":
            converted_temperatures.append(convert_to_celsius(temperature))

    result = tuple(zip(temperatures, converted_temperatures))
    return result