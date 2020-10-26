"""An example of how to represent a group of acquaintances in Python.

# Your code to go here...
class Person:
    def __init__(self, name, age, job, connection=[ ] ):
        self.name = name
        self.age = age
        self.job =job
        self.connection = connection

    def add_connection(self, friend, relationship):
        name=friend.name
        self.connection.append({name,relationship})
        print(friend)
        print(self.connection)

jill=Person('Jill', 26, 'biologist')
zalika = Person('Zalika', 28, 'artist')
john=Person('John', 27, 'writer')
nash=Person('Nash', 34, 'chef')

jill.add_connection(zalika, 'friend')
jill.add_connection(john, 'partner')
zalika.add_connection(jill, 'friend')
john.add_connection(jill, 'partner')
nash.add_connection(john, 'cousin')
nash.add_connection(zalika, 'landlord')

print(zalika.connection)
print(jill.connection)
print(john.connection)
print(nash.connection)
#zalika.add_connection(jill, 'friend')

def connection(person1, person2, relationship):
    if relationship == 'friend' or relationship == 'partner':
        person1.connection[person2.name]=relationship
        person2.connection[person1.name]=relationship
    else:
        person1.connection[person2]=relationship
 """

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

import json


def save_file(group):
    with open('group.json', 'w') as json_group_out:
        json_group_out.write(json.dumps(group))


# max age of people in the group
def age_list(group):
    ages = []
    for person in group.keys():
        age = group[person]['age']
        ages.append(age)
    return ages


def max_age(group):
    ages = age_list(group)
    max_age = max(ages)
    return max_age


def relations_list(group):
    relations_list = []
    for person in group.keys():
        relations = group[person]['relations']
        relations_list.append(relations)
    return relations_list


def number_of_relations(group):
    relations_number = []
    relations = relations_list(group)
    for relation in relations:
        relations_number.append(len(relation))
    return relations_number


def relations_mean(group):
    relations_number = number_of_relations(group)
    mean_relations = sum(relations_number) / len(relations_number)
    return mean_relations


def max_age_above1_relation(group):
    relations_number = number_of_relations(group)
    at_least_1_relation = []
    ages = age_list(group)
    x = 0
    for relations in relations_number:
        if relations > 1:
            person_age = ages[x]
            at_least_1_relation.append(person_age)
        max_age_relationship = max(at_least_1_relation)
        x = x + 1
    return max_age_relationship


def age_friend(group):
    relations = relations_list(group)
    at_least_1_friend = []
    ages = age_list(group)
    x = 0
    for relations in relations:
        for relation in relations:
            if relations[relation] == 'friend':
                person_age = ages[x]
                at_least_1_friend.append(person_age)
        max_age_relationship = max(at_least_1_friend)
        x = x + 1
    return max_age_relationship


def main(group):
    save_file(group)
    maximum_age = max_age(group)
    mean_relations = relations_mean(group)
    max_age_more_1 = max_age_above1_relation(group)
    max_age_friend = age_friend(group)

    print(f"STATISTICS: ")
    print(f"The maximum age of this group is: {maximum_age}")
    print(
        f"The average number of relations among members of the group is: {mean_relations},"
    )
    print(
        f"The maximum age of people in the group that have at least one relation is: {max_age_more_1},"
    )
    print(
        f"The maximum age of people in the group that have at least one friend is: {max_age_friend}"
    )


if __name__ == "__main__":
    main(group)