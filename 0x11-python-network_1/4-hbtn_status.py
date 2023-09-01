#!/usr/bin/python3

""" Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    result = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print('\t'"-type:", type(result.text))
    print('\t'"-content:", result.text)
