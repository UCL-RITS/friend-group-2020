"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

#my_group ={}
a = [{"name": "Jill", "age": 26,
      "job": "Biologist", "relation": {"friend": "Zalika", "partner": "John"}},
     {"name": "Zalika", "age": 28,
      "job": " artist", "relation": {"friend": "Jill"}},
     {"name": "John", "age": 27,
      "job": " writer", "relation": {"partner": "Jill"}},
     {"name": "Nash", "age": 34,
      "job": " chef", "relation": {"cousin": "Jill", "landlord": "Zalika"}}]
print(a)
