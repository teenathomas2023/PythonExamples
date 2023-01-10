# keys method keys()
'''names = { "name1": "RAvi",

"name2" : "Rajeev",
"name3": "Raghu"
}
x= names.keys()
names["name4"]="Teena"

y= names.values()

print(y)
print(x)

# get method get()

z= names.get("name4")
print(z)

q =names.get("age",25)
print(q)
print (names)
# here you will notice the age is created temporarily
# so it is not displayed when you dispaly the dictionary names
'''
#items() method
# the items method gives key value pairs of the dictionary.
'''
names = {
    "name1": "Ravi",
    "name2": "Rajeev",
    "name3" : "Raghu"
    }
x= names.items()
print(x)
names['name3'] = "Teena"
print(x)
'''
# pop method, pop() method removes the specified item from the dictionary.
# The value of the removed item is the return value of the pop() method.
'''
names = {
    "name1": "Ravi",
    "name2": "Rajeev",
    "name3" : "Raghu"
    }
names.pop("name3")
print(names)

# popitem() method

javascript ={
    "framework1": "React JS",
    "framework2": "Angular JS",
    "framework3": "Vue",
}
# The popitem() method removes the item that was last inserted into the dictionary.
javascript.popitem()
print(javascript)
'''

#update() method

names = {
    "name1": "Ravi",
    "name2": "Rajeev",
    "name3" : "Raghu"
    }
# The update() method inserts the specified items to the dictionary.

names.update({"color":"dodgerblue"})

print(names)