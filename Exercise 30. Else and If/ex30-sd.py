# Exercise 30. Else and If - Study Drills

# Variable declaration and initialization
people = 24
cars = 13
trucks = 25

# More cars
if cars > people:
    print("We should take the cars.")
# Less cars
elif cars < people:
    print("We should not take the cars.")
# Equal cars and people
else:
    print("We can't decide.")

# More trucks
if trucks > cars:
    print("That's too many trucks.")
# Less trucks
elif trucks < cars:
    print("Maybe we could take the trucks.")
# Equal trucks and people
else:
    print("We still can't decide.")

# More people
if people > trucks:
    print("Alright, let's just take the trucks.")
# Equal or less people
else:
    print("Fine, let's stay home then.")

if (cars > people) and (people < trucks):
    print("There are a lot of vehicles.")
else:
    print("We should buy more vehicles.")

if (cars > people) and (cars > trucks):
    print("We have more cars than people or trucks.")
elif (trucks > people) and (trucks > cars):
    print("We have more trucks than people or cars.")
else:
    print("There a mess here.")
