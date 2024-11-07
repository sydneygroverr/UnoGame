from card import Card
from play import Play

oCard = Card()
oPlay = Play()

playerName = oPlay.playerName()

oPlay.rules(playerName)

playerHand = oCard.getHand()
computerHand = oCard.getHand()

throwAwayPile = oCard.getStartCard()

