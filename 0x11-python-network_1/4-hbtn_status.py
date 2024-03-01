#!/usr/bin/python3
"""urllib request"""
import requests


if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    cont = r.text
    print("Body response:")
    print("\t- type: {}".format(type(cont)))
    print("\t- content: {}".format(cont))
