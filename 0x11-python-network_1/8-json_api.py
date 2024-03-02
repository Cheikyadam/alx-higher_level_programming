#!/usr/bin/python3
"""API"""
import sys
import requests


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) >= 2:
        q = sys.argv[1]
    else:
        q = ""
    parameters = {'q': q}
    # url = f"{url}?q={q}"
    r = requests.post(url, data=parameters)
    try:
        r_json = r.json()
        if len(r_json) == 0:
            print("No result")
        elif "id" in r_json and "name" in r_json:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except Exception as e:
        print("Not a valid JSON")
