#!/usr/bin/python3
"""
script that adds all arguments
to a Python list, and
then save them to a file
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    obj = load_from_json_file("add_item.json")
except:
    obj = []
for i in sys.argv[1:]:
    obj.append(i)
save_to_json_file(obj, "add_item.json")
