"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill':{'Age':26,'Job':'biologist','Relationship':{'Zalika':'friend','John':'partner'}},
'Zalika':{'Age':28,'Job':'artist','Relationship':{'Jill':'friend'}},
'John':{'Age':27,'Job':'writer','Relationship':{'Jill':'partner'}},
'Nash':{'Age':34,'Job':'chef','Relationship':{'John':'cousin','Zalika':'landlord'}}}


# the maximum age of people in the group

max_age=max([my_group[x]['Age'] for x in list(my_group.keys())])
name=[]
for x in list(my_group.keys()):
	if my_group[x]['Age'] == max_age:
		name.append(x)

print('The maximum age of people in the group is '+str(max_age)+', who is/are '+str(*name)+'.')


max_age = max([my_group[x]['Age'] for x in list(my_group.keys())])
name = []
for x in list(my_group.keys()):
	if my_group[x]['Age'] == max_age:
		name.append(x)
print('The maximum age of people in the group is '+str(max_age)+', who is/are '+str(*name)+'.')



# the average (mean) number of relations among members of the group
mean_number = [my_group[x]['Relationship'].__len__() for x in list(my_group.keys())]

mean_number =[my_group[X]['Relationship'].__len__() for X in list(my_group.keys()) ]
print('The average (mean) number of relations among members of the group is '+str(mean_number)+'.')



# the maximum age of people in the group that have at least one relation
max_age_one_relation = [my_group[x]['Age'] for x in list(my_group.keys()) if my_group[x]['Relationship'] != {}]
max_age_one_relation = max(max_age_one_relation)
name = []
for x in list(my_group.keys()):
	if my_group[x]['Age'] == max_age_one_relation:
		name.append(x)
print('The maximum age of people in the group that have at least one relation is '+str(max_age_one_relation)+', who is/are '+str(*name)+'.')


# [more advanced] the maximum age of people in the group that have at least one friend
max_age_one_friend = [my_group[x]['Age'] for x in list(my_group.keys()) if 'friend' in list(my_group[x]['Relationship'].values())]
max_age_one_friend = max(max_age_one_friend)
name = []

for x in list(my_group.keys()):
	if my_group[x]['Age'] == max_age_one_friend:
		name.append(x)
print('The maximum age of people in the group that have at least one friend is '+str(max_age_one_friend)+', who is/are '+str(*name)+'.')
