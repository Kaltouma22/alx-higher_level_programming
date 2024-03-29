#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
import urllib.error


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body.decode('utf-8')))
    except urllib.error.URLError as e:
        print("Error:", e.reason)
