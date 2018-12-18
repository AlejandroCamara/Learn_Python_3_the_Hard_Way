# Exercise 42. Is-A, Has-A, Objects, and Classes - Study Drills

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    
    def __init__(self, group):
        self.group = group

    def make_sound(self, animal="animal", sound="Muted"):
        print(f"The {animal} sounds {sound}")

## Dog is-an Animal
class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__("Mammals")
        ##  Dog has-a name
        self.name = name

    def make_sound(self):
        super(Dog, self).make_sound("Dog", "Guau Guau!!!")

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__("Mammals")
        ## Cat has-a name
        self.name = name

    def make_sound(self):
        super(Cat, self).make_sound("Cat", "Miau Miau!!!")

## Person is-an object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
    
    def say_my_name(self):
        print(f"""- Say my name...
        \r- {self.name}
        \r- You're Goddamn right!""")

    def love_pet(self):
        print(f"You're so cute {self.pet.name}!!!!")

## Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name because is a Person. hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

    def quit_your_job(self, boss):
        print(f"""-Firetruck you {boss}.
        \r- What!?
        \r- Firetruck you and your eyebrows""")

## Fish is-an object
class Fish(Animal):
    def __init__(self, poisonous, eatable):
        super(Fish, self).__init__("Acuatic Vertebrates")
        self.poisonous = poisonous
        self.eatable = eatable

    def being_fished(self):
        if self.eatable:
            print("Good bye Nemo. Don't leave the choral.")
        else:
            print("I may die today, but you'll follow me.")


## Salmon is-a Fish
class Salmon(Fish):
    def __init__(self, recipe):
        super(Salmon, self).__init__(False, True)
        self.recipe = recipe
    
    def show_recipe(self):
        print(f"I am a delicious {self.recipe} salmon.")

## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self):
        super(Halibut, self).__init__(False, True)
    
    def do_something(self):
        print(f"I don't know about myself.")

## rover is-a Dog
print(f'\n{"*" * 10} ROVER {"*" * 10}')
rover = Dog("Rover")
rover.make_sound()

## stan is-a Cat
print(f'\n{"*" * 10} SATAN {"*" * 10}')
satan = Cat("Satan")
satan.make_sound()

## mary is-a Person
print(f'\n{"*" * 10} MARY {"*" * 10}')
mary = Person("Mary")
mary.say_my_name()

## mary has-a cat as pet
mary.pet = satan
mary.love_pet()

## frank is-an Employee
print(f'\n{"*" * 10} FRANK {"*" * 10}')
frank = Employee("Frank", 120000)
frank.say_my_name()
frank.quit_your_job(mary.name)

## frank has-a dog as pet
frank.pet = rover
frank.love_pet()

## flipper is-a Fish
print(f'\n{"*" * 10} FLIPPER {"*" * 10}')
flipper = Fish(True, False)
flipper.being_fished()

## crouse is-a Salmon
print(f'\n{"*" * 10} CROUSE {"*" * 10}')
crouse = Salmon("Grilled")
crouse.being_fished()
crouse.show_recipe()

## harry is-a Halibut
print(f'\n{"*" * 10} HALIBUT {"*" * 10}')
harry = Halibut()
harry.being_fished()
harry.do_something()