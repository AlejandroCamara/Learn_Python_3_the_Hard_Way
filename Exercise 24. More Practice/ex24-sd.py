# Exercise 24. More Practice - Study Drills

# One line strings printing
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# Multiline string with tab and new line escape characters
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")

# Variable with the value of the math operation
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# Function that receives a number as parameter
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # Return the three calculated values
    return jelly_beans, jars, crates

# Main code

start_point = 10000
# Unpacking the returned values by secret_formula
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
# Use String format function
print("With a starting point of: {}".format(start_point))
# it's just like with and f"" string
# Use a formatted string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# Unpack variable number of values from formula
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
