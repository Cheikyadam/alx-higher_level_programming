#!/usr/bin/python3
"""Github API"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    username = sys.argv[2]
    url = f"https://api.github.com/repos/{username}/{repo}/commits"
    try:
        r = requests.get(url)
        res = r.json()
        for i in range(10):
            try:
                print(
                        "{}: {}".
                        format(
                            res[i]['sha'], res[i]['commit']['author']['name']))
            except IndexError:
                break
    except Exception as e:
        pass
