#!/usr/bin/python3
"""
    A python Script that takes your GitHub credentials
    (username and password) auth = HTTPBasicAuth(username, password)
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    auth = HTTPBasicAuth(username, password)

    resp_url = requests.get("https://api.github.com/user", auth=auth)

    try:
        data = resp_url.json()
        if 'id' in data:
            print(data['id'])
        else:
            print('None')
    except ValueError:
        print('Not a valid JSON')
