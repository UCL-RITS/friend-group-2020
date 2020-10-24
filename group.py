"""An example of how to represent a group of acquaintances in Python."""
import json
import statistics

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

# Using comprehensions to calculate various parameters from the members of the group
max_age = max(person['age'] for name, person in group.items())
print(max_age)
avg_rels = statistics.mean(len(person['relations']) for name, person in group.items())
print(avg_rels)
max_age_1_rel = max(person['age'] for name, person in group.items() if len(person['relations']) > 0)
print(max_age_1_rel)
max_age_1_friend = max(person['age'] for name, person in group.items() if 'friend' in person['relations'].values())
print(max_age_1_friend)

# Writing the group dictionary into a json file
with open('group_data.json', 'w') as json_file:
    json.dump(group, json_file, indent=4)

# Reading the json file
with open('group_data.json', 'r') as json_file:
    group_data = json_file.read()

# Printing the json file data to check that is contains the correct data
print(group_data) 