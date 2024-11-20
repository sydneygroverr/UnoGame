from card import Card
from play import Play

oCard = Card()
oPlay = Play()

playerName = oPlay.playerName()

oPlay.rules(playerName)

playerHand = oCard.getHand()
computerHand = oCard.getHand()

throwAwayPile = oCard.getStartCard()

print("Here is your starting hand:")

print(playerHand)

print("Here is the starting card: ")

print(throwAwayPile)

print("You go first!")
player = [playerHand, computerHand]
x, y = 0, 1

# while len(playerHand) > 0 or len(computerHand) > 0:
if x == 0:
    card = oPlay.chooseCard(player[x], throwAwayPile)
else: 
    card = oPlay.computerTurn(player[x], throwAwayPile)

throwAwayPile = card
print(throwAwayPile)

if card == "+4":
    extraCards = oCard.draw4()
    player[y].extend(extraCards)
    x, y = y, x
elif card == "choose color":
    throwAwayPile = oCard.chooseColor() + " 0"
    x, y = y, x
elif card.endswith("skip"):
    x, y = x, y
elif card.endswith("draw 2"):
    extraCards = oCard.draw2()
    player[y].extend(extraCards)
    x, y = y, x
else:
    x, y = y, x


    

