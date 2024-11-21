from card import Card
from play import Play

oCard = Card()
oPlay = Play()

playerName = oPlay.playerName()

oPlay.rules(playerName)

playerHand = oCard.getHand()
computerHand = oCard.getHand()

throwAwayPile = oCard.getStartCard()

print("\nHere is your starting hand:")
print(playerHand)

print("\nHere is the starting card: ")
print(throwAwayPile)

print("\nYou go first!\n")

player = [playerHand, computerHand]
print(throwAwayPile)

x, y = 0, 1

while len(playerHand) > 0 or len(computerHand) > 0:
    if x == 0:
        card = oPlay.chooseCard(player[x], throwAwayPile)
    else: 
        card = oPlay.computerTurn(player[x], throwAwayPile)

    if card == "":
        cardDrawn = oCard.getCard()
        player[x].append(cardDrawn)
    else:
        throwAwayPile = card
        player[x].remove(card)

    print("Dicard pile: " + throwAwayPile)

    if card == "+4":
        extraCards = oCard.draw4()

        if x == 0:
            throwAwayPile = oCard.chooseColor() + " 0"
        else: 
            throwAwayPile = oCard.computerChooseColor(player[x]) + " 0"

        player[y].extend(extraCards)

        print("Dicard pile: " + throwAwayPile)
        x, y = y, x

    elif card == "choose color":
        if x == 0:
            throwAwayPile = oCard.chooseColor() + " 0"
        else: 
            throwAwayPile = oCard.computerChooseColor(player[x]) + " 0"

        print("Dicard pile: " + throwAwayPile)        
        x, y = y, x

    elif card.endswith("skip"):
        x, y = x, y

    elif card.endswith("draw 2"):
        extraCards = oCard.draw2()
        player[y].extend(extraCards)

        x, y = y, x

    else:
        x, y = y, x


    if len(playerHand) == 0:
        print("You win!")
        break 
    elif len(computerHand) == 0:
        print("You lose. Computer wins!")
        break
    else:
        continue
