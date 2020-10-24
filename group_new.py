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


# create file and write
with open('group_file.json', 'w') as f:
    json.dump(group, f, indent=4)

# read file and load
with open('group_file.json', 'r') as json_file:
    my_group = json_file.read()

mydata = json.loads(my_group)

print(mydata)


