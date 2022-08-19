#!/usr/bin/env python3

"""This is the function getting info from currrency API"""

import json
import requests
from error import error


def currency():
    # API info
    url = "https://currencyscoop.p.rapidapi.com/latest"
    headers = {
        "X-RapidAPI-Key": "d035fa45aemsh430d48a1e3f67dap1ecfcbjsna38aa140363a",
        "X-RapidAPI-Host": "currencyscoop.p.rapidapi.com"
    }
    # Getting data from API
    response = requests.request("GET", url, headers=headers)
    # Convert data to JSON format
    data = json.loads(response.text)
    updated_on = data["response"]["date"]

    # Ask user for amount to convert and use try/except to ensure user enter a number
    try:
        value_input = float(
            input('Please enter how much U.S. dollar you want to convert:\n--> $ '))
    except:
        error()
        currency()

    # Have user choose a currency to convert to.
    unit_input = input('Please choose a currency:\ni.e. EUR, GBP, CAD...\n--> ').upper()

    try:
        # Get the currency rate.
        foreign_rate = data["response"]["rates"][f"{unit_input}"]
        # Calculate out put based on user input
        value_output = round(float(value_input) * foreign_rate, 2)

    except:
        error()
        currency()
    # Print the result
    output = f'${value_input} equals {value_output} {unit_input}'
    print(output)
    print(f'Rate updates on {updated_on}\n')
