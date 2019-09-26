# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["sword"],
    "friends" : [],
    "location" : "start"
}


rooms = {
    "room1" : "mystic",
    "room2" : "throne room",
    "room3" : "treasure room"
}


import random # random numbers
import sys # system stuff for exiting


def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))


    if result <= difficulty:
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty)


    return result





def gameOver():
    print ("-------------------------------")
    print ("Congrats you successfully obtained the teasure")
    print ("name: " + player["name"])
    print ("score: " + str(player["score"])
    return



def skelotonRoom():
    print ("You travel through a dark and dicrepit tunnel, filled with human skeletons")
    print ("It seems that many don't make it out of the temple of ojibogi alive.")
    input("press enter >")


   
    print ("You enter into what seems to be a throne room")
    print ("A skeleton sits on the throne with his crown still on")
    print ("...all of a sudden the skelton stands! ")
    input("press enter >")
    
    print ("What do you do next!?.")


    if ("gem" in player["items"]):
        print ("options: [ fight , try to reason with him , run ]")
  
    pcmd = input(">")


    # option 1: talk to the skeloton
    elif (pcmd == "try to reason with him"):
        print ("you approach the throne and talk to the skeleton king!")
        print ("Let's roll a dice to see what happens next!")
        input("press enter to roll >")


        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20


        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("The skelton admires your non violent ways! He presents you the treasure!!.")
            player["score"] += 50
        else:
            print ("The skelton draws his sword an strikes you down")
            gameOver() # game over


    # option 2: fight the skeloton
    elif (pcmd == "fight"):
        print ("You draw your sword and run at the skeloton king!")
        print ("the skeloton king draws his sword")
        print ("Let's roll a dice to see what happens next!")
        input("press enter to roll >")


        difficulty = 10
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20


        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("You jump and stike down the skeloton king! You are victorious")
            print ("You then break into the treasure room and take what is rightfully yours")
            player["score"] += 10000
        else:
            print ("OH NO! The Skelton king strikes you down. Game over.")
            gameOver() # game over        



def mysticEncounter():
    print ("You approach the mystic, he presents 2 rocks.")
    print ("One is gold and one is black.")
  
    if (("sword" in player["items"]):
        print ("Your options: [ black, gold ]")

    pcmd = input(">") # user input


    # Player option 1 - die
    if (pcmd == "black"):
        print ("The mystic snaps his fingers and poisonous snakes pop up from the floor. and you DIE. click enter to restart" )
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!

    # Player option 2 - survive
    elif (pcmd == "gold"):
        print ("You have chosen wisely, says the mystic. He opens a secret door and you continue.")
        raw_input("press enter >")
        skelotonRoom() # path 1




    # exiting / catching errors and crazy inputs
    elif (pcmd == "exit"):
        print ("you exit.")
        return # exit the application
        


def introStory():
    # let's introduce them to our world
    print ("Good to see you again! What is your name?")
    player["name"] = input("Please enter your name >")


    # intro story, quick and dirty (think star wars style)
    print ("Welcome to the indiana jones temple adventure " + player["name"] + "!")
    print ("Do you think you have what it takes to obtain the mystical relic of ojibogi")
    print ("Here is your story....")
    print ("You've traveled for 5 days through the rain forest and approach the temple of ojibogi.")
    print ("You see there are 2 paths, your guide says the path on the right is the safest path.")
    print ("Do you follow their direction>?")


    pcmd = input("please choose yes or no >")


    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You were smart to take your guides advice, you've avoided your imminent death, but you encounter a mystic ...")
        print ()
        input("press enter >")
        mysticEncounter()
    else:
        print ("OMG you've been struck down by a hidden blow dart and you die... restart your adventure.")
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!






# main! most programs start with this.
def main():
    print ("Indiana Jones Temple Adventure") # call the function to print an image
    introStory() # start the intro


main() # this is the first thing that happens