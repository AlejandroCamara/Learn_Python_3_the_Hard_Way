# Exercise 08. Printing, Printing - Study Drills

# String variable 
formatter = "{} {} {} {}"

# Replaces the curly brackets with the parameters given to the format function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Replaces "{}" with "{} {} {} {}", i.e. formatter string value
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))