#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)
"""
from urllib import request
from sys import argv
import urllib


if __name__ == "__main__":

    url = argv[1]
    data = urllib.parse.urlencode({"email": argv[2]})
    data = data.encode("utf-8")

    with request.urlopen(url, data) as response:
        html = response.read()
        html = html.decode("utf-8")
    print(html)
