#!/usr/bin/python3
add_item = __import__('7-add_item').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
add_item(my_list, filename)

filename = "my_dict.json"
my_dict = {
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
add_item(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    add_item(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
