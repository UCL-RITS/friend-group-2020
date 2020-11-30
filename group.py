"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    
"Jill" : 

{'job': 'Biologist' ,
'age': '26', 
'relations': {'Zalika': 'friend', 'John': 'Partner'}},

"Zalika" : 

{'job': 'artist' ,
'age': '28', 
'relations': {'Jill': 'friend'}},

"John" : 

{'job': 'writer' ,
'age': '27', 
'relations': {'Jill': 'Partner'}},

"Nash" : 

{'job': 'chef' ,
'age': '34', 
'relations': {'Zalika': 'landlord', 'John': 'cousin'}}


}

print(f"Zalika's age is: {my_group['Zalika']['age']}")
print(f"Nash's job is: {my_group['Nash']['job']}")
print(f"Relationship between Jill and John is: {my_group['Jill']['relations']['John']}")
