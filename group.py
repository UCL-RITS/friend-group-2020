"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import numpy as np

class Person:

    def __init__(self, name, age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.relationships = {}

    def add_relationship(self, connectedname, relationship):
        self.relationships[connectedname]= relationship 
        
        
    
Jill = Person("Jill", 26, "biologist")
Zalika = Person("Zalika" ,28, "artist")
John = Person("John", 27, "writer")
Nash = Person("Nash",34, "chef")

Jill.add_relationship("Zalika", "friend")
Jill.add_relationship("John", "partner")
Zalika.add_relationship("Jill", "friend")
John.add_relationship("Jill", "partner")
Nash.add_relationship("John","cousin")
Nash.add_relationship("Zalika","landlord")


people = [Jill, Zalika, John, Nash]

#printing the maximum age of a person in the group using comprehension
print(np.max([person.age for person in people]))

#prining the average(mean) number of relations of the group using comprehension
print(np.mean([len(person.relationships) for person in people]))

#printing the maximum age of the person in the group which has atleast one relation 
print(np.max([person.age for person in people if len(person.relationships) >= 1]))


#printing the maximum age of the person in the group which has atleast one friend 
print(np.max([person.age for person in people for rel in person.relationships.values() if rel== 'friend']))

