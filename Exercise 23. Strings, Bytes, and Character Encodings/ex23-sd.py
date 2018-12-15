# Exercise 23. Strings, Bytes, and Character Encodings - Study Drills
# Download command:
# powershell -command "& { iwr https://learnpythonthehardway.org/python3/languages.txt -OutFile languages.txt }"
# DBES - Decode Bytes, Encode Strings
# bytes.decode() => String
# string.encode() => bytes

import sys
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(bytes_line, encoding, errors):
    cooked_string = bytes_line.decode(encoding, errors = errors)
    print(bytes_line, "<===>", cooked_string.strip())

# Open the file in read and binary mode
languages = open("languages.txt", 'rb')

main(languages, encoding, error)

