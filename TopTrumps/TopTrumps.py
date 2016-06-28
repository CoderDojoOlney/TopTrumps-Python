import random
import time

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
    
    time.sleep(1)

    playerCard = playerDeck.pop(0)
    computerCard = computerDeck.pop(0)

    print("YOUR CARD")
    print("Name:", playerCard.name)
    print("a. Height:", playerCard.height)
    print("b. Caps:", playerCard.caps)
    print("c. Metres made:", playerCard.metres)
    print("d. Tackles made:", playerCard.tackles)
    print("e. Penalties conceded:", playerCard.penalties)
    
    time.sleep(1)

    if playerTurn == True:
        answer = input("Which property do you choose? ")
        while allowedResponses.count(answer) == 0:
            answer = input("That isn't a valid answer, please try again: ")
    else:
        answer = random.choice(allowedResponses)
        print("Computer chooses", answer)

    print("COMPUTER CARD")
    print("Name:", computerCard.name)

    playerWins = False

    if answer == "a":
        print("Height:", computerCard.height)
        isDraw = (playerCard.height == computerCard.height)
        playerWins = (playerCard.height > computerCard.height)
    elif answer == "b":
        print("Caps:", computerCard.caps)
        isDraw = (playerCard.caps == computerCard.caps)
        playerWins = (playerCard.caps > computerCard.caps)
    elif answer == "c":
        print("Metres made:", computerCard.metres)
        isDraw = (playerCard.metres == computerCard.metres)
        playerWins = (playerCard.metres > computerCard.metres)
    elif answer == "d":
        print("Tackles made:", computerCard.tackles)
        isDraw = (playerCard.tackles == computerCard.tackles)
        playerWins = (playerCard.tackles > computerCard.tackles)
    elif answer == "e":
        print("Penalties conceded:", computerCard.penalties)
        isDraw = (playerCard.penalties == computerCard.penalties)
        playerWins = (playerCard.penalties < computerCard.penalties)

    time.sleep(1)

    if isDraw:
        print("It's a tie!")
        playerDeck.append(playerCard)
        computerDeck.append(computerCard)
    elif playerWins:
        print("You win this hand!")
        playerDeck.append(playerCard)
        playerDeck.append(computerCard)
        playerTurn = True
    else:
        print("You lose this hand!")
        computerDeck.append(computerCard)
        computerDeck.append(playerCard)
        playerTurn = False

time.sleep(2)

if len(playerDeck) == 0:
    print("YOU LOSE!")
else:
    print("YOU WIN!")