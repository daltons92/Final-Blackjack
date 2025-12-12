''' 
A Class that represents a deck of cards.
'''

from enum import Enum
import random

class Suit(Enum):
    DIAMOND = 1
    HEART = 2
    CLUB = 3
    SPADE = 4

class Value(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

class CardDeck:

    cardsAvailable = [] # Represents the available deck of cards

    # Constructor which calls shuffleDeck() for cardsAvailable[]
    def __init__(self):
        self.shuffleDeck()
        
    # Will 'Shuffle/Reset' the deck, enabling all cards/suites to be available
    def shuffleDeck(self):
        for suit in Suit:
            for value in Value:
                CardDeck.cardsAvailable.append([suit.name, value.value])
        random.shuffle(CardDeck.cardsAvailable)

    # Will return a random card selected from the deck using RNG
    def drawCard(self):
        if(len(CardDeck.cardsAvailable) < 1): # Shuffle the deck if we are out of cards
            CardDeck.shuffleDeck(self)
            print("The dealer gives the deck a thorough shuffle ..")
        cardDrawn = CardDeck.cardsAvailable.pop()
        print(f"Card drawn: {cardDrawn[1]} of {cardDrawn[0]}")
        return cardDrawn
    