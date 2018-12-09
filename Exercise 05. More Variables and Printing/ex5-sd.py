# Exercise 05: More Variables and Printing - Study Drills.

name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height_cm = height_inches * 2.54
weight_lbs = 180 #lbs
weight_kg = weight_lbs * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_inches} inches, or {height_cm} centimeters, tall.")
print(f"He's {weight_lbs} pounds, or {round(weight_kg, 2)} kgs, heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the cofee.")

# this line is tricky, try to get it exactly
total = age + height_inches + weight_lbs
print(f"If I add {age}, {height_inches}, and {weight_lbs} I get {total}.")