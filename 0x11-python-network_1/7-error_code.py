#!/usr/bin/python3

"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
"""

import requests
import sys
""" Importing the sys and requests modules"""

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
