"""An example of how to represent a group of acquaintances in Python."""

entries = [
    ["Jill", 26, "biologist", {"friend":"Zalika","partner":"John"}],
    ["Zalika", 28, "artist", {"friend":"Jill"}]
           ]

my_group = [
    {'name': 'Jill', 'age': 26, 'job': 'biologist', 'relation': {'friend': 'Zalika', "partner":"John"}}, 
    {'name': 'Zalika', 'age': 28, 'job': 'artist', 'relation': {'friend': 'Jill'}}
    ]

"""
def write_entries(entries):
    """ take entries and put them (in order) into the base_dict template """

    base_list = [] # return this in the end
    base_dict = {"name":None, "age":None, "job":None, "relation":None}

    for entry in entries:
        print(entry)

        user_dict = {**base_dict}
        for k,key in enumerate([*base_dict]):
            
            print(key, '=', entry[k])
            user_dict[key] = entry[k]

        base_list.append(user_dict)

    return base_list

# list for everyone to go in
my_group = write_entries(entries)

print("\n people in the group:")
for person in my_group: 
    print(person)
"""