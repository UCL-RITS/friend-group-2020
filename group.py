"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

friends={
    'Jill' : {'age' : '26' , 'job' : 'a Biologist'  , 
              'connection' : {
                  'Zalika':'friend',
                  "John" : 'partner'
                  }
              },
    'Zalika' : {'age' : '28' , 'job' : 'an Artist'  , 
                'connection' : {
                    'Jill' : 'friend'
                    }
                },
    'John' : {'age' : '27' , 'job' : 'a Writer'  ,
              'connection' : {
                  'Jill' : 'partner'
                  }
              },
    'Nash' : {'age' : '34' , 'job' : 'a Chef'  , 
              'connection' : {
                  'John' : 'cousin',
                  'Zalika' : 'landlord'
                  }
              }
    }

maxage = max([deets['age']  for person , deets in friends.items()])
avgconnection = sum([len(deets['connection']) for person, deets in friends.items()])//4
oldestif1=max([deets['age'] for person, deets in friends.items() if len(deets['connection']) > 0 ])
oldestif1friend = max( [deets['age'] for person, deets in friends.items()  if 'friend' in friends[person]['connection'].values() ])


print('The age of the oldest person in the group is ', maxage, ' years old.')
print('Each person has' , avgconnection, 'relation on average.')
print('The maximum age of the person in the group that has at least one relation is', oldestif1, 'years old.')
print('The maximum age of the person in the group that has at least one friend is', oldestif1friend, 'years old.')