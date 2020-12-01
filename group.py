"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import json

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
'relations': {'Zalika': 'landlord', 'John': 'cousin'}},

"Richard" :

{'job': 'writer' ,
'age': '53', 
'relations': {}}


}


#some examples of how to retreive info from dict
print(f"Zalika's age is: {my_group['Zalika']['age']}")
print(f"Nash's job is: {my_group['Nash']['job']}")
print(f"Relationship between Jill and John is: {my_group['Jill']['relations']['John']}")

#return max age of group
ages = [my_group[i]['age'] for i in my_group.keys()]
print(f"The maximum age of this group of people is: {max(ages)}") 

#return mean number of relations in group
rels = [len(my_group[i]['relations']) for i in my_group.keys()]
print(f"The mean number of relations in this group of people is: {sum(rels)/len(rels)}")

#return max age of group that have at least one relation
ages_rels = [my_group[i]['age'] for i in my_group.keys() if len(my_group[i]['relations']) >= 1]
print(f"The maximum age of people in this group that have at lease one relation is: {max(ages_rels)}") 

#return max age of group that have at least one friend
ages_friends = [my_group[i]['age'] for i in my_group.keys() if 'friend' in my_group[i]['relations'].values()]
print(f"The maximum age of people in this group that have at lease one friend is: {max(ages_friends)}")



#JSON

#write
with open('groupdata.json' ,'w') as jsonfile:
    json.dump(my_group, jsonfile, indent=3)

#load
with open('groupdata.json' ,'r') as loadedjsonfile:
    json.load(loadedjsonfile)
print(loadedjsonfile)



