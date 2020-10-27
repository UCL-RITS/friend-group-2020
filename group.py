from enum import Enum
import numpy as np

"""An example of how to represent a group of acquaintances in Python."""

# Make a enum storing possible relation types and an ID for that relationship type
class Relation(str, Enum):
     PARTNER = "Partner"
     FRIEND = "Friend"
     LANDLORD = "Landlord"
     COUSIN = "Cousin"

# Store data as a dict of dict's, where the key is the ID of the user which is used in relations
my_group = {
                1: {
                    'name': 'Jill',
                    'job': 'Biologist',
                    'age': 26,
                    'relations': [
                        {'to': 2, 'type': Relation.FRIEND},
                        {'to': 3, 'type': Relation.PARTNER}
                    ]
                },
                2: {
                    'name': 'Zalika',
                    'job': 'Artist',
                    'age': 28,
                    'relations': [
                        {'to': 1, 'type': Relation.FRIEND}
                    ]
                },
                3: {
                    'name':'John',
                    'job': 'Writer',
                    'age': 27,
                    'relations': [
                        {'to': 1, 'type': Relation.PARTNER}
                    ]},
                4: {
                    'name': 'Nash',
                    'job': 'Chef',
                    'age': 34,
                    'relations': [
                        {'to': 3, 'type': Relation.COUSIN},
                        {'to': 2, 'type': Relation.LANDLORD}
                    ]
                },
        }

# Firstly begin by looking at all the users and their ages, to get the average and maximum age globally

# Loop through and make a list of the ages
ages = [friend['age'] for friend in my_group.values()]
# Print maximum and average
print("Maximum age in group: ", np.max(ages))
print("Average age in group: ", np.average(ages))

# Now find the maximum age of people in the group that have at least one relation
ages = [friend['age'] for friend in my_group.values() if len(friend['relations']) >= 1]
# Print maximum and average
print("Maximum age of people in group with at least one relation: ", np.max(ages))

# Now find the maximum age of people in the group that have at least one friend

# Firstly, using a simple for loop
ages = []
for friend in my_group.values():
    num_friends = 0
    for relation in friend['relations']:
        if relation['type'] == Relation.FRIEND:
            num_friends = num_friends + 1
    if num_friends >= 1:
        ages.append(friend['age'])
print("Maximum age people in the group that have at least one friend (for loop): ", np.max(ages))

# Then an alternative where it's written as one line using list comprehension expressions
ages = [friend['age'] for friend in my_group.values() if [relation['type'] for relation in friend['relations']].count(Relation.FRIEND) >= 1]
# Print maximum and average
print("Maximum age people in the group that have at least one friend (list comprehension): ", np.max(ages))

# Save the friend data to a JSON file
import json

# Make the JSON file and write data
with open('friend_group.json', 'w') as file:
    json.dump(my_group, file, indent=4)

# Read JSON file into a string
with open('friend_group.json', 'r') as file:
    loaded_group = file.read()

# Parse the JSON string
loaded_friend_group = json.loads(loaded_group)

# Now convert the string relation types back into relation enum members
for friend in loaded_friend_group.values():
    for relation in friend['relations']:
        relation['type'] = Relation(relation['type'])

# Also, json.loads converts our integer IDs for each user into strings
# So let's convert them back into integers
for friend in list(loaded_friend_group):
    loaded_friend_group[int(friend)] = loaded_friend_group.pop(friend)

print("Did loaded friend group equal original group? ", my_group == loaded_friend_group)
