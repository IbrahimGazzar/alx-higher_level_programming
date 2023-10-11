#!/usr/bin/python3
"""
    This module adds all given arguments to a list
    Then saves the list as a json object
"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    ls = load_from_json_file("add_item.json")
except Exception:
    ls = []
for i, item in enumerate(sys.argv):
    if i != 0:
        ls.append(item)
with open("add_item.json", "w", encoding="utf-8"):
    save_to_json_file(ls, "add_item.json")
