#!/usr/bin/python3
"""
    Script that lists 10 commits (from the most recent to oldest)
    of a given repository by a given owner using the GitHub API
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = ("https://api.github.com/repos/"
           f"{owner_name}/{repository_name}/commits")
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Failed to retrieve commits. Status code:\
                {response.status_code}")
