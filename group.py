"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import numpy as np

my_group = [{
	     	"name":"Jill", 
	     	"age":26,
	     	"occupancy":"biologist",
	     	"relationships":{"friend":"Zalika", "partner":"John"}
	}, {
		"name":"Zalika",
		"age":28,
		"occupancy":"artist",
		"relationships":{"friend":"Jill"}
	}, {
		"name":"John",
		"age":27,
		"occupancy":"writer",
		"relationships":{"partner":"Jill"}
	}, {
		"name":"Nash",
		"age":34,
		"occupancy":"chef",
		"relationships":{"cousin":"John", "tenant":"Zalika"}
	}]


# the maximum age of people in the group

Max_age = max([dict['age'] for dict in my_group])
print("The maximum age of people in the group is",Max_age)

# the average (mean) number of relations among members of the group

relations_vals = [len(dict['relationships']) for dict in my_group]
Mean_relations = np.mean(relations_vals)
print("The average (mean) number of relations among members of the group is",Mean_relations)

# the maximum age of people in the group that have at least one relation
Ages_relations = []

for dict in my_group:
    if len(dict['relationships']) > 0:
        Ages_relations.append(dict['age'])

print("The maximum age of people in this group is",max(Ages_relations),"that at least one relation")

# the maximum age of people in the group that have at least one friend
Ages_friend = []

for dict in my_group:
    if "friend" in dict['relationships'].keys():
        Ages_friend.append(dict['age'])

print("The maximum age of people in the group is",max(Ages_friend),"that have at least one friend")
