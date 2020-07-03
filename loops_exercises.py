# #Question 1 
# add via append 
# my_list = [1, 4, 2, 1]

# # while loop + 

# while len(my_list) < 5:
#     my_var = input("give me a number? ")
#     my_list.append(my_var)
#     print(my_var)
#     print(my_list)

# print(my_list)


#Question 2 
#print each item in the list + amount: 
# pets = [
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Biscuit", "biscuit@whippes.park"],
#     ["Rory", "rory@whippies.park"],
# ]
# print(pets)

# # #display for loop to access each item 
# for pet in pets: 
#     print(f"{pets[0]}:")
# for pet in pets[0:]:
#     print(f"       {pet}")
       
#Question 3 

#Ask user for three names 
# name = input("What are three names?")
# while len(name) > 1: 
#     if name == "Izzy":
#         print("You are awesome!")
#     else: 
#         print(f"Hi {name}")
#     name = input("What is your name? ")

# while True:
#     name = input("What is your name? ")

# name.append(["Archie", "Boston"])
# print(name_collection)

#Question 4

# groceries = [
#     ["Baby Spinach", 2.78],
#     ["Hot Chocolate", 3.70],
#     ["Crackers", 2.10],
#     ["Bacon", 9.00],
#     ["Carrots", 0.56],
#     ["Oranges", 3.08]
# ]
# print(groceries)

# total = 0
# for item in groceries:
#     quantity = input(f"What quantity of {item[0]} would you like? ")
#     item[1] = item[1] * int(quantity)
#     total += item[1]
# total = f"${total:.2f}"
# print("====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item[0]:<20} ${item[1]:.2f}")
# print("============================")
# print(f"{total:>27}")
