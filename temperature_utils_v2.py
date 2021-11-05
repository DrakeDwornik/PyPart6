from typing import Iterable, Tuple



def temperature_converter(input_temperature, input_unit, output_unit):
    temperature_dictionary = {}
    temperature_dictionary[input_unit] = input_temperature
    if input_unit == "c":
        temperature_dictionary["k"] = input_temperature + 273.15
        temperature_dictionary["f"] = temperature_dictionary["c"] * 1.8 + 32
    elif input_unit == "f":
        temperature_dictionary["c"] = (input_temperature - 32 ) / 1.8
        temperature_dictionary["k"] = temperature_dictionary["c"] + 273.15
    elif input_unit == "k":
        temperature_dictionary["c"] = input_temperature - 273.15
        temperature_dictionary["f"] = (input_temperature - 273.15) * 1.8 + 32
    return round(float(temperature_dictionary[output_unit]),2)

def temperature_tuple_versitale(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_measurement: str) -> Tuple[Tuple]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :param output_unit_of_measurement: The unit of measure for the second item in the inner tuples
    :return: A tuple of tuples
    """
    converted_temperatures = []
    for temperature in temperatures:
        converted_temperature = temperature_converter(temperature, input_unit_of_measurement, output_unit_of_measurement)
        converted_temperatures.append((temperature, converted_temperature,input_unit_of_measurement,output_unit_of_measurement))

    result = tuple(converted_temperatures)
    return result

print(temperature_tuple_versitale((0, 32, 100, 212, 273, 373), "f", "k"))