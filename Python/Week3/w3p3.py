# Initialize a dictionary of capitals in the form capitals={‘Karnataka’:’Bangalore’,’Maharashtra’:’Mumbai’,’Tamilnadu’:’Chennai’} 
# Execute the following and observe the output: 
# a) capitals.keys() 
# b) capitals.values() 
# c) capitals.items() 
# d) capitals.get(‘Karnataka’) 
# e) print(capitals) 
# f) other_capitals={‘Gujarat’:’Ahmedabad’,} 
# g) capitals.update(other_capitals) 
# h) print(capitals) 
# i) print(other_capitals)

capitals = {
    "Karnataka": "Bangalore",
    "Maharashtra": "Mumbai",
    "Tamilnadu": "Chennai",
}
print(capitals.keys())
print(capitals.values())
print(capitals.items())
print(capitals.get("Karnataka"))
print(capitals)
other_capitals = {"Gujarat": "Ahmedabad"}
capitals.update(other_capitals)
print(capitals)
print(other_capitals)