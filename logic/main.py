class UnoGame:

    def initializeGame(self):
        from card import Card
        from play import Play

        oCard = Card()
        oPlay = Play()

        playerName = oPlay.playerName()

        oPlay.rules(playerName)

        playerHand = oCard.getHand()
        computerHand = oCard.getHand()

        throwAwayPile = oCard.getStartCard()

        return oCard, oPlay, playerName, playerHand, computerHand, throwAwayPile

    def playerTurn(oPlay, oCard, player, throwAwayPile, x, y):
        if x == 0:
            card = oPlay.chooseCard(player[x], throwAwayPile)
        else: 
            card = oPlay.computerTurn(player[x], throwAwayPile)

        if card == "":
            cardDrawn = oCard.getCard()
            player[x].append(cardDrawn)
            
            # if x == 0:
            #     print(player[x])
            #     # show hand of player
                
        else:
            throwAwayPile = card
            player[x].remove(card)

        throwAwayPile, x, y = specialCards(oCard, oPlay, card, throwAwayPile, player, x, y)

        return player, throwAwayPile, x, y


    def specialCards(oCard, oPlay, card, throwAwayPile, player, x, y):
        if card == "+4":
            extraCards = oCard.draw4()

            if x == 0:
                throwAwayPile = oCard.chooseColor() + " 0"
            else: 
                throwAwayPile = oCard.computerChooseColor(player[x]) + " 0"

            player[y].extend(extraCards)

            # print("Dicard pile: " + throwAwayPile)
            x, y = y, x

        elif card == "choose color":
            if x == 0:
                throwAwayPile = oCard.chooseColor() + " 0"
            else: 
                throwAwayPile = oCard.computerChooseColor(player[x]) + " 0"

            # print("Dicard pile: " + throwAwayPile)        
            x, y = y, x

        elif card.endswith("skip"):
            x, y = x, y

        elif card.endswith("draw 2"):
            extraCards = oCard.draw2()
            player[y].extend(extraCards)

            x, y = y, x

        else:
            x, y = y, x

        return player, throwAwayPile, x, y


    def checkWinner(player):
        
        if len(player[0]) == 0:
            return("You win!") 
        elif len(player[1]) == 0:
            return("You lose. Computer wins!")
        else:
            return False 


    def playGame():
        oCard, oPlay, playerHand, computerHand, throwAwayPile = UnoGame.initializeGame()
        player = [playerHand, computerHand]
        x, y = 0, 1

        while len(player[x]) > 0 or len(player[y]) > 0:
            throwAwayPile, x, y = UnoGame.playerTurn(oPlay, oCard, player, throwAwayPile, x, y)
            if UnoGame.checkWinner(player) != False:
                print(UnoGame.checkWinner)
                break
            else:
                continue

    def get_game_state(self):
        # Return the current game state
        return {
            'deck': self.throwAwayPile,
            'current_turn': self.x,
            'player_hand': self.playerHand,
            'computer_hand': self.computerHand
        }