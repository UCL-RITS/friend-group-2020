"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

import numpy as np

my_group = [{
	     	"name":"Jill", 
	     	"age":26,
	     	"occupancy":"biologist",
	     	"relationships":{"friends":["Zalika"], "partner":"John"}
	}, {
		"name":"Zalika",
		"age":28,
		"occupancy":"artist",
		"relationships":{"friends":["Jill"], "landlord":"Nash"}
	}, {
		"name":"John",
		"age":27,
		"occupancy":"writer",
		"relationships":{"partner":"Jill", "cousin":"Nash"}
	}, {
		"name":"Nash",
		"age":34,
		"occupancy":"chef",
		"relationships":{"cousin":"John", "tenant":"Zalika"}
	}]

# the maximum age of people in the group
print(f"The maximum age in the group is {max([dict['age'] for dict in my_group])}")

# the average (mean) number of relations among members of the group
print(f"The average number of relations in the group is {np.mean([len(dict['relationships']) for dict in my_group])}")

# NOTE: the following two methods follow different of structuring data, which looks inconsistent.
# 	This is intentional and is done to show both ways..
# 	The first method assumes that all the keys exist even if the correspinding are empty.
#	The second method assumes that if no values correspond to the key, the key itself
#	would not be input into the dictionary.

# the maximum age of people in the group that have at least one relation
ages_withRelations = []
for dict in my_group:
	if len(dict["relationships"])>0: # Checking for a length of an array corressponding to an EXISTING key
		ages_withRelations.append(dict["age"])
print(f"The maximum age in the group among members /w 1+ relations is {max(ages_withRelations)}")

# the maximum age of people in the group that have at least one friend
ages_withFriends = []
for dict in my_group:
	if "friends" in dict["relationships"].keys(): # Checking for the existence of the key
		ages_withFriends.append(dict["age"])
print(f"The maximum age in the group among members /w friends is {max(ages_withFriends)}")
