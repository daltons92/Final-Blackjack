'''
A class that represents the player.
'''

class Player():

    global mScore # Tracks players score
    global mCardsValue # Tracks players card value (ex: 21)

    # Constructor which will load data from sava.txt if available
    def __init__(self):
        global mCardsValue, mScore
        mScore = 0 # Tracks players score
        mCardsValue = 0 # Tracks players hands/cards value
        try: # Load previous score/save data if there is any
            in_file = open("save.txt", "r")
            loadedScore = in_file.readline()
            if loadedScore == "": # If the file is empty, set score to 0
                loadedScore = 0
            mScore = int(loadedScore)
            print(f"Old save data with a score of {mScore} was loaded.")
            in_file.close()
        except FileNotFoundError: # If theres no save data, create save.txt
            print("Save file was not found, creating save.txt.")
            out_file = open("save.txt", "w")
            out_file.write("0")
            out_file.close()

    # Saves the player's score to a text file for future use
    def saveGame(self):
        try:
            out_file = open("save.txt", "w")
            out_file.write(f"{mScore}")
            out_file.close()
        except FileNotFoundError: # If theres no save data, create save.txt
            print("Save file was not found, creating save.txt.")
            out_file = open("save.txt", "w")
            out_file.write(f"{mScore}")
            out_file.close()

    # Changes players score
    def addCardToHand(self, card):
        global mCardsValue
        if card[1] in (11, 12, 13): # If a jack/queen/king is drawn add a value of 10
            mCardsValue += 10
        elif card[1] == 14: # Else if a Ace is drawn add 1 or 11 depending on which is more beneficial
            if mCardsValue < 10:
                mCardsValue += 11
            else:
                mCardsValue += 1
        else: # Else just add the cards face value
            mCardsValue += card[1]
        print(f"You drew a {card[1]}, your totals hand value is now {mCardsValue}")

    # Returns player's mCardValue
    def getCardsValue(self):
        return mCardsValue
    
    # Set player's mCardValue
    def setCardsValue(self, value):
        global mCardsValue
        mCardsValue = value

    # Get player's score
    def getScore(self):
        global mScore
        return mScore

    # Change player's score
    def changeScore(self, value):
        global mScore
        mScore += value