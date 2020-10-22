"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill' : {'Name': 'Jill', 
                      'Age':26, 
                      'job':'biologist',
                      'connections': [{'type':'friend','to':'Zalika'}, {'type':'partner','to':'John'}]}, 
           'Zalika' : {'Name': 'Zalika', 
                       'Age':28, 
                       'job':'artist',
                       'connections':[{'type':'landlord','to':'Nash'},{'type':'friend','to':'Jill'}]},
           'John' : {'Name': 'John', 
                     'Age':27, 
                     'job':'writer',
                     'connections':[{'type':'cousin','to':'Nash'},{'type':'partner','to':'Jill'}]},
           'Nash' : {'Name': 'Nash', 
                     'Age':34, 
                     'job':'chef',
                     'connections':[{'type':'cousin','to':'John'},{'type':'tenant','to':'Zalika'}]}}

age_list=[]
relation_count=[]
social_age_list=[]
havefriend_age_list=[]

for people, people_dic in my_group.items():
    age_list.append(people_dic['Age'])
    relation_count.append(len(people_dic['connections']))
    if len(people_dic['connections']) != 0 :
        social_age_list.append(people_dic['Age'])
    have_friend = False
    for connection_dic in people_dic['connections']:
        if connection_dic['type'] == 'friend':
            have_friend = True
    if have_friend == True:
        havefriend_age_list.append(people_dic['Age'])

age_list.sort()    
social_age_list.sort()
print('The maximum age of people in the group is',age_list[-1])
print('The average (mean) number of relations among members of the group is',int(sum(relation_count)/len(relation_count)))
print('The maximum age of people in the group that have at least one relation is',social_age_list[-1])
print('The maximum age of people in the group that have at least one friend is',havefriend_age_list[-1])


