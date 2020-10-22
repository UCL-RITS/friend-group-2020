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

ages = [my_group[key]['age'] for key in my_group.keys()]
ages_rel = [my_group[key]['age'] for key in my_group.keys() if my_group[key]['relations']] #includes age if relations not empty (however in this case all entries have at least one relation)
ages_frnd = [my_group[key]['age'] for key in my_group.keys() if 'friend' in my_group[key]['relations'].values()]


print("Maximum overall age is %i" % max(ages))
print("Average overall age is %f" % (sum(ages)/len(ages)))
print("Maximum age of those with at least one relative is %i" % max(ages_rel))
print("Maximum age of those with at least one friend is %i" % max(ages_frnd))

