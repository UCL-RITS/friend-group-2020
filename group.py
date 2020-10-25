"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
		'Jill' :{
			'age': 26,
			'job':['biologist'],
			'relations':{'friend':['Zalika'],'partner':['John']}
			},
        'Zalika' :{
			'age':28,
			'job':['Artist'],
			'relations':{'friend':['Jill']}
			 }, 
		'John' :{
			'age':27,
            'job':['Writer'],
            'relations':{'partner':['Jill']}
			},
		"Nash":{
        	"age": 34,
        	"job": "chef",
        	"relations": {'cousin':['John'], "landlord": ["Zalika"]}
        }
}
all_ages= []
age_dic = {name : people['age'] for name, people in my_group.items()}
for ages in age_dic.values():
	all_ages += [ages]
print(max(all_ages))

ttl_number, ttl_relation, all_ages_with_relation, all_ages_with_friend = 0 , 0, [], []
relation_dic = {name : people['relations'] for name, people in my_group.items()}
for name, relations in relation_dic.items():
	relations = dict(relations)
	ttl_number += 1
	for each_person in relations.values():
		ttl_relation = ttl_relation + len(each_person)
	if relations != {}:
		all_ages_with_relation += [age_dic[name]] 
		if 'friend' in relations.keys() :
			all_ages_with_friend += [age_dic[name]]

print(str(ttl_relation/ttl_number))	
print(max(all_ages_with_relation))
print(max(all_ages_with_friend))

