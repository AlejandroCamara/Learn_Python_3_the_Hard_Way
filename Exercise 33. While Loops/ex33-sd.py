# Exercise 33. While Loops - Study Drills

def print_numbers(numbers):
    for num in numbers:
        print(num)

def add_numbers_for(limit, step):
    numbers = []
    for i in range(0, limit + 1, step):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print_numbers(numbers)

def add_numbers_while(limit, step):
    i = 0
    numbers = []
    while i < limit + 1:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += step
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    
    print_numbers(numbers)

add_numbers_while(10, 2)
print("**************************")
add_numbers_for(10, 2)
