class Play():

    def playerName(self):
        name = input("What is your name?")
        return name

    def rules(self, name):
        played = input(f"Hi {name}! Have you played UNO before? y/n \n")

        no = ['n', 'no', 'nah', 'never', 'negative', 'nope']
        yes = ['y', 'yes', 'ya', 'yeah', 'yah']

        rules = """Here are the rules of the game:\n
                Each player starts with 7 cards\n
                Players will go back and forth placing a card into the discard pile\n
                You can play a card when it matches either the colour or number of the card, \n
                or if you have any wild cards. \n
                If you have no playable cards, you must draw a card from the draw pile. \n
                The aim of UNO is to be the first player to get rid of all of your cards \n
                so you'll want to avoid picking up cards as best you can. \n
                Good luck and have fun! \n"""
        
        start = "Then lets get started!"

        if played.lower() in no:
            print(rules)
        else:
            print(start)

    def chooseCard(self, hand, throwAwayPile):
        print(hand)
        card =  input("What card do you want to play? 1-" + str(len(hand))) 
        val = int(card) - 1
        choice = hand[val] 

        result = Play.validCard(self, choice, throwAwayPile, hand)

        if result == True:
            return choice


    def validCard(self, card, throwAwayPile, hand):

        if card == "+4" or card == "choose color":
            throwAwayPile = card
            return True
        elif card.split(" ")[0] == throwAwayPile.split(" ")[0]:
            throwAwayPile = card
            return True
        elif card.split(" ")[1] == throwAwayPile.split(" ")[1]:
            throwAwayPile = card
            return True
        else:
            print(f'{card} is an invalid card. Try again.')
            self.chooseCard(self, hand, throwAwayPile)

    # def computerTurn(self, hand, throwAwayPile):
    #     # do computer turn here