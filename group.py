"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
my_group = {
    'Jill' : {
         'age': 26,
         'job': 'biologist',
         'connection': {
             'Zalika':'friend',
             'John':'partner'
         }},
     'Zalika' : {
         'age': 28,
         'job': 'artist',
         'connection': {
             'Jill':'friend'
         }},
    'John' : {
         'age': 27,
         'job': 'writer',
         'connection': {
             'Jill':'partner'
         }},     
    'Nash' : {
         'age': 34,
         'job': 'chef',
         'connection': {
             'John':'cousin',
             'Zalika':'landlord'
         }}   
}

print(my_group.items())

#Question 1#
age_1 = {friend: person["age"] for friend, person in my_group.items()} 
print("The maximum age in the group is:", max(age_1.values())) 

#Question 2#
no_relations = {friend: len(my_group[friend]['connection']) for friend, person in my_group.items()} 
print("The average (mean) number of relations among members of the group: is", sum([x for x in no_relations.values()])/len(no_relations))

#Question 3#
age_2 = {friend: person["age"] for friend, person in my_group.items() if len(my_group[friend]['connection'])>=1} 
print("The maximum age of people in the group that have at least one relation is:", max(age_2.values())) 

#Question 4#
age_3 = {friend: person["age"] for friend, person in my_group.items() if "Friend" in my_group[friend]['connection'][0].values()}
print("The maximum age of people in the group that have at least one friend is:", max(age_3.values()))