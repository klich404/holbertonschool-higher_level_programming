#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    html = requests.get(url)
    if html.status_code >= 400:
        print("Error code: {}".format(html.status_code))
    else:
        print(html.text)
