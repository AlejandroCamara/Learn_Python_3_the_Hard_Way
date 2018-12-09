# Exercise 04: Variables and Names - Study Drills.

# Number of cars
cars = 100
# Car capacity. In Python 3, the cast to Float is done automatically.
space_in_a_car = 4
# Number of drivers
drivers = 30
# NUmber of passengers
passengers = 90
# Unused cars
cars_not_driven = cars - drivers
# Used cars
cars_driven = drivers
# Total number of passengers that can be driven
carpool_capacity = cars_driven * space_in_a_car
# Average number of passengers in a car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")