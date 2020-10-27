"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group =
"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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

print("max age:" + str(max([value['age'] for value in my_group.values()])))

a = [len(value['relations']) for value in my_group.values()] 

print("Average no of relations: " + str(sum(a)/len(a)))

b = [value['age'] for value in my_group.values() if len(value['relations']) >= 1] 

print("Max age of people with >= 1 relation: " + str(max(b)))