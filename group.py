import numpy as np

group = {
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

# 1) Get maximum age of group 

print(max(person['age'] for person in group.values()))

# 2) Get mean number of relations

print(np.mean([len(p['connection']) for p in group.values()]))

# 3) Get maxmium age of people that have at least one relation

print(max(person['age'] for person in group.values() if len(person['connection'])))

# 4) Get maxmium age of people that have at least one friend 

print(max(person['age'] for person in group.values() if 'friend' in person['connection'].values()))
