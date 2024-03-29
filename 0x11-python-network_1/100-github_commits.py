#!/usr/bin/python3
"""
    Script that takes 2 arguments: repository name and owner name
    Uses the GitHub API to retrieve information about the repository
"""
import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}"
    response = requests.get(url)

    if response.status_code == 200:
        repo_info = response.json()
        print(f"Repository name: {repo_info['name']}")
        print(f"Owner: {repo_info['owner']['login']}")
        print(f"Description: {repo_info['description']}")
        print(f"Stars: {repo_info['stargazers_count']}")
        print(f"Forks: {repo_info['forks_count']}")
        print(f"URL: {repo_info['html_url']}")
    else:
        print(f"Failed to retrieve repository information.\
                Status code: {response.status_code}")
