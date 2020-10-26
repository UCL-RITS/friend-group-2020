group = {
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
import numpy as np

ages=[]

for person in group:
    ages.append(group[person]["age"])
print('maximum age of people in the group is', np.max(ages))



#the average (mean) number of relations among members of the group
relation = []
for person in group:
    #print(group[person]["relations"])
    relation.append(len(group[person]["relations"].keys()))
print('average number of relations among members of the group is', np.mean(relation))


#the maximum age of people in the group that have at least one relation
age_n = []
for person in group:
    if len(group[person]["relations"].keys()) >= 1:
        age_n.append(group[person]["age"])
print('maximum age of people in the group that have at least one relation is', np.max(age_n))



#[more advanced] the maximum age of people in the group that have at least one friend
Ages = []
for person in group:
    if "friend" in group[person]["relations"].values():
        Ages.append(group[person]["age"])
                
print('The maximum age of people in the group that have at least one friend is', np.max(Ages))



