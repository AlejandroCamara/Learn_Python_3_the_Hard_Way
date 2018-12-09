# Exercise 06. Strings and Text - Study Drills.

# Variable
types_of_people = 10
# Variable x storing the formatted string
x = f"There are {types_of_people} types of people."

# String variables
binary = "binary"
do_not = "don't"

# Variable y storing the formatted string
# ************** String-ception **************
y = f"Those who know {binary} and those who {do_not}."

# Print string variables
print(x)
print(y)

# ************** String-ception **************
print(f"I said: {x}")

# ************** String-ception **************
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Format joke_evaluation replacing hilarious value in {} position.
print(joke_evaluation.format(hilarious))

# String variables
w = "This is the left side of ..."
e = "a string with a right side."

# Print w and e strings concatenation 
print(w + e)
