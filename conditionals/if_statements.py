# #If Statements 

# is_raining = True 
# is_cold = False 

# if is_raining is True: 
#     print("You will need an umbrella today!")

# if is_cold:
#     print("You will need a jumper today!")

# temperature = 16

# if temperature < 12:
#     print("Omg it is actually slightly cool in Perth")
# else: 
#     print("Urgh when can I wear my jeans?!")

# temperature = 16
# windchill = 4
# is_cold = temperature - windchill < 16
# is_raining = False 
# print(is_cold)

# if is_cold: 
#     print("You will need a jumper today!")
# else: 
#     print("No need for a jumper today!")

if is_cold and is_raining:
    print("Just stay home")
else:
    # print("It's ok outside")
    if is_raining:
        print("You will need an umbrella today!")
    if is_cold:
        print("You will need a jumper today!")
    
