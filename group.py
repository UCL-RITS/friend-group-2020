"""An example of how to represent a group of acquaintances in Python."""

""" 
# ATTEMPT 1:  USING CLASSES BUT IT GOT TOO COMPLICATED WITH SELF 
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

# Attempt 2: Using dictionary of dictionaries 

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

