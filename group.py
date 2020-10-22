"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

#my_group ={}
friends = [{"name": "Jill", "age": 26,
      "job": "Biologist", "relation": {"friend": "Zalika", "partner": "John"}},
     {"name": "Zalika", "age": 28,
      "job": " artist", "relation": {"friend": "Jill"}},
     {"name": "John", "age": 27,
      "job": " writer", "relation": {"partner": "Jill"}},
     {"name": "Nash", "age": 34,
      "job": " chef", "relation": {"cousin": "Jill", "landlord": "Zalika"}},
      {"name": "Jack", "age": 29,"job": "Doctor"}]
print(friends)


#first question-------------
maxage=0
n=len(friends)
for i in range(n):
    if maxage<friends[i]["age"]:
        maxage=friends[i]["age"]
print(maxage)


#second question-------------
allrelation=0
for i in range(n):
    allrelation+=len(friends[i]["relation"])
meanofrelation=allrelation/n
print(meanofrelation)
#third question-------------

maxage1=0
n=len(friends)
for i in range(n):
    if len(friends[i]["relation"])>=1:
        if maxage1<friends[i]["age"]:
            maxage1=friends[i]["age"]
print(maxage1)
#advanced question-------------

maxage2=0
n=len(friends)
for i in range(n):
    if "friend" in friends[i]["relation"]:
        if maxage2<friends[i]["age"]:
            maxage2=friends[i]["age"]
print(maxage2)


