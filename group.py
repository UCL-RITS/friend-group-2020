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
print("The maximum age of the people in the group is:", max({room['age']for name, room in group.items

# average (mean) number of relations among members of the group
relations_person = {len(room['relations']) for name, room in group.items()}
mean = sum(relations_person)/len(relations_person)
print("The average (mean) number of relations among members of the group:", mean)






