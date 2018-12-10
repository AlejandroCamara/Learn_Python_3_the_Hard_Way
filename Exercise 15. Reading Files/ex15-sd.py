# Exercise 15. Reading Files - Study Drills

# Import argv from sys module
from sys import argv
# Unpack arguments into variables
script, filename = argv

# Open a file an store the file object into txt
txt = open(filename)

# Print file contents with read() function
print(f"Here's yout file {filename}:")
print(txt.read())

# Close txt file
txt.close()

# Ask the user to enter the filename while the script is running
print("Type the filename again:")
file_again = input('> ')

# Open file 
txt_again = open(file_again)

# Print file contents
print(txt_again.read())

# Close txt_again file
txt_again.close()
