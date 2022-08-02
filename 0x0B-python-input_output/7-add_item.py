#!/usr/bin/python3
"""add item"""


import json

filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []
obj.extend(sys.argv[1:])
save_to_json_file(obj, filename)
