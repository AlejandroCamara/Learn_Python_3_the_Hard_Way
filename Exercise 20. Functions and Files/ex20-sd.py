# Exercise 20. Functions and Files - Study Drills

# Import argv variable of sys module
from sys import argv

# Unpack the arguments received from console
script, input_file = argv

# Function that prints all the file contents
def print_all(f):
    print(f.read())

# Function that sets the 'file head' at the beginning of the file
def rewind(f):
    f.seek(0)

# Function that prints the next line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# Openning the file
current_file = open(input_file)

# Call to print all the file
print("First let's print the whole file:\n")
print_all(current_file)

# Call to reset the 'file head' to the first line
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# Call to print one line
print("Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file)

# Call to print one line
current_line += 1   # 2
print_a_line(current_line, current_file)

# Call to print one line
current_line += 1   # 3
print_a_line(current_line, current_file)