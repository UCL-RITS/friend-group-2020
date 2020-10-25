"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = { "Jill" : {"age" : 26, "job" : "biologist", "connection" : ["Zalika", "John"]}, 
           
            "Zaklika" : {"age" : 28, "job" : "artist", "connection" : ["Jill"]},
           
            "John" : {"age" : 27, "job" : "writer", "connection" : ["Jill"]},
           
           "Nash" : {"age" : 34, "job" : "chef", "connection" : ["Zalika", "John"]}}

class Person:
    """
    Person object to hold the information on one person
    """
    def __init__(self, name, age, job=None):
        """
        -------inputs-------
        name - str
        age - int
        job - str
        """
        self.name = name
        self.age = age
        self.job = job
        self.relations = {}

    def add_relations(self, *args):
        """
        Adds relations to other persons
        -------inputs-------
        *args - tuples (Person object, str) representing the related person and the relationship type
        """
        for pair in args:
            self.relations[pair[0]] = pair[1]

    def print_rels(self):
        """
        Prints this persons relations in format: name (age, job) -- relationship
        """
        for key in self.relations.keys():
            print(key.name + ' (' + str(key.age) + ', ' + key.job + ') -- ' + self.relations[key])


Jill = Person('Jill', 26, 'biologist')
Zalika = Person('Zalika', 28, 'artist')
John = Person('John', 27, 'writer')
Nash = Person('Nash', 34, 'chef')

Jill.add_relations((Zalika, 'friend'), (John, 'partner'))
Zalika.add_relations((Jill, 'friend'))
John.add_relations((Jill, 'partner'))
Nash.add_relations((John, 'cousin'), (Zalika, 'landlord'))

my_group = [Jill, Zalika, John, Nash]

import numpy as np

# Maximum age
max_age = max([ person.age for person in my_group ])
print('Maximum age = ' + str(max_age))

# Average number of relations
mean_rels = np.mean([ len(person.relations.keys()) for person in my_group ])
print('Mean number of relations = ' + str(mean_rels))

# Maximum age for ppl with at least one relation
max_age_min1rel = max([ person.age for person in my_group if len(person.relations.keys()) >= 1 ])
print('Maximum age of people with at least one relation = ' + str(max_age_min1rel))

# Maximum age for ppl with at least one friend
max_age_min1friend = max([ person.age for person in my_group if 'friend' in person.relations.values() ])
print('Maximim age of people with at least one friend = ' + str(max_age_min1friend))
