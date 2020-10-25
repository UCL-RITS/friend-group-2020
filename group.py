"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import statistics

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

#finding maximum age
max_age = max(person['age'] for person in my_group.values())
print(max_age)

#finding person w age 28 (my own exercise)
for person in my_group:
    if my_group[person]["age"] == 28:
        print(person)

#finding mean number of relations 
num_of_relations = statistics.mean(len(person['relations']) for name, person in my_group.items())
print(num_of_relations)

#max age with at least one relation
max_age_one_relation = max(person['age'] for person in my_group.values() if len(person['relations']) > 0)
print(max_age_one_relation)

#max age with at least one friend
max_age_one_friend = max(person['age'] for person in my_group.values() if "friend" in person["relations"].values())
print(max_age_one_friend)