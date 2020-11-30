import json 
import statistics

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

# Comprehensions
# Maximum age in group
max_age = max(person['age'] for name, person in group.items())
print(max_age)

# Average number of relations among members of the group
average = statistics.mean(len(person['relations']) for name, person in group.items())
print(average)

# Maximum age of people who have at least 1 relation
max_age_2 = max(person['age'] for name, person in group.items() if (len(person['relations']) > 0) )
print(max_age_2)

# Maximum age of people who have at least 1 friend
max_age_3 = max(person['age'] for name, person in group.items() if 'friend' in person['relations'].values())
print(max_age_3)

# create file and write
with open('group_file.json', 'w') as f:
    json.dump(group, f, indent=4)

# read file and load
with open('group_file.json', 'r') as json_file:
    my_group = json_file.read()

mydata = json.loads(my_group)

print(mydata)


