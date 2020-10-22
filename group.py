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

print(group.items())

max_age = 0
max_age_with_relation = 0
max_age_with_friend = 0
num_relations = 0

for name, info in group.items():
    if info['age'] > max_age:
        max_age = info['age']
    if len(info['connection']) > 0 and info['age'] > max_age_with_relation:
        max_age_with_relation = info['age']
    if 'friend' in info['connection'].values() and info['age'] > max_age_with_friend:
        max_age_with_friend = info['age']
    num_relations += len(info['connection'])

print('maximum age: ', max_age)
print('maximum age with relation: ', max_age_with_relation)
print('maximum age with friend: ', max_age_with_friend)
print('mean number of relations: ', num_relations/len(group))