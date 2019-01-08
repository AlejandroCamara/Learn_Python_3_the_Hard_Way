# Exercise 48. Advanced User Input with Study Drills

lexicon = {'direction' : ["north", "south", "east", "west", "down", "up", "left", "right", "back"],
            'verb': ["go", "stop", "kill", "eat"],
            'stop': ["the", "in", "of", "from", "at", "it"],
            'noun': ["door", "bear", "princess", "cabinet"]}

# Identify which type of word is
def search_lexicon(word):
    for key in lexicon.keys():  # Search in each dictionary entry
        if (word.lower() in lexicon[key]):
            return (key, word)

    return ('error', word) 

def scan(user_input):
    # Normalize input
    words = user_input.split(' ')
    result = []

    for word in words:
        if (word.isnumeric()):  # Check if the input is a number
            result.append(('number', int(word)))
        else:
            result.append(search_lexicon(word))
    return result