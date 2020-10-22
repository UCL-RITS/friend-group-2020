"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = { "Jill" : { "Age": 26, "Job": ["Biologist"], "Connections": [{"Zalika" : "Friend", "John": "Partner"}] 

},

"Zalika" : { "Age": 28, "Job": ["Artist"], "Connections": [{"Jill" : "Friend", "Nash": "Tenant"}]
},

"John" : { "Age": 27, "Job": ["Writer"], "Connections": [{"Jill" : "Partner", "Nash": "Cousin"}]
},

"Nash" : { "Age": 34, "Job": ["Chef"], "Connections": [{"John" : "Cousin", "Zalika": "Landlord"}]
}

}

# Part 1

age_list = {friend: person["Age"] for friend, person in my_group.items()} # age of each person in the group
print("Group member and respective age:", age_list)
print("The maximum age in the group is:", max(age_list.values())) #Retrieve the maximum age

# Part 2

no_relations = {friend: len(my_group[friend]["Connections"][0]) for friend, person in my_group.items()} #dictionary of the number of relations for each person in the group
print("Group members and their number of relations:", no_relations)
print("The average (mean) number of relations among members of the group: is", sum([x for x in no_relations.values()])/len(no_relations))

# Part 3

age_list2 = {friend: person["Age"] for friend, person in my_group.items() if len(my_group[friend]["Connections"][0])>=1} #list of people with at least 1 relation
print("Group members with at least one relation, and their respective ages", age_list2)
print("The maximum age (for people with at least one relation) is:", max(age_list2.values())) #Retrieve the maximum age

# Part 4

age_list3 = {friend: person["Age"] for friend, person in my_group.items() if "Friend" in my_group[friend]["Connections"][0].values()} #dictionary of people with at least one friend
print("Group members with at least one friend, and their respecive ages", age_list3)
print("The maximum age (for people with at least one friend) is:", max(age_list3.values())) #Retrieve the maximum age
