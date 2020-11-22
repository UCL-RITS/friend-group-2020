# Using the example code from the lecture

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

def mean(data):
    """Compute the mean of a non-empty list of numbers."""
    return sum(data) / len(data)


print(max(person["age"] for person in group.values()))
print(mean([len(person["relations"]) for person in group.values()]))
print(max(person["age"] for person in group.values() if person["relations"]))
print(max(person["age"] for person in group.values() if "friend" in person["relations"].values()))

import json

#write file
with open('group_file.json', 'w') as json_file:
	json.dumps(group, json_file, indent=4)

#read file
with open('group_file.json', 'r') as json_file:
	group_data = json_file.read()