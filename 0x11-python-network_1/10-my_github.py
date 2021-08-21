#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import requests
from sys import argv
import requests.auth


if __name__ == "__main__":
    id = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        json_id = id.json()
        print(json_id['id'])
    except:
        print("None")
