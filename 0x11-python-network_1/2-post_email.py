#!/usr/bin/python3
"""
that takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
"""

import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('utf-8')

    try:
        with urllib.request.urlopen(url, data) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error:", e.reason)
