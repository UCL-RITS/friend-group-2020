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

################################### Add statistics ###########################################

# the maximum age of people in the group
# the average (mean) number of relations among members of the group
# the maximum age of people in the group that have at least one relation
# [more advanced] the maximum age of people in the group that have at least one friend
max_age = 0
number_of_relation = 0
max_age_w_relation = 0
max_age_w_friend = 0
oldest = []
oldest_w_relation = []
oldest_w_friend = []

for person, data in group.items():
    # count the relations
    number_of_relation = number_of_relation + len(data['connection'])
    
    if data['age'] >= max_age:     # find max age
        max_age = data['age']
        oldest = person
    if len(data['connection'])>0: # find max age with relations
        if data['age'] >= max_age_w_relation:
            max_age_w_relation = data['age']
            oldest_w_relation = person
    if 'friend' in data['connection'].values():
        if data['age'] >= max_age_w_friend:
            max_age_w_friend = data['age']
            oldest_w_friend = person
            
print('Maximum age is', max_age ,' years, The name is', oldest)
print('Maximum age with relation is', max_age_w_relation ,' years, The name is ', oldest_w_relation)
print('Maximum age with friend is', max_age_w_friend ,' years, The name is ',oldest_w_friend)
