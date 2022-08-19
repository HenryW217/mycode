#!/usr/bin/env python3
"""This is the function of cooking volume converter"""

from error import error


def cooking():
    # Take input of unit that "from" and "to" with the value.
    cooking_unit_input = input(
        'Please enter a unit from the list:\nml\nteaspoon\ntablespoon\ncup\nfloz\npt\nqt\n--> ')
    cooking_value_input = input('Please enter a value\n--> ')
    cooking_unit_output = input(
        'Which unit to convert to?\nml\nteaspoon\ntablespoon\ncup\nfloz\npt\nqt\n--> ')
    # Convert from ml to others.
    if cooking_unit_input.lower() == 'ml':
        try:
            if cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) / 4.929, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) / 14.787, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) / 240, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) / 29.574, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) / 473.2, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 946.4, 4)
            output = f'{cooking_value_input} ml is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()
    # Convert from teaspoon to others.
    elif cooking_unit_input.lower() == 'teaspoon':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 4.929, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) / 3, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) / 48.692, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) / 6, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) / 96, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 192, 4)
            output = f'{cooking_value_input} teaspoon is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()

    # Convert from tablespoon to others.
    elif cooking_unit_input.lower() == 'tablespoon':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 14.787, 4)
            elif cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) * 3, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) / 16.231, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) / 2, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) / 32, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 64, 4)
            output = f'{cooking_value_input} tablespoon is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()
    # Convert from cup to others.
    elif cooking_unit_input.lower() == 'cup':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 240, 4)
            elif cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) * 48.6922, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) * 16.2307, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) * 8.11537, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) / 1.972, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 3.943, 4)
            output = f'{cooking_value_input} cup is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()

    # Convert from floz to others.
    elif cooking_unit_input.lower() == 'floz':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 29.574, 4)
            elif cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) * 6, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) * 2, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) / 8.11537, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) / 16, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 32, 4)
            output = f'{cooking_value_input} floz is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()

    # Convert from pt to others.
    elif cooking_unit_input.lower() == 'pt':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 473.176, 4)
            elif cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) * 96, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) * 32, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) * 1.97157, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) * 16, 4)
            elif cooking_unit_output.lower() == 'qt':
                result = round(float(cooking_value_input) / 2, 4)
            output = f'{cooking_value_input} pt is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()

    # Convert from qt to others.
    elif cooking_unit_input.lower() == 'qt':
        try:
            if cooking_unit_output.lower() == 'ml':
                result = round(float(cooking_value_input) * 946.353, 4)
            elif cooking_unit_output.lower() == 'teaspoon':
                result = round(float(cooking_value_input) * 192, 4)
            elif cooking_unit_output.lower() == 'tablespoon':
                result = round(float(cooking_value_input) * 64, 4)
            elif cooking_unit_output.lower() == 'cup':
                result = round(float(cooking_value_input) * 3.94314, 4)
            elif cooking_unit_output.lower() == 'floz':
                result = round(float(cooking_value_input) * 32, 4)
            elif cooking_unit_output.lower() == 'pt':
                result = round(float(cooking_value_input) * 2, 4)
            output = f'{cooking_value_input} qt is {result} {cooking_unit_output.lower()}.'
            print(output)
        except:
            error()
            cooking()
