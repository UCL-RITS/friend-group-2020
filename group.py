"""An example of how to represent a group of acquaintances in Python."""

import numpy as np

my_group = {
	"Jill" : {
		"Age" : 26,
		"Occupation" : "Biologist",
		"Connections" : {
			"Zalika" : "friend",
			"John" : "partner"
		}
	},
	"Zalika" : {
		"Age" : 28, 
		"Occupation" : "Artist",
		"Connections" : {
			"Jill" : "friend"
		}
	},
	"John" : { 
		"Age" : 27, 
		"Occupation" : "Writer", 
		"Connections" : { 
			"Jill" : "partner" 
		}
	},
	"Nash" : { 
		"Age" : 34, 
		"Occupation" : "Chef", 
		"Connections" : { 
			"John" : "cousin", 
			"Zalika" : "landlord" 
		}
	}
}

ages = [friend["Age"] for friend in my_group.values()]
print("Maximum age in friend group = ", np.max(ages))
print("Average age in friend group = ", np.mean(ages))

agesWithRelations = [friend["Age"] for friend in my_group.values() if len(friend["Connections"]) >= 1]
print("Maximum age of friend in group with at least one relation = ", np.max(agesWithRelations))

agesWithFriends = [friend["Age"] for friend in my_group.values() if "friend" in friend["Connections"].values()]
print("Maximum age of friend in group with at least one friend = ", np.max(agesWithFriends))
