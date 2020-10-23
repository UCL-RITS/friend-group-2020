"""An example of how to represent a group of acquaintances in Python."""

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

# Comprehension to create new dict with names (keys) against ages (values) from dict(group):
ages = {age: name['age'] for age, name in group.items()}  

#Prints max age in list of ages.values:
print("Maximum age:",max(list(ages.values())))

#New dict capturing values against 'relations' key in dict(group):
rel = {n: relation['relations'] for n, relation in group.items()}

#Creates a list from the values in dict(rel):
number = list(rel.values())

# List of all relation types:
rel_list = ['friend', 'partner', 'cousin', 'landlord']

# Empty lists defined for later use:
tot = list()
k = list()
check = int()
l = list()

# New list from values in dict(ages):
list_age = list(ages.values())

# Loops through range 0 to 3, pulling out items from list(number) and list(list_age), which correspond to int(j),
# as strings:
for j in range(4):
    str_num = str(number[j])
    str_age = str(list_age[j])
    
    #Sets int(z) to zero then loops through items in list(rel_list)    
    z = 0
    for x in rel_list:
        
        # Counts the number of times each item in rel_list (x) is found in str_num, 
        # adding the total to int(z) each time:
        y = str_num.count(x)
        z += y
        
        # Adds the person's age to list(l) each time str(x) is equal to 'friend' 
        # and the number of friend relations (int(y)) is more than zero
        if x == "friend" and y > 0:
            l.append(str_age)
    
    # Where the total number of relations int(z) is greater than zero, the person's age is added to list(k)
    if z > 0:
        k.append(str_age)
        
    # Total relations for each person is added to list(tot)
    tot.append(z)
        
# Prints out the required info:
print("Average number of relations:", sum(tot)/len(tot))
print("Maximum age if more than one relation:", max(k))
print("Maximum age if more than one friend:", max(l))
