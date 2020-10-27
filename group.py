"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...


class Person:
    def __init__(self, name, age, job, connection={} ):
        self.name = name
        self.age = age
        self.job =job
        self.connection = connection

    def add_connection(self, friend, relationship):
        self.connection.update({friend.name:relationship})
        if relationship=='friend' or relationship=='partner':
            friend.connection.update({self.name:relationship})


jill=Person('Jill', 26, 'biologist')
zalika = Person('Zalika', 28, 'artist')
john=Person('John', 27, 'writer')
#nash=Person('Nash', 34, 'chef')

jill.add_connection(zalika, 'friend')
jill.add_connection(john, 'partner')
print(zalika.connection)
print(jill.connection)
#zalika.add_connection(jill, 'friend')


