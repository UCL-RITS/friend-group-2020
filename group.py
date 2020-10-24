"""An example of how to represent a group of acquaintances in Python."""

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


def oldest_person(group):
    return max([person['age'] for person in group.values()])


def mean_relations_count(group):
    relations = [len(person['relations']) for person in group.values()]
    return sum(relations)/len(relations)


def oldest_person_with_relations(group):
    relations = {key: value for (key, value) in group.items()
                 if len(value['relations'])}
    return oldest_person(relations)


def oldest_person_with_friends(group):
    relations = {key: value for (key, value) in group.items()
                 if "friend" in value['relations'].values()}
    return oldest_person(relations)

# [more advanced] the maximum age of people in the group that have at least one friend


print(f"the oldest person is {oldest_person(my_group)} years old")
print(
    f"the average numper of relations among the group is {mean_relations_count(my_group)}")
print(
    f"the oldest person with relations is {oldest_person_with_relations(my_group)} years old")
print(
    f"the oldest person with friends is {oldest_person_with_friends(my_group)} years old")