# I want a class deck, that takes in suits [], cards[], number of decks
# pokerDeck = Deck(["Hearts"....], ["A", "K"....], 1)
# hand = pokerDeck.draw(5)
# the cards remaining wont have the hand cards
# pokerDeck.shuffle() <= reorder the deck, and add all cards back to it
# be creative add more things to deck.
# note: remember the deck knows nothing about the game being played
# pokerDeck.cut(10) <= pass in an index and it should slice it and reorder as expected
import random

SUITS = [ "Club", "Diamond", "Heart", "Spade" ]
CARD_TYPES= [
    "Ace", "Jack", "King", "Queen",
    2, 3, 4, 5, 6, 7, 8, 9, 10
]

class Deck:
    def __init__(self, suits, cardTypes, numberOfDecks):
        self.cards = [f"{c} of {s}" for s in suits for c in cardTypes]
        self.cards = self.cards * numberOfDecks

    def draw(self, count):
        if len(self.cards) < count:
            raise OutOfCardsException(
                f"Asked for {count} cards than are {len(self.cards)} available")

        return [self.cards.pop(0) for i in range(count)]

    def cut(self, place):
        if len(self.cards) < place:
            raise InvalidCutException(
                "You must pick a valid place within the deck to cut")

        self.cards = self.cards[place:] + self.cards[:place]

    def shuffle(self):
        random.shuffle(self.cards)


class OutOfCardsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCutException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

if __name__ == "__main__":
    pokerDeck = Deck(SUITS, CARD_TYPES, 1)
    print(pokerDeck.cards)
    pokerDeck.shuffle()
    print(pokerDeck.cards)
    hand1 = pokerDeck.draw(5)
    hand2 = pokerDeck.draw(5)

    print(hand1)
    print(hand2)
    print(pokerDeck.cards)

    pokerDeck2 = Deck(SUITS, CARD_TYPES, 1)
    print(pokerDeck2.cards)
    pokerDeck2.cut(5)
    print(pokerDeck2.cards)