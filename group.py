"""An example of how to represent a group of acquaintances in Python."""


      
my_group ={"Jill":{"name": "Jill", "age": 26, 
           "Jobs": "Biologist", "Aquaintances" : {"Zalika":"Friend","John":"Partner"}},
"Zalika":{"name": "Zalika", "age": 28, 
           "Jobs": "Artist", "Aquaintances" : {"Jill":"Friend"}},
"John":{"name": "John", "age": 27, 
           "Jobs": "Writer", "Aquaintances" : {"Jill":"Partner"}}, 
"Nash":{"name": "Nash", "age": 34, 
           "Jobs": "Chef", "Aquaintances" : {"John":"Cousin","Zalika":"Landlord"}} }

names_and_ages={ages: room['age'] for ages, room in my_group.items()}
max_age = max(names_and_ages.values())
max_name = [k for k, v in names_and_ages.items() if v == max_age]
print( "Oldest person/people:",max_name,"at age:",max_age)

# names_and_relations={A: room['Aquaintances'] for A, room in my_group.items()}
ppl_and_rels={name: len(room['Aquaintances']) for name, room in my_group.items()}
total_ppl=len(ppl_and_rels)
total_rels=sum(ppl_and_rels.values())
print("Average number of relations is:",total_rels/total_ppl)

at_least_1_rel={name: room['age'] for name, room in my_group.items() if len(room['Aquaintances']) > 0}
max_age1 = max(at_least_1_rel.values())
max_name1 = [k for k, v in at_least_1_rel.items() if v == max_age1]
print("Maximum age of people with at least 1 relation is:",max_age1 ,", and this is/these are:",max_name1)

ppl_and_rels2={name: room['Aquaintances'] for name, room in my_group.items()}
keys_list = list(ppl_and_rels2.keys())
k=len(keys_list)

popular_people=[]
pop_friends_deets={}
for i in range(k):
    ppl_with_friends = [k for k, letter in ppl_and_rels2[keys_list[i]].items() if letter == "Friend"]
    if len(ppl_with_friends)>0:
        popular_people+=[keys_list[i]]

k=len(popular_people)
for t in range(k):
    pop_friends_deets[popular_people[t-1]]=my_group[popular_people[t-1]]

names_and_ages2={ages: room['age'] for ages, room in pop_friends_deets.items()}    
max_age2 = max(names_and_ages2.values())
max_name2 = [k for k, v in names_and_ages2.items() if v == max_age2]     
print( "Oldest person/people with at least 1 friend is:",max_name2,"at:",max_age2)       



