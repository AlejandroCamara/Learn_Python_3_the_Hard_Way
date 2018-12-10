# Exercise 13. Parameters, Unpacking, Variables - Study Drills 3

from sys import argv
# read the WYSS section for how to run this
script, first_half = argv

second_half = input("Enter the second half of your phrase: ")
print(f"{first_half} {second_half}")