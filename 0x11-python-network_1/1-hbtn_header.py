#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            print(x_request_id)
    except urllib.error.URLError as e:
        print("Error:", e.reason)
