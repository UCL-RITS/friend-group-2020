"""An example of how to represent a group of acquaintances in Python."""

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

# maximum age
print("The maximum age of the people in the group is:", max({name['age']for group, name in group.items()}))

# average (mean) number of relations among members of the group
relations_person = {len(name['relations']) for group, name in group.items()}
mean = sum(relations_person)/len(relations_person)
print("The average (mean) number of relations among members of the group:", mean)

# the maximum age of people in the group that have at least one relation
print("The maximum age of people in the group that have at least one relation is",
        max({name['age'] for group, name in group.items() if len(name['relations']) > 0 }))

# the maximum age of people in the group that have at least one friend (indent for readability)
print ("The maximum age of people in the group that have at least one friend is",
        max({name['age'] for group, name in group.items() for relation_name, relation_relation in name['relations'].items() 
        if 'friend' is (relation_relation)}))