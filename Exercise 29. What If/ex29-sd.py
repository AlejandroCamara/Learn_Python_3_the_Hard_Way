# Exercise 29. What If - Study Drills

people = 25
cats = 15
dogs = 10


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 15
cats += 10

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

if (people == dogs) and (people == cats):
    print("There is no difference in evolution.")

if (dogs < cats) and (people <= dogs):
    print("Dogs and people are in trouble.")

if (True and False) or (not False and True):
    print("True")