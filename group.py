"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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
#print(group["John"]["relations"])


# maximum age
print(max([group[key]['age'] for key in group]))

# average number of relations
print(sum([len(group[key]['relations']) for key in group])/ len(group))

# maximum age of people that have at least one relation
print(max([group[key]['age'] for key in group if group[key]['relations']]))

# maximum age of people that have at least one friend
print(max([group[key]['age'] for key in group if group[key]['relations'] if 'friend' in group[key]['relations'].values()]))