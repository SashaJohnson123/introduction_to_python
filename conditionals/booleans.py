#Booleans

is_raining  = True
is_cold = False

print(is_raining)
print(is_cold)

print("AND Comparisons:")

is_raining = False 
is_cold = False 
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)

is_raining = False 
is_cold = True 
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)

is_raining = True 
is_cold = False 
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)

is_raining = True 
is_cold = True 
print(is_raining and is_cold, not is_cold, is_raining and not is_cold)

print("OR Comparisons:")
is_raining = False 
is_cold =  False 
print(is_raining or is_cold, is_raining or not is_cold)

is_raining = False 
is_cold =  True 
print(is_raining or is_cold, is_raining or not is_cold)

is_raining = True 
is_cold =  False 
print(is_raining or is_cold, is_raining or not is_cold)

is_raining = True 
is_cold =  True 
print(is_raining or is_cold, is_raining or not is_cold)


print()
is_raining = True 
is_cold = True
is_raining_and_is_cold = is_raining and is_cold
print(is_raining_and_is_cold)
