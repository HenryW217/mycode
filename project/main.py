#!/usr/bin/env python3

"""This program has few unit converter for daily use"""

# This is the main function that give user options to select what converter they want to use.

# Import function from other files.
from length import length
from area import area
from weight import weight
from temperature import temperature
from cooking import cooking
from currency import currency
from fun import fun

# Main menu


def main():
    print("\nWelcome to unit converter, please select by enter the number")
    m_input = input(
        '1. Length \n2. Area \n3. Weight \n4. Temperature \n5. Volume\n6. Currency\n7. Fun stuff\n--> ')
    if m_input == '1':
        print('--Length Converter--')
        length()
    elif m_input == '2':
        print('--Area Converter--')
        area()
    elif m_input == '3':
        print('--Weight Converter--')
        weight()
    elif m_input == '4':
        print('--Temperature Converter--')
        temperature()
    elif m_input == '5':
        print('--Cooking Volume--')
        cooking()
    elif m_input == '6':
        print('--Currency--')
        currency()
    elif m_input == '7':
        print('--Car Troubleshooting Flowchart--')
        fun()
    else:
        print('Please select a number')
        main()
    again = input('\nEnter Y to main menu, anykey to exit\n -->').lower()
    if again == 'y':
        main()
    elif again == 'anykey':
        print('Eric, did you find the "anykey"?\n')
        exit()
    else:
        exit()


main()
