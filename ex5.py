name = 'Khaya Ubisi'
age = 32
height = 1.7 #meters
weight = 70 #kgs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_inches = "{:.2f}".format(height * 39.37)
weight_pounds = weight * 2.205

print(f"Let's talk about {name}.")
print(f"He's {height} meters tall.")
print(f"He weighs {weight} kilograms.")
print("Actually he's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"He's {height} meters tall, which is {height_inches} inches.")
print(f"He weighs {weight} kilograms, {weight_pounds} in pounds.")

#this line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

