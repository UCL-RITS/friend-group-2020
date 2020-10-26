"""An example of how to represent a group of acquaintances in Python."""

import statistics
import json

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}


with open ('my_group.json','w') as json_file: 
    json.dump(my_group,json_file, indent=4)

with open ('my_group.json','r') as json_file:
    my_group_as_string = json_file.read()

my_group_json = json.loads(my_group_as_string)