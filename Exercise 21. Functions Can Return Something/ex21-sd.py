# Exercise 21. Functions Can Return Something - Study Drills

def add(a ,b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
    
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b
    
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

# My own function
def square(x):
    print(f"CREATING THE SQUARE OF {x}")
    return x ** 2

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# (age + ( height - (weight * (iq / 2))))
what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")

print("Testing the square function.")
print(f"2 * 2 = {square(2)}")
print(f"12 * 12 = {square(12)}")

print("My own formula is: a^2 + 2ab + b^2")
a = 4
b = 12
by_hand = (a ** 2) + (2*a*b) + (b ** 2)
by_functions = add(square(a), add(multiply(2, multiply(a, b)), square(b)))
print(f"When a = {a} and b = {b}, then a^2 + 2ab + b^2 equals:")
print(f"By hand = {by_hand}\nBy functions = {by_functions}")
