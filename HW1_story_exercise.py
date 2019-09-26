# let the user know what's going on
print ("Welcome to the Great Clairvoyant Scott's machine of fortunes")
print ("Answer the questions below to learn your future.")
yourName = raw_input("To begin this path into the unknown, tell me your name")
print ("aahh,") + ("a great name ")+ ("let's get started then")
print ("-----------------------------------")

# variables containing all of your story info
adjective1 = input("What adjective would you use to describe yourself?: ")
color1 = input("What is your favorite color?: ")
statement1  = input("What job would you never want to have: ")
location1 = input("Where would you never want to live?: ")
favoriteNumber = input("What is your favorite number?: ")
famousPerson1 = input("Who is a famous person you admire?: ")
famousPerson2 = input("Who is a famous person you despise?: ")
favFood = input("What is your favorite food?: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "I see great success in your life, you will have many " + adjective1 + " adventures."\
"But your friend, their future does not look so bright. I see them turning " + color1 + " and working as a " + statement1 + " in " + location1 " for eternity..." \
"Let me look back into my crystal ball...Ahh, I see that you will have " + favoriteNumber + " children. One of them will grow up to be as famous as " + famousPerson1 + ". " \
"Another... hmm, they will end up like " + famousPerson2 + " ... unfortunate soul." \
"It seems our time is coming to a close " + yourName + ". For my final prediction, I will summon the spirit of Forutna to gain insight into your destiny..." \
"Mmmmm, I see, yes... Fortuna is telling me that you will be eating " + favFood " for lunch... Thank you " + yourName + " Now that will be $1,000 dollars, I accept cash and all major credit card brands.)"\



# finally we print the story
print (story)
