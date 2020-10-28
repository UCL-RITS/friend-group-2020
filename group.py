"""An example of how to represent a group of acquaintances in Python."""

import json 
group = {
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
with open('group.json', 'w') as file:
    json.dump(group, file, indent=2)

#Read the file:
with open('group.json', 'r') as file:
    group = file.read()

print(group)

