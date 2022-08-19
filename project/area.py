#!/usr/bin/env python3
"""This is the function of area converter"""

from error import error


def area():
    # Unit "from", "to" and "value".
    unit_input = input(
        'Please enter a unit from the list:\nft\nyd\nmile\nm\nkm\n--> ')
    value_input = input('Please enter a value\n--> ')
    unit_output = input(
        'Which unit to convert to?\nft\nyd\nmile\nm\nkm\n--> ')
    # Convert from sq ft to others.
    if unit_input.lower() == 'ft':
        try:
            if unit_output.lower() == 'yd':
                result = round(float(value_input) / 9, 4)
            elif unit_output.lower() == 'mile':
                result = round(float(value_input) / 27880000, 4)
            elif unit_output.lower() == 'm':
                result = round(float(value_input) / 10.764, 4)
            elif unit_output.lower() == 'km':
                result = round(float(value_input) / 10760000, 4)
            output = f'{value_input} square ft is {result} square {unit_output.lower()}.'
            print(output)
        except:
            error()
            area()

    # Convert from sq yd to others.
    elif unit_input.lower() == 'yd':
        try:
            if unit_output.lower() == 'ft':
                result = round(float(value_input) * 9, 4)
            elif unit_output.lower() == 'mile':
                result = round(float(value_input) / 3098000, 4)
            elif unit_output.lower() == 'm':
                result = round(float(value_input) / 1.196, 4)
            elif unit_output.lower() == 'km':
                result = round(float(value_input) / 1196000, 4)
            output = f'{value_input} square yd is {result} square {unit_output.lower()}.'
            print(output)
        except:
            error()
            area()

    # Convert from sq mile to others.
    elif unit_input.lower() == 'mile':
        try:
            if unit_output.lower() == 'ft':
                result = round(float(value_input) * 27880000, 4)
            elif unit_output.lower() == 'yd':
                result = round(float(value_input) * 3098000, 4)
            elif unit_output.lower() == 'm':
                result = round(float(value_input) * 2590000, 4)
            elif unit_output.lower() == 'km':
                result = round(float(value_input) * 2.58999, 4)
            output = f'{value_input} square mile is {result} square {unit_output.lower()}.'
            print(output)
        except:
            error()
            area()

    # Convert from sq m to others.
    elif unit_input.lower() == 'm':
        try:
            if unit_output.lower() == 'ft':
                result = round(float(value_input) * 10.7639, 4)
            elif unit_output.lower() == 'yd':
                result = round(float(value_input) * 1.19599, 4)
            elif unit_output.lower() == 'mile':
                result = round(float(value_input) / 2590000, 4)
            elif unit_output.lower() == 'km':
                result = round(float(value_input) / 1000000, 4)
            output = f'{value_input} square m is {result} square {unit_output.lower()}.'
            print(output)
        except:
            error()
            area()

    # Convert from sq km to others.
    elif unit_input.lower() == 'km':
        try:
            if unit_output.lower() == 'ft':
                result = round(float(value_input) * 1550000000, 4)
            elif unit_output.lower() == 'yd':
                result = round(float(value_input) * 1196000, 4)
            elif unit_output.lower() == 'm':
                result = round(float(value_input) * 1000000, 4)
            elif unit_output.lower() == 'mile':
                result = round(float(value_input) / 2.59, 4)
            output = f'{value_input} square km is {result} square {unit_output.lower()}.'
            print(output)
        except:
            error()
            area()
