#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    with requests.get('https://intranet.hbtn.io/status') as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
