#!/usr/bin/python3
"""
    Script that takes your GitHub credentials (username and password)
    Uses the GitHub API to display your id
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py USERNAME PASSWORD")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    auth = (username, password)
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        user_id = response.json().get('id')
        if user_id:
            print(f"Your GitHub user ID is: {user_id}")
        else:
            print("User ID not found in the response.")
    else:
        print(f"Failed to retrieve user ID.Status code:\
        {response.status_code}")
