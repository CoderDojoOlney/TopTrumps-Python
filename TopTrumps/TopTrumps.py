import random

class Card:
    def __init__(self, name, height, caps, metres, tackles, penalties):
        self.name = name
        self.height = height
        self.caps = caps
        self.metres = metres
        self.tackles = tackles
        self.penalties = penalties

cards = []
cards.append(Card("Billy Vunipola", 1.88, 26, 336, 46, 2)) 
cards.append(Card("Chris Robshaw", 1.88, 48, 51, 48, 5))
cards.append(Card("Owen Farrell", 1.88, 40, 56, 47, 4))
cards.append(Card("Mike Brown", 1.83, 48, 417, 9, 1))

random.shuffle(cards)

playerDeck = []
computerDeck = []

# Deal the cards
while len(cards) > 0:
    playerDeck.append(cards.pop(0))
    computerDeck.append(cards.pop(0))

playerTurn = True
allowedResponses = ["a", "b", "c", "d", "e"]

while len(playerDeck) > 0 and len(computerDeck) > 0:
    
    playerCard = playerDeck.pop[0]
    computerCard = computerDeck.pop[0]

    print("Name:", thisCard.name)
    print("1. Height:", thisCard.height)
    print("2. Caps:", thisCard.caps)
    print("3. Metres made:", thisCard.metres)
    print("4. Tackles made:", thisCard.tackles)
    print("5. Penalties conceded:", thisCard.penalties)
    
    if playerTurn == True:
        answer = input("Which property do you choose? ")
