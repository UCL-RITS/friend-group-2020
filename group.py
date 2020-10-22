"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = []

class group_member():
    def __init__(self, name, age, job = "student"):
            self.name = name
            self.age = age
            self.job = job
            self.relationships = []

    def newRelationship(self, person, connection):
            self.relationships.append([person, connection])


Brendan = group_member("Brendan", 26)
Kumail = group_member("Kumail", 22)
Weichao = group_member("Weichao", 22)
Yuyang = group_member("Yuyang", 22)

my_group.append(Brendan)
my_group.append(Kumail)
my_group.append(Weichao)
my_group.append(Yuyang)

Brendan.newRelationship(Kumail, "classmate")

Jill = group_member("Jill", 26, "biologist")
Zalika = group_member("Zalika", 28, "artist")
John = group_member("John", 27, "writer")
Nash = group_member("Nash", 34, "chef")

Jill.newRelationship(Zalika, "friend")
Jill.newRelationship(John, "partner")
Zalika.newRelationship(Jill, "friend")
John.newRelationship(John, "partner")
John.newRelationship(Nash, "cousin")
Nash.newRelationship(John, "cousin")
Nash.newRelationship(Zalika, "landlord")
