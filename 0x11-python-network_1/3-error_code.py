#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8)
"""
from urllib import request
from sys import argv
import urllib


if __name__ == "__main__":

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.__dict__.get("code")))
