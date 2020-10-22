"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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


