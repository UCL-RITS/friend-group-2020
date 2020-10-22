"""An example of how to represent a group of acquaintances in Python."""


def main():
    Jill = {"name": "Jill", "age": 26, "job": "biologist", "connections": {"friend": ["Zalika"], "partner": ["John"]}}
    Zalika = {"name": "Zalika", "age": 26, "job": "artist", "connections": {"friend": ["Jill"]}}
    John = {"name": "John", "age": 27, "job": "writer", "connections": {"partner": ["John"]}}
    Nash = {"name": "Nash", "age": 34, "job": "chef", "connections": {"cousin": ["John"], "landlord": ["Zalika"]}}

    my_group = [Jill, Zalika, John, Nash]
    print(my_group)


main()
