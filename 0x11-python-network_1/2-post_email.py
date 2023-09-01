#!/usr/bin/python3

"""
Python script that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

import urllib.parse
import urllib.request
import sys
""" Importing the require modules"""


if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    email_data = {'email': email}
    data = urllib.parse.urlencode(email_data)
    data = data.encode('ascii')  # data type should be bytes
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        the_result_page = response.read()
        print(the_result_page.decode('utf-8'))
