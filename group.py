friends = {
    'Jill' : {
        "age": 26, 
        "job": "Biologist", 
        "relation" : {
            "friend":"Zalika",
            "partner":"John"
            },
        },
    'Zalika' : {
        "age": 28, 
        "job": "Artist", 
        "relation" : {
            "friend":"Jill"
            },
        },
    'John' : {
        "age": 27, 
        "job": "Writer", 
        "relation" : {
            "partner":"Jill"
            },
        },
    'Nash' : {
        "age": 34, 
        "job": "Chef", 
        "relation" : {
            "cousin":"John",
            "landlord":"Zalika"
            },
        },
}
print(max([data["age"] for people, data in friends.items()]))
print(len([data["relation"] for people, data in friends.items()])/sum([len(relatives) for relatives in [data["relation"] for people, data in friends.items()]]))
print(max([data["age"] for people, data in friends.items()if len(data["relation"]) > 1]))