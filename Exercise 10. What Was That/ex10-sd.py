# Exercise 10. What Was That? - Study Drills

# String with tab escape character
tabby_cat = "{}I'm tabbed in.".format('\t')
# String with new line escape character
persian_cat = "I'm split{}on a line.".format('\n')
# String with backslash character
backslash_cat = "I'm {} a {} cat.".format('\\', '\\')

# Multiline string
fat_cat = '''
I'll do a list:
{}* Cat food
{}* Fishies
{}* Catnip{}{}* Grass
'''.format('\t', '\t', '\t', '\n', '\t')

# Print strings
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)