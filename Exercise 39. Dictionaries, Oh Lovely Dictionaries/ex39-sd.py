# Exercise 39. Dictionaries, Oh Lovely Dictionaries - Study Drills

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

# Erase the dictionary contents
states.clear()
cities.clear()

states = dict([("Ciudad de México", "CDMX"), 
                ("Chiapas", "Chis"), 
                ("Colima", "Col"), 
                ("Guerrero", "Gro"), 
                ("Hidalgo", "Hgo")])

print(str(states))

# Combine two dictionaries
missing_states = {"Jalisco": "Jal"}
states.update(missing_states)
print(str(states))

# Iterate from items
for key, value in states.items():
    print(f"The city {key} is abbreviated {value}")

# Create new dictionary with the keys in the first parameter, and the default value
cities = cities.fromkeys(states.values(), "City not registered")
print(str(cities))

cities_names = ["Tlalpan", "Tuxtla", "Colima", "Acapulco", "Pachuca", "Guadalajara"]

# Update the value associated to a key
for city, name in zip(cities.keys(), cities_names):
    cities[city] = name

print(str(cities))
