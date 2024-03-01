#!/usr/bin/python3
"""urllib request"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        body = response.headers
    print(body['X-Request-Id'])
