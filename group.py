"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
jill = {"name": "Jill", "age": 26,
        "job": "biologist"}

zalika = {"name": "Zalika", "age": 28,
          "job": "artist"}

john = {"name": "John", "age": 27,
        "job": "writer"}

nash = {"name": "Nash", "age": 0,
        "job": "chef"}

jill["friend"] = zalika
jill["partner"] = john
jill["cousin"] = nash
zalika["friend"] = jill
zalika["landlord"] = nash
john["partner"] = jill

example_group = [jill, zalika, john, nash]

weixi = {"name": "Weixi Zhang", "age": 20,
        "job": "student"}
# aaa = ...
my_group = [weixi] #, aaa

print(my_group[2]["job"])

