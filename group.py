"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill': {},
    'Zalika': {},
    'John': {},
    'Nash': {}
}

my_group['Jill']['age'] =26
my_group['Jill']['job']= "biologist"
my_group['Jill']['relation'] = {'zalika': 'friend', 'john': 'partner'}


my_group['Zalika']['age'] = 28
my_group['Zalika']['job']='artist'
my_group['Zalika']['relation']= {'jill': 'friend'}


my_group['John']['age'] = 27
my_group['John']['job']='writer'
my_group['John']['relation']= {'jill': 'partner'}

my_group['Nash']['age'] = 34
my_group['Nash']['job']='chef'
my_group['Nash']['relation']= {'jill': 'cousin', 'Zalika': 'landlord'}

a1 = max([my_group[key]['age'] for key in my_group])
a2 = sum([len(my_group[key]['relation']) for key in my_group]) / len(my_group)
a3 = max([my_group[key]['age'] for key in my_group if my_group[key]['relation']])
a4 = max([my_group[key]['age'] for key in my_group if my_group[key]['relation'] if 'friend' in my_group[key]['relation'].values()])