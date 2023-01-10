#Set 
#Same type of data
'''
days={"Monday","Tuesday","Wednesday","Thursday","Friday"}
print(f"Days:{days}\nType:{type(days)}")
print("Looping through the set elaments:")
for i in days:
    print(i)
'''
#Different type of data
'''
mixed = {5.19,"set",("Paris","London"),"Set"}
print(mixed)
'''
#Creating a set from a tuple
'''
colors = set(("blue","red","green","blue"))
print (colors)
print(type(colors))

# creating a set from a list

colors2 = set(["blue","red","green","blue"])
print(colors2)
print(type(colors2))

'''
# create a set from a dictionary
'''
colors=set(
    {
        "blue":1,
        "red":2,
        "green":3

    }
)
print(colors)
print(type(colors))

# Create empty set
names = {}
print(names)
print(type(names))
numbers = set()
print(numbers)
print(type(numbers))

'''
#Add items to the set

days = set(["Monday","Tuesday","Wedenesday","Thursday","Friday"])
print(f"Days:{days}")
print("\nAdding other days to the set...")
days.add("Saturdays")
days.add("Sunday")
print("\n Printing the modified set...")
for i in days:
 print(i)
