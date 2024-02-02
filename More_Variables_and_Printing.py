name = 'Zed'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
c_height = height*2.54
k_weight = weight*.4535924

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Or, {c_height} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"Or, {k_weight} kilograms heavy.")
print("Actually not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + c_height + k_weight
print(f"If I add {age}, {c_height}, and {k_weight}, I get {total}.")