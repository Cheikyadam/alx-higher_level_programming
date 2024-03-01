#!/usr/bin/python3
"""urllib request error code"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
        print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
