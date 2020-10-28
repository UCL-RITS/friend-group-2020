"An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Kyriazis":{"age":25,
                        "job":"Msc Student",
                        "relations":{"Mathew","Friend"}
                        },
            "Mathew":{"age":24,
                    "job":"Phd Student",
                    "relations":{"Kyriazis":"Friend","Michael":"Friend"}
                    },
            "Michael":{"age":25,
                    "job":"Phd Student",
                    "relations":{"Kyriazis":"Friend","Mathew":"Friend"}
                    },
            "Emre":{"age":22,
                    "job":"Mres",
                    "relations":{"Kyriazis":"Friend","Mathew":"Friend","Michael":"Friend"}
                    }        
            } 
print(f"All relations of Emre {my_group['Emre']['relations']}")                               

print(f"Relationship between Emre and Kyriazis {my_group['Emre']['relations']['Kyriazis']}")   

