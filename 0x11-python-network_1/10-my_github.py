#!/usr/bin/python3
"""Github API"""
import sys
import requests


if __name__ == '__main__':
    token = sys.argv[2]
    username = sys.argv[1]
    url = f"https://api.github.com/users/{username}"
    headers = {'Authorization': f"Bearer{token}"}
    try:
        r = requests.get(url, headers=headers)
        res = r.json()
        print(res['id'])
    except Exception as e:
        pass
