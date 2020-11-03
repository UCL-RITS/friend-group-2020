"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group={
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
