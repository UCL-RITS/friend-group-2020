"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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

max_age = (max([value["age"] for value in my_group.values()]))
print("The maximum age of people in this group is " + str(max_age))

len_relations = [len(value['relations']) for value in my_group.values()]
mean_relations = (sum(len_relations)/len(len_relations))
print("The mean number of relations among members of the group is " + str(mean_relations))

age_one_relation = [value['age'] for value in my_group.values() if len(value['relations']) >=1]
max_age_one_relation = str(max(age_one_relation))
print("The maximum age of people in the group that have at least one relation is " + max_age_one_relation)

import json

group_file = json.dumps(my_group, indent=4)

print(group_file)
