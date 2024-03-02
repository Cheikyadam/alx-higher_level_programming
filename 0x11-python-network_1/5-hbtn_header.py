#!/usr/bin/python3
"""requests headers"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    if "X-Request-Id" in r.headers:
        print(r.headers['X-Request-Id'])
