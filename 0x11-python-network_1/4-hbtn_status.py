#!/usr/bin/python3
"""A Python script that fetches https://alx-intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":
    url = requests.get('https://alx-intranet.hbtn.io/status')
    body = url.text

    print("Body response:")
    print(f'\t- type: {type(body)}')
    print(f'\t- content: {body}')
