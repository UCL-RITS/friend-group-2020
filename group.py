"""An example of how to represent a group of acquaintances in Python."""

# ATTEMPT 1:  USING CLASSES BUT IT GOT TOO COMPLICATED WITH SELF 
""" 
#Clearing out variables 
jill = []
zalika = []

# Your code to go here...
class Person:
    def __init__(self, name, age, job, connection= [] ):
        self.name = name
        self.age = age
        self.job =job
        self.connection = connection

    def add_connection(self, friend, relationship):
        #Problem: This also updates the connection of the friend using self of person and person's friend 
        #self.connection.update({friend.name: relationship})
        self.connection.append({friend.name : relationship})


jill=Person('Jill', 26, 'biologist')
zalika = Person('Zalika', 28, 'artist')
john=Person('John', 27, 'writer')
#nash=Person('Nash', 34, 'chef')

jill.add_connection(zalika, 'friend')
jill.add_connection(john, 'partner')
print("Jill's connection: ", jill.connection)
zalika.add_connection(jill, 'friend')
print("Zalika's connection: ", zalika.connection)
"""

# ATTEMPT 2: Using dictionary of dictionaries 

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

#Unpacking things in nested dictionary of dictionaries : member name is string, member is actual dictionary value with its items
[print(member['age']) for member_name, member in group.items()]

# 1. Max age of people in the group 
ages = []
[ages.append(member['age']) for member_name, member in group.items()]
print("Maximum age of group: ", max(ages))

# 2. Average (mean) number of relations among members of the group 
no_relations = []
[no_relations.append(len(member['relations'])) for member_name, member in group.items()]
avg_relations = sum(no_relations) / len(no_relations)
print("Average number of relations: " , avg_relations)

# 3. The maximum age of people in the group that have at least one relation 
ages_1relation = []
[ages_1relation.append(member['age']) for member_name, member in group.items() if len(member['relations']) > 0 ]
print("Max age of people in the group that have at least one relation: ", max(ages_1relation))

#4. Maximum age of people in the group that have at least one friend 
print('friend' in group['Jill']['relations'].values()) #Test if friend is in relations.values
ages_wfriends = [] 
[ages_wfriends.append(member['age']) for member_name, member in group.items() if ('friend' in member['relations'].values())]
print('Maximum age of people w/at least one friend: ', max(ages_wfriends))

