"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {'Jill':{'Age':26,'Job':'biologist','Relationship':{'Zalika':'friend','John':'partner'}},
'Zalika':{'Age':28,'Job':'artist','Relationship':{'Jill':'friend'}},
'John':{'Age':27,'Job':'writer','Relationship':{'Jill':'partner'}},
'Nash':{'Age':34,'Job':'chef','Relationship':{'John':'cousin','Zalika':'landlord'}}}

#stores all information except name
groupArray = []

for allInfo in my_group.values():
    groupArray.append(allInfo)

ageArray = []
relationArray = []
for memberInfo in groupArray:
    ageArray.append(memberInfo['Age'])
    relationArray.append(memberInfo['Relationship'])


#the maximum age of people in the group
maxAge = max(ageArray)
print(maxAge)

relationLength = []
for relation in relationArray:
    relationLength.append(relation.__len__())

sum = 0
for i in relationLength:
    sum = sum + i
meanRelation = sum/relationLength.__len__()


#the average (mean) number of relations among members of the group
print(meanRelation)


ageArray2 = []
for a in groupArray:
    if a['Relationship'].__len__() >= 1:
        ageArray2.append(a['Age'])

#the maximum age of people in the group that have at least one relation
maxAge2 = max(ageArray2)
print(maxAge2)



friendArray = []
for a in groupArray:
    for b in a['Relationship'].values():
        if b == 'friend':
            friendArray.append(a['Age'])



#[more advanced] the maximum age of people in the group that have at least one friend
maxAge3 = max(friendArray)
print(maxAge3)

        

    
    
       
        





    


    


    
    
