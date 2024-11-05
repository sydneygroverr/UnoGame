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
    