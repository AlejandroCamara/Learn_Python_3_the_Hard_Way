# Exercise 34. Accessing Elements of Lists

def print_animal_sentences(animal, index):
    if index == 0:
        position = "1st"
    elif index == 1:
        position = "2nd"
    elif index == 2:
        position = "3rd"
    else:
        position = f"{index}th"

    print(f"The {position} animal is at {index} and is a {animal}.")
    print(f"The animal at {index} is the {position} and is a {animal}.\n")


animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

# 1. The animal at 1.
print_animal_sentences(animals[1], 1)

# 2. The third (3rd) animal.
print_animal_sentences(animals[2], 2)

# 3. The first (1st) animal.
print_animal_sentences(animals[0], 0)

# 4. The animal at 3.
print_animal_sentences(animals[3], 3)

# 5. The fifth (5th) animal.
print_animal_sentences(animals[4], 4)

# 6. The animal at 2.
print_animal_sentences(animals[2], 2)

# 7. The sixth (6th) animal.
print_animal_sentences(animals[5], 5)

# 8. The animal at 4.
print_animal_sentences(animals[4], 4)