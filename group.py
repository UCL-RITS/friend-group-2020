"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
person1 = {"name" : "Person1", "age" : 20,
           "job" : "student"}
person2 = {"name" : "Person2", "age" : 20,
           "job" : "student"}

person1["classmate"] = person2

my_group = [person1, person2]

print(person1["name"])
