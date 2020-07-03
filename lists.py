print("lists yay!")

tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]

print(tea_collection) 

print(tea_collection[1])
print(tea_collection[3])
print(tea_collection[0:2])
print(tea_collection[2:4])

print(tea_collection[-1])
print(tea_collection[-2])  
print(tea_collection[1:-1])
print(tea_collection[-3:-1])

#Assign items 
tea_collection[-1] = "Melbourne Breakfast"
print(tea_collection)

print(tea_collection[-3:])

print()

#Length of list 
print(len(tea_collection))

#Add one item 
tea_collection.append("Chai")
print(tea_collection)
print(len(tea_collection))

#Add multiple items to list at once 
tea_collection.extend(["New York Breakfast", "Berry"])
print(tea_collection)

print()

#Delete item from list (automatically done) 
print(tea_collection.pop())
print(tea_collection)

#Remove specific item in a list 
print(tea_collection.pop(1))
print(tea_collection)

#Remove specific string in a list 
tea_collection.remove("Chai")
print(tea_collection)

#Remove bunch of items at once 
del tea_collection[1:3]
print(tea_collection)

#Empty/ Clear the list 
tea_collection.clear()
print(tea_collection)

#Put lists inside lists (sub-lists) 
tea_collection = [
   ["Earl Grey", "Melbourne Breakfast", "Chai"], 
   ["Peppermint", "Lemon and Ginger", "Strawberry Cream"]
]
print(tea_collection)
#= each item is now another separate list 

#Print FIRST item in the FIRST list 
print(tea_collection[0])
print(tea_collection[0][0])

black_teas = tea_collection[0]
print(black_teas)

#Add another sub-list to the list 
tea_collection.append(["Chamomile", "Green", "Dandelion"])
print(tea_collection)

#Tie lists with if statements 
print(len(tea_collection))

if len(tea_collection) > 3: 
    print("greater than 3")
else: 
    print("less than or equal to 3")

black_teas = tea_collection[0]
print(black_teas)

if "Chai" in black_teas:  
    print("Yay! we have Chai!")

