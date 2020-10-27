"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
import json
my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "relations": {
            "Zalika": "friend",
            "John": "partner"
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "relations": {
            "Jill": "friend"
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "relations": {
            "Jill": "partner"
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "relations": {
            "John": "cousin",
            "Zalika": "landlord"
        }
    }
}

ages =[my_group[key]['age'] for key in my_group.keys()]
relations =[my_group[key]['relations'] for key in my_group.keys()]
ttl_rel_len = sum([len(each.keys()) for each in  relations])
ages_with_rel =[my_group[key]['age'] for key in my_group.keys() if my_group[key]['relations']] 
ages_with_fri =[my_group[key]['age'] for key in my_group.keys() if 'friend' in my_group[key]['relations'].values()] 

print('the maximum age of people in the group: %d' %max(ages))
print('the average (mean) number of relations among members of the group: %.2f' %(ttl_rel_len/len(ages)))
print('the maximum age of people in the group that have at least one relation: %d' %max(ages_with_rel))
print('the maximum age of people in the group that have at least one friend: %d' %max(ages_with_fri)) 

