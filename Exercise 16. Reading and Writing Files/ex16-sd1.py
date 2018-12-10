# Exercise 16. Reading and Writing Files - Study Drills 1

from sys import argv

script, filename = argv

print("Opening the file...")
target = open(filename, 'r')

print(f"The contents of {filename} are: \n{target.read()}")
target.close()