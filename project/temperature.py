#!/usr/bin/env python3
"""This is the function of temperature converter"""

from error import error


def temperature():
    temperature_unit_input = input('Please enter the unit, "F" or "C"\n--> ')
    temperature_value_input = input('Please enter a value\n--> ')
    if temperature_unit_input.lower() == 'f':
        try:
            temperature_output = round(
                (float(temperature_value_input) - 32) * 5 / 9, 2)
            output = f'{temperature_value_input} Fahrenheit is {temperature_output} Celsius.'
            print(output)
        except:
            error()
            temperature()

    elif temperature_unit_input.lower() == 'c':
        try:
            temperature_output = round(
                float(temperature_value_input) * 9 / 5 + 32, 2)
            output = f'{temperature_value_input} Celsius is {temperature_output} Fahrenheit.'
            print(output)
        except:
            error()
            temperature()
    else:
        error()
        temperature()
