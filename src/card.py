import random

class Card():
    color = ["blue", "green", "yellow", "red"]
    value = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "skip", "draw 2"]
    wild = ["+4", "choose color"]

    def getCard(self):

        cardColor = random.randrange(0,4)
        x = random.randrange(0,14)

        if x < 12:
            val = self.value[x]
            self.c = (f'{self.color[cardColor]} {val}')
        elif x == 12:
            val = self.wild[0]
            self.c = val
        else:
            val = self.wild[1]
            self.c = val
         
        return self.c   
    
    # ensures starting card is a plain number card
    def getStartCard(self):
        cardColor = random.randrange(0,4)
        x = random.randrange(0,10)

        val = self.value[x]
        self.c = (f'{self.color[cardColor]} {val}')
         
        return self.c 
    
    # to start each game both players get 7 cards
    def getHand(self):
        hand = []
        x = 0

        while x < 7:
            hand.append(self.getCard()) 
            x += 1

        return hand

    def draw4(self):
        x = 0
        val = []
        while x < 4:
            val.append(self.getCard())
            x += 1
        return val
    
    def chooseColor(self):
        color = input("What would you like the new color to be? 1-red, 2-blue, 3-green, 4-yellow\n")

        if color == "1":
            color = "red"
        elif color == "2":
            color = "blue"
        elif color == "3":
            color = "green"
        else:
            color = "yellow"

        return color
    
    def draw2(self):
        x = 0
        val = []
        while x < 2:
            val.append(self.getCard())
            x += 1
        return val
    
    def computerChooseColor(self, hand):
        x = 0
        color = ""

        while color == "":
            if hand[x].split()[0] == "red":
                color = "red"
            elif hand[x].split()[0] == "blue":
                color = "blue"
            elif hand[x].split()[0] == "green":
                color = "green"
            elif hand[x].split()[0] == "yellow":
                color = "yellow"
            else: 
                x += 1
                if x > len(hand):
                    color = "red"
        
        return color