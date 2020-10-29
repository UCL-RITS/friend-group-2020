"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

Yohn = {"name":"Yohn",
        "age":25,
        "Jobs":"Phd",
        "Acquaintances":[["Yewen","Friend"],["Kris","Colleague"]]}
Yewen={"name":"Yewen", 
       "age":22,
       "Jobs":"student",
       "Acquaintances":[["Yohn","Friend"],["Alice":"Flatmate"]]} 

my_group =[Yohn,Yewen]

print(my_group)

for i in range(len(my_group)):
    entry = my_group[i]
    print(entry["name"],"is",str(entry["age"],",a(n)",
          entry["Jobs"],"and (s)he is ", 
          entry["Acquaintances"][0][0]," 's ", entry["Acquaintances"][0][1],".")  
