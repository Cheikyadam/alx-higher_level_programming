#!/usr/bin/python3
"""Github API"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[2]
    username = sys.argv[1]
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    try:
        r = requests.get(url)
        res = r.json()
        for i in range(10):
            print(
                    "{}: {}".
                    format(res[i]['sha'], res[i]['commit']['author']['name']))
    except Exception as e:
        print(None)
