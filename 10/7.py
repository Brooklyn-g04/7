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
