#!/usr/bin/env python3
"""This is the function of weight converter"""

from error import error


def weight():
    # Take input of unit that "from" and "to" with the value.
    weight_unit_input = input(
        'Please enter a unit from the list:\nlb\noz\ng\nkg\n--> ')
    weight_value_input = input('Please enter a value\n--> ')
    weight_unit_output = input(
        'Which unit to convert to?\nlb\noz\ng\nkg\n--> ')
    # Convert from lb to others.
    if weight_unit_input.lower() == 'lb':
        try:
            if weight_unit_output.lower() == 'oz':
                result = round(float(weight_value_input) * 16, 4)
            elif weight_unit_output.lower() == 'g':
                result = round(float(weight_value_input) * 453.592, 4)
            elif weight_unit_output.lower() == 'kg':
                result = round(float(weight_value_input) / 2.205, 4)
            output = f'{weight_value_input} lb is {result} {weight_unit_output.lower()}.'
            print(output)
        except:
            error()
            weight()

    # Convert from oz to others.
    elif weight_unit_input.lower() == 'oz':
        try:
            if weight_unit_output.lower() == 'lb':
                result = round(float(weight_value_input) / 16, 4)
            elif weight_unit_output.lower() == 'g':
                result = round(float(weight_value_input) * 28.3495, 4)
            elif weight_unit_output.lower() == 'kg':
                result = round(float(weight_value_input) / 35.274, 4)
            output = f'{weight_value_input} oz is {result} {weight_unit_output.lower()}.'
            print(output)

        except:
            error()
            weight()

    # Convert from g to others.
    elif weight_unit_input.lower() == 'g':
        try:
            if weight_unit_output.lower() == 'lb':
                result = round(float(weight_value_input) / 453.592, 4)
            elif weight_unit_output.lower() == 'oz':
                result = round(float(weight_value_input) / 28.3495, 4)
            elif weight_unit_output.lower() == 'kg':
                result = round(float(weight_value_input) / 1000, 4)
            output = f'{weight_value_input} g is {result} {weight_unit_output.lower()}.'
            print(output)
        except:
            error()
            weight()
    # Convert from kg to others.
    elif weight_unit_input.lower() == 'kg':
        try:
            if weight_unit_output.lower() == 'lb':
                result = round(float(weight_value_input) * 2.20462, 4)
            elif weight_unit_output.lower() == 'oz':
                result = round(float(weight_value_input) * 35.274, 4)
            elif weight_unit_output.lower() == 'g':
                result = round(float(weight_value_input) * 1000, 4)
            output = f'{weight_value_input} kg is {result} {weight_unit_output.lower()}.'
            print(output)
        except:
            error()
            weight()
