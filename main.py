# A class is a grouping of both data and functions(Methods) to operate on that data
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduceYourself(self):
        print("Hello my name is", self.name)

    def changeName(self, newName):
        self.name = newName

justin = Person("Justin", 31)
print(justin.name)
justin.changeName("Not Justin")
print(justin.name)
print(justin.age)
adam = Person("Adam", 28)

people = [ justin, adam ]

for i in people:
    i.introduceYourself()


# Create a circle class, this class takes in (radius) and has a method to get the area
# Circle(10)
# Circle.area() => area of the circle
# Circle.diameter() => diameter of the circle

# Note there is a build in PI in python modules google to find out how to use it
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def diameter(self):
        return self.radius * 2

    def __repr__(self):
        return f"Circle(10)"

    def __str__(self):
        return f"This is a Circle of radius 10"

    def __int__(self):
        return 10

    def __iter__(self):
        yield f"Radius: {self.radius}"

circle = Circle(10)
area = circle.area()
diameter = circle.diameter()

print(str(circle), repr(circle), int(circle), tuple(circle), area, diameter, sep="\n")

class TicketVendor:
    def __init__(self, event, ticketCount):
        self.event = event
        self.totalTickets = ticketCount
        self.tickets = ticketCount

    def __iter__(self):
        while(self.tickets):
            yield f"You are ticket number {self.totalTickets - self.tickets + 1}"
            self.tickets = self.tickets - 1
        

party = TicketVendor("New years", 100)

for t in party:
    print(t)


# I want a class deck, that takes in suits [], cards[], number of decks
# pokerDeck = Deck(["Hearts"....], ["A", "K"....], 1)
# hand = pokerDeck.draw(5)
# the cards remaining wont have the hand cards
# pokerDeck.shuffle() <= reorder the deck, and add all cards back to it
# be creative add more things to deck.
# note: remember the deck knows nothing about the game being played
# pokerDeck.cut(10) <= pass in an index and it should slice it and reorder as expected

