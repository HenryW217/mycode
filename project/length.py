#!/usr/bin/env python3
"""This is the function of length converter"""

from error import error


def length():
    # Take input of unit that "from" and "to" with the value.
    length_unit_input = input(
        'Please enter a unit from the list:\ninch\nft\nyd\nmile\nmm\nm\nkm\n--> ')
    length_value_input = input('Please enter a value\n--> ')
    length_unit_output = input(
        'Which unit to convert to?\ninch\nft\nyd\nmile\nmm\nm\nkm\n--> ')

    # Convert from inch to others.
    if length_unit_input.lower() == 'inch':
        try:
            if length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) / 12, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) / 36, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 63360, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 25.4, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) / 39.37, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) / 39370.1, 4)
            output = f'{length_value_input} inch is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from ft to others.
    elif length_unit_input.lower() == 'ft':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) * 12, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) / 3, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 5280, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 304.8, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) / 3.2808, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) / 3280.84, 4)
            output = f'{length_value_input} ft is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from yd to others.
    elif length_unit_input.lower() == 'yd':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) * 36, 4)
            elif length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) * 3, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 1760, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 914.4, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) / 1.09361, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) / 1093.61, 4)

            output = f'{length_value_input} yd is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from mile to others.
    elif length_unit_input.lower() == 'mile':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) * 63360, 4)
            elif length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) * 5280, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) * 1760, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 1609340, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) * 1609.34, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) * 1.60934, 4)
            output = f'{length_value_input} mile is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from mm to others.
    elif length_unit_input.lower() == 'mm':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) / 25.4, 4)
            elif length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) / 304.8, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) / 914.4, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 1609000, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) / 1000, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) / 1000000, 4)
            output = f'{length_value_input} mm is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from m to others.
    elif length_unit_input.lower() == 'm':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) * 39.3701, 4)
            elif length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) * 3.28084, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) * 1.09361, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 1609, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 1000, 4)
            elif length_unit_output.lower() == 'km':
                result = round(float(length_value_input) / 1000, 4)
            output = f'{length_value_input} m is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    # Convert from km to others.
    elif length_unit_input.lower() == 'km':
        try:
            if length_unit_output.lower() == 'inch':
                result = round(float(length_value_input) * 39370.1, 4)
            elif length_unit_output.lower() == 'ft':
                result = round(float(length_value_input) * 3280.84, 4)
            elif length_unit_output.lower() == 'yd':
                result = round(float(length_value_input) * 1093.61, 4)
            elif length_unit_output.lower() == 'mile':
                result = round(float(length_value_input) / 1.609, 4)
            elif length_unit_output.lower() == 'mm':
                result = round(float(length_value_input) * 1000000, 4)
            elif length_unit_output.lower() == 'm':
                result = round(float(length_value_input) * 1000, 4)
            output = f'{length_value_input} km is {result} {length_unit_output.lower()}.'
            print(output)
        except:
            error()
            length()

    else:
        error()
        length()
