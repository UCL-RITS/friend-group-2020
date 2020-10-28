"""An example of how to represent a group of acquaintances in Python."""
import json
import yaml

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

# save as a json file
with open('group.json', 'w') as f:
    json.dump(group, f)

with open('group.json', 'r') as f:
    group_json = f.read()

group_json = json.loads(group_json)
print(group_json)

# save as a yaml file

with open("group.yaml", "w") as f:
    yaml.dump(group, f)

with open("group.yaml", "r") as f:
    group_yaml = yaml.load(f)

print(yaml.safe_dump(group_yaml))