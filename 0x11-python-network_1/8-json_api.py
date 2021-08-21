#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    d = {'q': ""}
    if len(argv) > 1:
        d['q'] = argv[1]
    html = requests.post('http://0.0.0.0:5000/search_user', data=d)
    try:
        json_html = html.json()
        if len(json_html) > 0:
            print("[{}] {}".format(html.text['id'], html.text['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
