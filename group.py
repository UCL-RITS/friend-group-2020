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
