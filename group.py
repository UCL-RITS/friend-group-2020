"""An example of how to represent a group of acquaintances in Python."""

# use dictionaries 
# use lists

#person keys: name, age, job, connections to others


    #Jill is 26, a biologist and she is Zalika's friend and John's partner.
    #Zalika is 28, an artist, and Jill's friend
    #John is 27, a writer, and Jill's partner.
    #Nash is 34, a chef, John's cousin and Zalika's landlord.

#should allow people to have no job
#should allow people to have no connections
#reciprocal connections?

# Your code to go here...

my_group = {
    'Jill': {
        'age': 26,
        'job': 'biologist',
        'connections': {
            'Zalika': 'friend',
            'John': 'partner',
        }
    },

    'Zalika': {
        'age': 28,
        'job': 'artist',
        'connections': {
            'Jill': 'friend'
        }
    },

    'John': {
        'age': 27,
        'job': 'writer',
        'connections': {
            'Jill': 'partner',
            'Nash': 'cousin'
        }
    },

    'Nash': {
        'age': 34,
        'job': 'chef',
        'connections': {
            'John': 'cousin',
            'Zalika': 'landord'
        }
    }
}


# function to compute mean of non-empty list of numbers
def mean(data):
    return sum(data)/len(data)

# max age of people in group
print(max(person['age'] for person in my_group.values()))   #34

# average number of relations among members of the group
print(mean([len(person['connections'])for person in my_group.values()]))    #1.75

# max age of people in the group that have min 1 relation
print(max(person['age'] for person in my_group.values() if person['connections']))  #34

# max age of people in group with min 1 friend
print(max(person['age'] for person in my_group.values() if 'friend' in person['connections'].values())) #28



