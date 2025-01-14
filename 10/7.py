# More strings and text

x = "There are %d types of people." % 10
# below we are setting the words equal to the word you want
binary = "binary"
doNot = "don't"
# below we are putting our words into code (%s) is used for words
y = "Those who know %s and those who %s" % (binary, doNot)
# below we made it to where we can just type x and the word we want will type out
print(x)
print(y)
# below we are using the x and y to fill in the words we don't want to type
print("I said: %r.:" % x)
print("I also said: '%s'." % y)
# below we are setting the words we want to use equal to the words we really want to be typed
hilarious = True
# we made a joke
jokeEvaluation = "Isn't that joke so funny?! %r"
print(jokeEvaluation % hilarious)
# below we are using w and e to equal it to the words we want to be typed out
w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

# More printing fun
# we are now making a story
print("Mary had a little lamb.")
# below we made the % equal to the word "snow" so that we use the % instead of typing out the word
print("It's fleece was white as %s." % 'snow')
print("and everywhere that Mary went.")
# below we have it made where the "." will be multiplied by 10
print("." * 10)
# below we have made it where the word cheese burger will be spelled out by each letter instead of all together
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "b"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# below we have put the word cheese and teh word burger together by adding the word we set them equal to all together
print(end1 + end2 + end3 + end4 + end5 + end6,)
print(end7 + end8 + end9 + end10 + end11 + end12)
print("Cheese burger")


# But wait! There's more:
formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter %(True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
# why do I use %r instead of %s in the above example?
# the %r prints everything

# which should I use on a regular basis?

# why does %r sometimes only give me single quotes around things?

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApril\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Her are the months: ", months)

print("""
There's something going on here.
With the three double-quotes
We'll be able to type as we like.
Even 4 lines if we want, or 5, or 6.
""")

print("Here are the months: %r" % months)
print("Here are the months: %s" % months)

# escape sequences redux
tabbyCat = "\tI'm tabbed in."
persianCat = "I'm split\non a line."
backslashCat = "I'm \\ a \\ cat."
topCat = """
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t*Grass

"""

print(tabbyCat)
print(persianCat)
print(backslashCat)
print(topCat)

# Escape Seq            What it does?
# \\        1. this divides the symbol by two
# \'        2.it takes the slash away and leaves ' by itself
# \"        3.it takes the slash away and leaves the " by itself
# \a        4. makes a weird symbol
# \b        5. it makes everything disappear except for the 5
# \f        6. it made the same weird symbol
# \n        7. it made everything disappear except for the 7.
# \N{name}      8.
# \r
# \t
# \uxxxx
# \Uxxxxxxx
# \v
# \ooo
# \xhh

print("1. \\\\\\\\")
print("2. \'")
print("3. \"")
print("4. \a")
print("5.\b")
print("6.\f")
print("7.\n")


# What does the following code block do:
#  While True:
#     for i in ["/", "-", "|", "//", "|"]:
#        print("%s/r" % i, end='')

#  Can you use ''' instead of """?

age = input("How old are you?")
height = input("How tall are you?")
print("So, you are %r old and %r tall" % (age, height))

# Ask 4 more questions and handle those responses

favoriteClass = input("What's your favorite class?")
favoriteFood = input("What's your favorite food?")
favoriteAnimal = input("What's your favorite animal?")
favoriteColor = input("What's your favorite color?")
print("You like going to %r" % favoriteClass)
print("You like eating %r" % favoriteFood)
print("You like seeing your %r after school" % favoriteAnimal)
print("You like wearing %r everyday" % favoriteColor)

# My story

name = input("What is your name?")
siblings = input("How many siblings do you have?")
house = input("How big is your house?")
gpa = input("What does your gpa look like?")
height = input("How tall are you?")
crush = input("Who is your crush?")

print(" Hi! Your name is %r ? Oh that's pretty, my name is Brooklyn. " % name)
print("You have %r siblings? That is really cool, I hate having siblings they are so annoying! " % siblings)
print("Your house is %r? I would love to live in my dream house, so would you? Yes it would be nice but for now it's good to stick with your %r house. " % (house,house))
print("Dang! Your gpa is that %r? I am always worried about my gpa. It is always nice to see the gradebook when I get all good grades." % gpa)
print("I always have to look up at you, I feel very short compared to you, considering you are %r and I am only 5 feet." % height)
print("Earlier I saw you staring at that one dude . Who is he/she? Oh! I know %r, he/she is really nice but super weird. so...Good luck with that." % crush)
print(" Well, I guess I will see you tomorrow, it was really nice getting to know you bye %r" % name)
