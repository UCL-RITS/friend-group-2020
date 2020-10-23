"""An example of how to represent a group of acquaintances in Python."""


      
my_group ={
    "Jill":{"name": "Jill", "age": 26, 
           "Jobs": "Biologist", "Aquaintances" : {"Zalika":"Friend","John":"Partner"}},

    "Zalika":{"name": "Zalika", "age": 28, 
           "Jobs": "Artist", "Aquaintances" : {"Jill":"Friend"}},

    "John":{"name": "John", "age": 27, 
           "Jobs": "Writer", "Aquaintances" : {"Jill":"Partner"}}, 

    "Nash":{"name": "Nash", "age": 34, 
           "Jobs": "Chef", "Aquaintances" : {"John":"Cousin","Zalika":"Landlord"}} }

# All done in one line using list comprehensions but brevity comes at the cost of being harder to read
# Normally I would do some of these calculations on multiple lines so it is clearer
max_age = max([my_group[key]["age"] for key in my_group.keys()])
mean_relations = sum([len(my_group[key]['Aquaintances'].values()) for key in my_group.keys()]) / len(my_group.keys())
max_age_relations = max([my_group[key]["age"] for key in my_group.keys() if my_group[key]['Aquaintances'].values()])
max_age_friend = max([my_group[key]["age"] for key in my_group.keys() if "Friend" in my_group[key]['Aquaintances'].values()])



print(f"The maximum age of the group is {max_age}.")
print(f"The average number of relations in the group is {mean_relations}.")
print(f"The maximum age of people who have at least one relation is {max_age_relations}.")
print(f"The maximum age of people who have at least one friend is {max_age_friend}.")