"An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {"Kyriazis":{"age":25,
                        "job":"Msc Student",
                        "friends":["Mathew","Michael"]
                        },
            "Mathew":{"age":24,
                    "job":"Phd Student",
                    "friends":["Kyriazis","Michael"]
                    },
            "Michael":{"age":25,
                    "job":"Phd Student",
                    "friends":["Kyriazis","Mathew"]
                    },
            "Emre":{"age":22,
                    "job":"Mres",
                    "friends":["Kyriazis","Michael","Mathew"]
                    }        
            } 
print(my_group["Emre"]["friends"][2])                               
