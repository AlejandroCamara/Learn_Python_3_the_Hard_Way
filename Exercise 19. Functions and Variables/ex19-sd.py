# Exercise 19. Functions and Variables - Study Drills

# Define sum_numbers function that receives two numbers and prints the sum of them
def sum_numbers(x, y):
    print(f"The sum of {x} + {y} is {x + y}") 

# Define cheese_and_crackers function that receives two parameters and print them
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# Call cheese_and_crackers with cheese_count = 20 and boxes_of_crackers = 30
print("We cant just give the function numbers directly:")
cheese_and_crackers(20, 30)

# Call cheese_and_crackers with cheese_count = 10 and boxes_of_crackers = 50
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call cheese_and_crackers with cheese_count = (10 + 20) and boxes_of_crackers = (5 + 6)
print("We van even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# Call cheese_and_crackers with cheese_count = (10 + 100) and boxes_of_crackers = (50 + 1000)
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Call #01 to sum_numbers
sum_numbers(1, 2)

# Call #02 to sum_numbers
sum_numbers(3 - 1, 2 * 16)

# Call #03 to sum_numbers
sum_numbers(100000, 2 / 2)

# Call #04 to sum_numbers
x = 14
y = 16
sum_numbers(x, y)

# Call #05 to sum_numbers
sum_numbers(x * x,  y * y)

# Call #06 to sum_numbers
sum_numbers(x * y, x * y)

# Call #07 to sum_numbers
sum_numbers(x / y, y / x)

# Call #08 to sum_numbers
sum_numbers(x + 150, y - 10)

# Call #09 to sum_numbers
sum_numbers(x + y - 25, x - y + 20)

# Call #10 to sum_numbers
sum_numbers( (x * y) % 5, (x - y) % 3)