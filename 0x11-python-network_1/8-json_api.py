#!/usr/bin/python3

"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

import sys
import requests
"""Importing the sys and requests modules"""


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    q_data = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=q_data)

    try:
        result_data = response.json()
        if result_data:
            print(f"[{result_data['id']}] {result_data['name']}")
        else:
            print('No result')
    except json.JSONDecodeError:
        print('Not a valid JSON')
