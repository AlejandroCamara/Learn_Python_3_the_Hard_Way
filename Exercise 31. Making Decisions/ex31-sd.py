# Exercise 31. Making Decisions - Strudy Drills

def door1():
    print("There's a gigant bear here eating cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Goog job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bears runs away.")

def door2():
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

def door3():
    print("""That you are a slave Neo. That you, like everyone else, was born into bondage...
    kept inside a prison that you cannot smell, taste, or touch. A prison for your mind.
    
    Unfortunately, no one can be told what the Matrix is. You have to see it for yourself.

    You take the blue pill and the story ends. You wake in your bed and believe whatever you want to believe.
    You take the read pill and stay in Wonderland and I show you how deep the rabbit-hole goes.

    Remember that all I am offering is the thruth. Nothing more.
    """)

    pill = input("> ")

    if pill.lower() == "blue":
        print("Open your mind: https://www.youtube.com/watch?v=m8e-FF8MsqU")
    else:
        print("You wake up and continue doing you Python exercises.")




print("""You enter a dark room with three doors.
Do you go through door #1, door #2 or door #3?""")

door = input("> ")

if door == "1":
    door1()
    
elif door == "2":
    door2()

elif door == "3":
    door3()

else:
    print("You stumble around and fall on a knife and die. Good job!")