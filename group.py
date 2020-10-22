"""An example of how to represent a group of acquaintances in Python."""

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

#the maximum age of people in the group

max_age_group = []

for groupname,groupinfo in my_group.items():
    max_age_group.append(groupinfo['age'])
    
print('1- Maximum age of people in group is: ', end="")
print(max(max_age_group))

#the average (mean) number of relations among members of the group

ave_relation_group = []

for groupname,groupinfo in my_group.items():
    relation_nb = len(groupinfo['relations'].values())
    ave_relation_group.append(relation_nb)
    
print('2- Average (mean) number of relations among members of the group is: ', end="")
print(max(ave_relation_group))

# the maximum age of people in the group that have at least one relation

max_age_one_relation = []

for groupname,groupinfo in my_group.items():
    if len(groupinfo['relations'].values()) >= 1:
        max_age_one_relation.append(groupinfo['age'])
    
print('3- Maximum age of people in the group that have at least one relation is: ', end="")
print(max(max_age_one_relation))


# [more advanced] the maximum age of people in the group that have at least one friend

max_age_one_friend = []

for groupname,groupinfo in my_group.items():
    for relation in groupinfo['relations'].values() :
        if relation == 'friend':
            max_age_one_friend.append(groupinfo['age'])
    
print('4- Maximum age of people in the group that have at least one friend is: ', end="")
print(max(max_age_one_friend))
