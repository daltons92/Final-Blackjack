import tkinter as tk
import time
from card_deck import CardDeck
from player import Player
from dealer import Dealer

''' 
A game of Blackjack
By Dalton Shanholtz
'''

WAGER_AMOUNT = 5 # Amount of default point to wager each round
ROUND_OVER = False 
# Variable for tracking the player and dealers hand value. Interestingly, this is global to prevent Tk from drawing a 'ghost/after effect' text
STATS_OF_ROUND_TEXT = None

# Resets the GUI cards (rectangles/text) after each round of blackjack
def resetCards():
    # We move the cards out of the windows view to prevent TK from drawing old images after rect/textCardsForPlayer.clear()
    # Perhaps not the best solution.
    for text in textCardsForPlayer: 
            canvas.move(text, 400, 1000) 
    for rect in rectCardsForPlayer: 
            canvas.move(rect, 400, 1000)
    textCardsForPlayer.clear()
    rectCardsForPlayer.clear()
    for text in textCardsForDealer: 
            canvas.move(text, 400, 1000) 
    for rect in rectCardsForDealer: 
            canvas.move(rect, 400, 1000)
    textCardsForDealer.clear()
    rectCardsForDealer.clear()

# Handles all logic for "Hit me" button
def hitMeBtnClickHandler():
    global ROUND_OVER, STATS_OF_ROUND_TEXT

    # Checks to see if the round is over, if the round is over we reset the cards before drawing the next
    if(ROUND_OVER):
         resetCards()
         ROUND_OVER = False

    # Draw a card from gameDeck and add it to the player's hand
    cardDrawn = gameDeck.drawCard()
    player.addCardToHand(cardDrawn)

    # Create a Rect and Text object to represent the Card.
    newCardRect = canvas.create_rectangle(500, 50, 550, 125, fill="white")
    if(cardDrawn[1] == 11):
        newCardText = canvas.create_text(525, 70, text=f"{cardDrawn[0]}\n  JACK", font=("Times", 8), fill="red", anchor="center", angle=0)
    elif(cardDrawn[1] == 12):
        newCardText = canvas.create_text(525, 70, text=f"{cardDrawn[0]}\n  QUEEN", font=("Times", 8), fill="red", anchor="center", angle=0)
    elif(cardDrawn[1] == 13):
        newCardText = canvas.create_text(525, 70, text=f"{cardDrawn[0]}\n  KING", font=("Times", 8), fill="red", anchor="center", angle=0)
    elif(cardDrawn[1] == 14):
        newCardText = canvas.create_text(525, 70, text=f"{cardDrawn[0]}\n  ACE", font=("Times", 8), fill="red", anchor="center", angle=0)
    else:
        newCardText = canvas.create_text(525, 70, text=f"{cardDrawn[0]}\n  {cardDrawn[1]}", font=("Times", 8), fill="red", anchor="center", angle=0)

    # Add the Rect and Text object for the card to lists for future use
    rectCardsForPlayer.append(newCardRect)
    textCardsForPlayer.append(newCardText)

    #statsOfRoundText is used to display the players and dealers hand value for the current round
    #statsOfRoundText = canvas.create_text(225, 320, text=f"aaaaaaaa", font=("Times", 18), fill="Blue", anchor="center", angle=0)
    if(STATS_OF_ROUND_TEXT != None): 
        canvas.move(STATS_OF_ROUND_TEXT, 1400, 12000)
    STATS_OF_ROUND_TEXT = canvas.create_text(225, 380, text=f"Player's Hand: {player.getCardsValue()}\nDealer's Hand: {dealer.getCardsValue()}\nScore: {player.getScore()}\nWager: {WAGER_AMOUNT}", font=("Times", 20), fill="Blue", anchor="center", angle=0)

    # Game Logic to calculate if we have lost or not
    renderCards()
    if(player.getCardsValue() > 21):
        player.changeScore(-WAGER_AMOUNT)
        print(f"You have busted, your score is now {player.getScore()}")
        player.setCardsValue(0)
        player.saveGame()
        ROUND_OVER = True
    elif(player.getCardsValue() == 21):
        player.changeScore(WAGER_AMOUNT)
        print(f"You hit blackjack, your score is now {player.getScore()}")
        player.setCardsValue(0)
        player.saveGame()
        ROUND_OVER = True

def increaseWagerBtnClickHandler(): # Click handler for icrementing the wager amount
    global WAGER_AMOUNT, STATS_OF_ROUND_TEXT
    WAGER_AMOUNT += 1
    if(STATS_OF_ROUND_TEXT != None): 
        canvas.move(STATS_OF_ROUND_TEXT, 1400, 12000)
    STATS_OF_ROUND_TEXT = canvas.create_text(225, 380, text=f"Player's Hand: {player.getCardsValue()}\nDealer's Hand: {dealer.getCardsValue()}\nScore: {player.getScore()}\nWager: {WAGER_AMOUNT}", font=("Times", 20), fill="Blue", anchor="center", angle=0)


def decreaseWagerBtnClickHandler(): # Click handler for decrementing the wager amount
    global WAGER_AMOUNT, STATS_OF_ROUND_TEXT
    WAGER_AMOUNT -= 1
    if(STATS_OF_ROUND_TEXT != None): 
        canvas.move(STATS_OF_ROUND_TEXT, 1400, 12000)
    STATS_OF_ROUND_TEXT = canvas.create_text(225, 380, text=f"Player's Hand: {player.getCardsValue()}\nDealer's Hand: {dealer.getCardsValue()}\nScore: {player.getScore()}\nWager: {WAGER_AMOUNT}", font=("Times", 20), fill="Blue", anchor="center", angle=0)


# Handles all logic for "Hold" button
def holdBtnClickHandler():
    global ROUND_OVER, STATS_OF_ROUND_TEXT

    # Checks to see if the round is over, if the round is over we reset the cards before drawing the next
    if(ROUND_OVER):
         resetCards()
         ROUND_OVER = False

    # Game Logic to see if we have won
    while (dealer.getCardsValue() < 21):
        cardDrawn = gameDeck.drawCard()
        dealer.addCardToHand(cardDrawn)
    
        # Create a Rect and Text object to represent the Card.
        newCardRect = canvas.create_rectangle(300, 200, 350, 275, fill="white")
        
        # Assign various values of cards drawn depending on whats drawn
        if(cardDrawn[1] == 11):
            newCardText = canvas.create_text(325, 220, text=f"{cardDrawn[0]}\n  JACK", font=("Times", 8), fill="red", anchor="center", angle=0)
        elif(cardDrawn[1] == 12):
            newCardText = canvas.create_text(325, 220, text=f"{cardDrawn[0]}\n  QUEEN", font=("Times", 8), fill="red", anchor="center", angle=0)
        elif(cardDrawn[1] == 13):
            newCardText = canvas.create_text(325, 220, text=f"{cardDrawn[0]}\n  KING", font=("Times", 8), fill="red", anchor="center", angle=0)
        elif(cardDrawn[1] == 14):
            newCardText = canvas.create_text(325, 220, text=f"{cardDrawn[0]}\n  ACE", font=("Times", 8), fill="red", anchor="center", angle=0)
        else:
            newCardText = canvas.create_text(325, 220, text=f"{cardDrawn[0]}\n  {cardDrawn[1]}", font=("Times", 8), fill="red", anchor="center", angle=0)
        
    
        # Add the Rect and Text object for the card to lists for future use
        rectCardsForDealer.append(newCardRect)
        textCardsForDealer.append(newCardText)
        # Check to see the outcome of the game
        if(dealer.getCardsValue() > 21):
            player.changeScore(WAGER_AMOUNT)
            print(f"The dealer has busted, you now have a score of {player.getScore()}.")
            ROUND_OVER = True
            break
        elif(dealer.getCardsValue() == 21):
            player.changeScore(-WAGER_AMOUNT)
            print(f"The dealer has blackjack and wins. You now have a score of {player.getScore()}")
            ROUND_OVER = True
            break
        elif(dealer.getCardsValue() >= player.getCardsValue()):
            player.changeScore(-WAGER_AMOUNT)
            print(f"You lost with a score of {player.getCardsValue()} against {dealer.getCardsValue()}. You now have a score of {player.getScore()}")
            ROUND_OVER = True
            break

    # This handles displaying basic UI elements for the player
    if(STATS_OF_ROUND_TEXT != None): 
        canvas.move(STATS_OF_ROUND_TEXT, 1400, 12000)
    STATS_OF_ROUND_TEXT = canvas.create_text(225, 380, text=f"Player's Hand: {player.getCardsValue()}\nDealer's Hand: {dealer.getCardsValue()}\nScore: {player.getScore()}", font=("Times", 20), fill="Blue", anchor="center", angle=0)

    renderCards()
        

    #resetCards()
    player.saveGame()
    player.setCardsValue(0)
    dealer.setCardsValue(0)



def renderCards(): # Responsible for animating cards to the left, when a new card is drawn
    for i in range(len(rectCardsForPlayer)):
        activeRect = rectCardsForPlayer[i] # Graphical rectangle to represent the shape of card
        activeText = textCardsForPlayer[i] # Text value to represent the value of a card
        if canvas.coords(activeRect)[2] > (i + 1) * 90: # If Card/coords are greater then a certain x value ..
            coordsToMove = (canvas.coords(activeRect)[2] - (i + 1) * 90 ) / 30 # Calculate coords to move 
            if coordsToMove < 0.5: # If cords to move is under 0.5, stablize it at 0.5 to not be too slow
                coordsToMove = 0.5
            canvas.move(activeRect, -coordsToMove, 0)
            canvas.move(activeText, -coordsToMove, 0)
            root.after(10, renderCards) # Loop back after 10ms

    for i in range(len(rectCardsForDealer)):
            activeRect = rectCardsForDealer[i] # Graphical rectangle to represent the shape of card
            activeText = textCardsForDealer[i] # Text value to represent the value of a card
            if canvas.coords(activeRect)[2] > (i + 1) * 90: # If Card/coords are greater then a certain x value ..
                coordsToMove = (canvas.coords(activeRect)[2] - (i + 1) * 90 ) / 30 # Calculate coords to move 
                if coordsToMove < 0.5: # If cords to move is under 0.5, stablize it at 0.5 to not be too slow
                    coordsToMove = 0.5
                canvas.move(activeRect, -coordsToMove, 0)
                canvas.move(activeText, -coordsToMove, 0)
                root.after(10, renderCards) # Loop back after 10ms 

playersHand = []

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Blackjack")

    canvas = tk.Canvas(root, width=500, height=500, bg="grey")
    canvas.pack()

    rectCardsForPlayer = [] # Array used to store rectangle shapes for use on Canvas as cards for player
    textCardsForPlayer = [] # Array used to store text of each card represented on Canvas player
    rectCardsForDealer = [] # Array used to store rectangle shapes for use on Canvas as cards for dealer
    textCardsForDealer = [] # Array used to store text of each card represented on Canvas dealer

    player = Player() 
    dealer = Dealer()
    gameDeck = CardDeck()

    # Create the GUI button elements and link the commands to the corresponding methods
    hitMeBtn = tk.Button(root, text=f"Hit Me!", command=hitMeBtnClickHandler)
    hitMeBtn.pack(pady=5)
    holdBtn = tk.Button(root, text="Hold", command=holdBtnClickHandler)
    holdBtn.pack(pady=5)
    IncreaseWagerBtn = tk.Button(root, text=f"Increase Wager", command=increaseWagerBtnClickHandler)
    IncreaseWagerBtn.pack(side=tk.RIGHT, pady=5)
    DecreaseWagerBtn = tk.Button(root, text="Decrease Wager", command=decreaseWagerBtnClickHandler)
    DecreaseWagerBtn.pack(side=tk.RIGHT)
    renderCards()

    root.mainloop()