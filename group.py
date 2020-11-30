"""An example of how to represent a group of acquaintances in Python."""
import statistics 
# Your code to go here...

my_group = []

Jill = {"name": "Jill", "age": 26, "job": "biologist", "connections": {"friend": ["Zalika"], "partner": ["John"]}}
Zalika = {"name": "Zalika", "age": 28, "job": "artist", "connections": {"friend": ["Jill"]}}
John = { "name": "John", "age": 27, "job": "writer", "connections": {"partner": ["John"]}}
Nash = {"name": "Nash", "age": 34, "job": "chef", "connections": {"cousin": ["John"], "landlord": ["Zalika"]}}

my_group = [Jill, Zalika, John, Nash]

''' The maximum age of people in the group
the average (mean) number of relations among members of the group
the maximum age of people in the group that have at least one relation
[more advanced] the maximum age of people in the group that have at least one friend '''


# Maximum age of people in the group
age_list = []

for person in my_group:
    age = person['age']
    age_list.append(age)

print('1- Maximum age of people in group is: ', end="")
print(max(age_list))

# Average number of relations among members of the group
nb_connections_list = []

for person in my_group:
    nb_connections = len(person["connections"])
    nb_connections_list.append(nb_connections)

print('2- Average number of relations is: ', end="")
print(statistics.mean(nb_connections_list))


# Maximum age of people in the group that have at least one relation

new_group = []
age_list2 = []

for person in my_group:
    nb_connections = len(person["connections"])

    if int(nb_connections) > 0:
        index = my_group.index(person)
        new_group.append(my_group[index])

for person2 in new_group:
    age = person2['age']
    age_list2.append(age)

print('3- Maximum age of people with at least 1 relation is: ', end="")
print(max(age_list2))
    

# Maximum age of people in the group that have at least one friend 
    
new_group2 = []
age_list3 = []

for person in my_group:
    if 'friend' in person["connections"]:
        nb_friends = len(person["connections"]["friend"])
        index = my_group.index(person)
        new_group2.append(my_group[index])

for person in new_group2:
    age = person['age']
    age_list3.append(age)


print('Maximum age of people with at least 1 friend is: ', end="")
print(max(age_list3))


