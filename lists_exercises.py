# Question 1 
# food_collection = ["Orange", "Apple", "Banana", "Strawberry", "Grape", "Blueberry", ["Carrot", "Cauliflower", "Pumpkin"], "Passionfruit", "Mango", "Kiwifruit"]
# print(food_collection)
# #The first item in the list 
# print(food_collection[0])
# # #The third item in the list 
# print(food_collection[2])
# # #The last item in the list 
# print(food_collection[-1]) 
# # #Remove last 3 items in the list 
# print(food_collection[7:10])
# # #Remove  last item  in the  sub-list 
# print(food_collection[6][-1])


# Question 2 
# mailing_list = [
#     ["Roary", "roary@moth.catchers"], 
#     ["Remus", "remus@kapers.dog"], 
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"], 
#     ["Biscuit", "biscuit@whippies.park"], 
#     ["Rory", "rory@whippies.park"], 
# ]
# print(mailing_list)

#Print listy items in separate lines  
# print(mailing_list[0])
# # print(mailing_list[1])
# # print(mailing_list[2])
# # print(mailing_list[3])
# # print(mailing_list[4])

# #Change comma for ":" and remove square brackets; 
# for pet_category in mailing_list: 
#     print(f"{pet_category[0]}:")
#     for pet in pet_category[1:]:
#         print(f"       {pet}")


#Question 3 

#Ask user for three names  
# name = input("What is your name? ")
# name = input("What is your name? ")
# name = input("What is your name? ")

#Add one item at a time  to a list 
# name_collection = [
#     ["Izzy",]
# ]
# print(name_collection)
# # print(len(name_collection)) 

# name_collection.append(["Archie", "Boston"])
# print(name_collection)
# print(name_collection[0:2])

# Question 4 
#Ask user to input a strong:  
mylist = input("This is a string")

mylist = input("What a lovely day!") 

# my_string = input('hey user, what's your name? ')
my_string = ("Hey user, I need a string for my program,can  you give me one?") 
mylist= list(my_string)
print(mylist)

#length  of string 
length_of_my_string = len(mylist)
print(length_of_my_string, mylist)
# print(f'The length of list is {length_of_my_string} and my list of characters is {mylist}')

list(my_string)
print(mylist)

# # Length of list 
# print(len(mylist))
