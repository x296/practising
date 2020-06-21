import random

daysBank = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
placesBank = ["castle", "forest", "mountains", "shopping center", "cave", "factory", "cardboard"]
figuresBank = ["King", "Knight", "Dwarf", "Gummy bear", "Fox", "Robot", "Whale", "Dragon", "Meteorite", "Ant", "Wind"]
verbsBank = ["drink", "eat", "sleep", "shout", "watch", "clap", "snork", "dance", "walk", "sit", "play", "read", "write"]
adjectivesBank = ["preatty", "ugly", "awful", "sweet", "dengerous", "stupid", "slim", "strong", "smart", "fat", "dumb"]

print("Welcome to a simple Story Generator!\n")
print("Please, take a moment for type some words and enjoy your masterpiece ;)")

userDay = str(input("Type a weekday (leave empty for random): "))
if userDay == "":
	userDay = daysBank[random.randrange(len(daysBank))]

userPlace = str(input("Type a place (leave empty for random): "))
if userPlace == "":
	userPlace = placesBank[random.randrange(len(placesBank))]

userCharacter = str(input("Type a character (leave empty for random): "))
if userCharacter == "":
	userCharacter = figuresBank[random.randrange(len(figuresBank))]

userCreature = str(input("Type a creature (leave empty for random): "))
if userCreature == "":
	userCreature = figuresBank[random.randrange(len(figuresBank))]

userVerb1 = str(input("Type a verb (leave empty for random): "))
if userVerb1 == "":
	userVerb1 = verbsBank[random.randrange(len(verbsBank))]

userVerb2 = str(input("Type another verb (leave empty for random): "))
if userVerb2 == "":
	userVerb2 = verbsBank[random.randrange(len(verbsBank))]

userVerb3 = str(input("Type the last verb (leave empty for random): "))
if userVerb3 == "":
	userVerb3 = verbsBank[random.randrange(len(verbsBank))]

userAdjective1 = str(input("Type an adjective (leave empty for random): "))
if userAdjective1 == "":
	userAdjective1 = adjectivesBank[random.randrange(len(adjectivesBank))]

userAdjective2 = str(input("Type another adjective (leave empty for random): "))
if userAdjective2 == "":
	userAdjective2 = adjectivesBank[random.randrange(len(adjectivesBank))]


storySchema = '''Story\n
It will be a short story. One day, maybe it was {day} or the other day, I can’t remember, 
a {character} was {verb1}ing in the {place}. It was completely normal day, and nothing foretold anything special. 
Suddenly, a/an {adjective1} {creature} fall down from the sky and hit the ground right next to {character}. 
{character} yelled and the {creature} starts {verb3}ing. When everything started to be very {adjective2} 
you woke up and wondering how it is possible, that {adjective1} {character} could {verb2} {creature}. 
Or maybe you totally mixed everything..?'''.format(day = userDay, place = userPlace, character = userCharacter, creature = userCreature, verb1 = userVerb1, verb2 = userVerb2, verb3 = userVerb3, adjective1 = userAdjective1, adjective2 = userAdjective2)

print(storySchema)
