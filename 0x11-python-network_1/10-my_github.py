#!/usr/bin/python3

"""
Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import sys
import requests
"""importing the required modules """

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, password))
    data = response.json()
    if 'id' in data:
        print(f"{data['id']}")
    else:
        print('None')
