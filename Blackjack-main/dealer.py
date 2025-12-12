'''
A class that represents the dealer.
'''

class Dealer():
    global dealerCardsValue # Tracks dealers card value (ex: 21)


    def __init__(self):
        global dealerCardsValue
        dealerCardsValue = 0 # Tracks dealers score
        

    def addCardToHand(self, card):
        global dealerCardsValue # Tracks dealers card value (ex: 21)
        if card[1] in (11, 12, 13): # If a jack/queen/king is drawn add a value of 10
            dealerCardsValue += 10
        elif card[1] == 14: # Else if a Ace is drawn add 1 or 11 depending on which is more beneficial
            if dealerCardsValue < 10:
                dealerCardsValue += 11
            else:
                dealerCardsValue += 1
        else: # Else just add the cards face value
            dealerCardsValue += card[1]
        print(f"The dealer draws a {card[0]} - {card[1]} with a total hand value of {dealerCardsValue}")


    # Returns dealer's cardValue
    def getCardsValue(self):
        return dealerCardsValue
    
    # Set dealer's cardValue
    def setCardsValue(self, value):
        global dealerCardsValue
        dealerCardsValue = value
