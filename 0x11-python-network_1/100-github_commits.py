#!/usr/bin/python3

"""
Please list 10 commits (from the most recent to
oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, here is the
documentation https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
Python script that takes 2 arguments in order to solve this challenge.
"""

import sys
import requests
""" Importing the required modules"""


def github_commits(repository, owner):
    """Method to help get the 10 commits from Github"""

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    response = requests.get(url)
    github_commits = response.json()

    for commit in github_commits[:10]:
        sha = commit['sha']
        name_author = commit["commit"]["author"]["name"]
        print(f'{sha}: {name_author}')


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    github_commits(repository_name, owner_name)
