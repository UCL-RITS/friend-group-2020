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
        'job': ['biologist'],
        'connections': {
            'friends': ['Zalika'],
            'partner': ['John'],
            'cousins': [],
            'landlord_of': []
        }
    },

    'Zalika': {
        'age': 28,
        'job': ['artist'],
        'connections': {
            'friends': ['Jill'],
            'partner': [],
            'cousins': [],
            'landlord_of': []
        }
    },

    'John': {
        'age': 27,
        'job': ['writer'],
        'connections': {
            'friends': [],
            'parter': ['Jill'],
            'cousins': ['Nash'],
            'landlord_of': []
        }
    },

    'Nash': {
        'age': 34,
        'job': 'chef',
        'connections': {
            'friends': [],
            'parter': [],
            'cousins': ['John'],
            'landlord_of': ['Zalika']
        }
    }
}