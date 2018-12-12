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
    ['f""', "Formatted String", "Allows to use variables and calculated values in strings"],
    ["end=''", "print() end parameter", "Sets the last character of a printed string"],
    [".format()", "String Format Function", "Replaces the placeholders with the parameters"],
    ["input()", "Input Function", "Prompts the user to enter a value"],
    ["open()", "File Open Function", "Opens the file passed as parameter"],
    [".read()", "File Read Function", "Stores all the contents of the file"],
    [".write()", "File Write Function", "Replaces the contents of the file with the parameter value"],
    [".close()", "File Close Function", "Saves and closes the file"],
    [".seek()", "File Seek Function", "Sets the file head to the specified byte"],
    [".readline()", "File Read Line Function", "Buffers the bytes until a new line character is found"],
    ["from", "-", "Indicates a Python Module that will be required"],
    ["import", "-", "Imports a module completely or a specific function or variable"],
    ["sys", "System-specific parameters and functions", "Provides access to some variables and functions used by the interpreter"],
    ["argv", "Arguments List", "Contains the parameters passed when the script is executed"],
    ["os.path", "Common pathname manipulations", "Allows to interact with the OS file system"],
    ["exists()", "os.path Exists Function", "Checks if a path is available in the file system"],
    ["*args", "-", "List of parameters of variable length"],
    ["\\\\", "Backslash", "Prints a \\"],
    ["\\\'", "Single Quote", "Prints a \'"],
    ["\\\"", "Double Quote", "Prints a \""],
    ["\\t", "Horizontal tab", "Prints a \ t"],
    ["\\n", "New Line", "Prints a new line "],
    ["\\a", "ASCII bell", "Prints a \a"],
    ["\\b", "ASCII backspace", "Prints a \b"],
    ["\\f", "ASCII formfeed", "Prints a \f"],
    ["\\\\", "Backslash", "Prints a \\"],
    ["\\r", "Carriage return", "Return the String head to the beginning of the line"],
    ["\\uxxx", "16 bit Character", "Prints a \\"],
    ["\\Uxxxxxxxx", "32 bit Character", "Prints a \\"],
    ["\\v", "Vertical Tab", "Prints a \v"],
    ["\\ooo", "Octal Character", "Prints an octal number"],
    ["\\xhh", "Hexadecimal Character", "Prints a hexadecimal number"],
]

print('+' + 25 * '-' + '+' + 40 * '-' + '+' + 80 * '-' + '+')
print('| {:^23s} | {:^38s} | {:^78s} |'.format(
            "SYMBOL OR WORD", "NAME", "MEANING/USAGE"))
for symbol in symbols_and_words:
    print('-' * 149)
    print('| {:^23s} | {:^38s} | {:^78s} |'.format(
            symbol[0], symbol[1], symbol[2]))
    
print('+' + 25 * '-' + '+' + 40 * '-' + '+' + 80 * '-' + '+')