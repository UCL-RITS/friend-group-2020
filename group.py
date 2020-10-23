from enum import Enum

"""An example of how to represent a group of acquaintances in Python."""

# Make a enum storing possible relation types and an ID for that relationship type
class Relation(Enum):
     PARTNER = 1
     FRIEND = 2
     LANDLORD = 3
     COUSIN = 4


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


# Block of code that extracts the maximum age in the group
group_ages = [value['age'] for value in my_group.values()]
print("the maximum age of people in the group is:", max(group_ages))

# Block of code that calculates the average of connections
# Follow quite similar approach as before with the difference that now we need the average
group_connections = [len(value['relations']) for value in my_group.values()]
print("Every person in the group has an average of", sum(group_connections)/len(group_connections),"relations")

# Block of code that extracts the maximum age in the group
group_ages = [value['age'] for value in my_group.values() if len(value['relations']) > 0]
print("the maximum age of people in the group that have at least one relation is :", max(group_ages))

# Block of code that extracts the maximum age of people in the group that have at least one friend
group_ages = [value['age'] for value in my_group.values() for relation_value in value['relations'] if relation_value['type'] == Relation.FRIEND]
print("the maximum age of people in the group that have at least one relation is :", max(group_ages))