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


def convert_to_fahrenheit(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahrenheit_temp = celsius_temp * 1.8 + 32
    fahrenheit_temp = round(fahrenheit_temp, 2)
    return fahrenheit_temp

def temperature_converter(input_temperature, input_unit, output_unit):
    temperature_dictionary = {}
    temperature_dictionary[input_unit] = input_temperature
    if input_unit == "c":
        temperature_dictionary["k"] = input_temperature - 273.15
        temperature_dictionary["f"] = temperature_dictionary["c"] * 1.8 + 32
    elif input_unit == "f":
        temperature_dictionary["c"] = (input_temperature - 32 ) / 1.8
        temperature_dictionary["k"] = temperature_dictionary["c"] + 273.15
    elif input_unit == "k":
        temperature_dictionary["c"] = input_temperature + 273.15
        temperature_dictionary["f"] = (input_temperature - 273.15) * 1.8 + 32
    return temperature_dictionary[output_unit]

def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_meansurement: str) -> Tuple[Tuple[float, float]]:
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
            converted_temperatures.append(temperature_converter(temperature,"c","f"))
        elif input_unit_of_measurement == "f":
            converted_temperatures.append(temperature_converter(temperature,"f","c"))

    result = tuple(zip(temperatures, converted_temperatures))
    return result

def temperature_tuple_versitale(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :param output_unit_of_meansurement: The unit of measure for the second item in the inner tuples
    :return: A tuple of tuples
    """
    converted_temperatures = []
    for temperature in temperatures:
        converted_temperature = temperature_converter(temperature, input_unit_of_measurement, output_unit_of_measurement)
        converted_temperatures.append(round(float(converted_temperature),2))


    result = tuple(zip(temperatures, converted_temperatures))
    return result

