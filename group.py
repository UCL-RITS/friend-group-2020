"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

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

# print(group['Jill']['age'])

def findMaximunAge():
    name = 'Jill'
    temp = group['Jill']['age']
    for people in group:
        if group[people]['age'] > temp:
            name = people
            temp = group[people]['age']
    return name

def mean_realationship():
    temp = 0
    PeopleNo = 0
    for people in group:
        PeopleNo = PeopleNo + 1
        temp = len(group[people]['relations'])+temp
    return temp/PeopleNo

def MaxAgeOnerelationship():
    name = 'Jill'
    temp = group['Jill']['age']
    for people in group:
        if group[people]['age'] > temp and len(group[people]['relations']) >=1:
            name = people
            temp = group[people]['age']
    return name

def MaxAgeOneFriend():
    name = 'Jill'
    temp = group['Jill']['age']
    for people in group:
        if group[people]['age'] > temp and len(group[people]['relations']) >=1:
            for index in group[people]['relations']:
                if group[people]['relations'][index] == 'friend':
                    name = people
                    temp = group[people]['age']
    return name


print(findMaximunAge())
print(mean_realationship())
print(MaxAgeOnerelationship())
print(MaxAgeOneFriend())



    
