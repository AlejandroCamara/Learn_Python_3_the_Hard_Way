# Exercise 34. Accessing Elements of Lists - Study Drills

def print_element_sentences(element, index, name):
    if index == 0:
        position = "1st"
    elif index == 1:
        position = "2nd"
    elif index == 2:
        position = "3rd"
    else:
        position = f"{index}th"

    print(f"The {position} {name} is at {index} and is a {element}.")
    print(f"The {name} at {index} is the {position} and is a {element}.\n")

def iterate_elements(arr, name):
    for i in range(0, len(arr)):
        print_element_sentences(arr[i], i, name)


animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
programming_languages = ["Python", "C", "C++", "C#", "Java", "Ruby", "PHP", "Clojure", "Lisp", "FORTRAN", "JavaScript"]
movies = ["Lord of the Rings", "Star Wars", "Matrix", "Kill Bill", "Back to the Future", "Spiderman"]

iterate_elements(animals, "animal")
iterate_elements(programming_languages, "programming language")
iterate_elements(movies, "movie")

