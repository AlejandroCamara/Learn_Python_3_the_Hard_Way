# Exercise 22. What Do You Know So Far
print(f"{'*' * 10} WORK IN PROGRESS {'*' * 10}\n")
symbols_and_words = [
    ["'", "Single Quote", "String Delimiter"],
    ['\"', "Double Quote", "String Delimiter"],
    ['"""', "Triple Double Quote", "Multiline String Delimiter"],
    ['#', "Hashtag/Octothorpe", "One line Comment Delimiter"],
    ["'''", "Triple Single Quote", "Multiline Comment Delimiter"],
    ["%", "Modulo/Percentage", "Returns the reminder of a division"],
    ["+", "Plus", "Adds two numbers"],
    ["-", "Minus", "Substracts two numbers"],
    ["*", "Asterisk", "Multiplies two numbers"],
    ["/", "Forward Slash", "Divides two numbers"],
    ["=", "Assignation", "Assigns a value to a variable"],
    ["==", "Comparison", "Compares two values"],
    [">", "Greater than", "Checks if the left value is greater than the right value"],
    ["<", "Less than", "Checks if the left value is lower than the right value"],
    [">=", "Greater than or equal", "Checks if the left value is greater or equal than the right value"],
    ["<=", "Less than or equal", "Checks if the left value is lower or equal than the right value"],
    ["{}", "Curly Brackets", "Placeholder for formatted strings"],

]
print('+' + 25 * '-' + '+' + 40 * '-' + '+' + 80 * '-' + '+')
print('| {:^23s} | {:^38s} | {:^78s} |'.format(
            "SYMBOL OR WORD", "NAME", "MEANING/USAGE"))
for symbol in symbols_and_words:
    print('-' * 153)
    print('| {:^23s} | {:^38s} | {:^78s} |'.format(
            symbol[0], symbol[1], symbol[2]))
    
print('+' + 25 * '-' + '+' + 40 * '-' + '+' + 80 * '-' + '+')