import random


class MSDie():
    def __init__(self,sides):
        self.sides = sides
        self.value = 1
    
    def roll(self):
        self.value = random.randint(1,self.sides)

    # use instead of self.value
    def getValue(self):
        return self.value
    #  use instead self.sides
    def getSides(self):
        return self.sides

    def setValue(self,value):
        self.value = value
    
    def setSides(self,sides):
        self.sides = sides 


dieBag = []

# makes 7 die  |
#              V
for i in range(7):
    dieBag.append(MSDie(6))
# adds 7 die to list ^
# rolls each die |
#                V
for die in dieBag:
    die.roll()
    print(die.getValue())

# changing the valuse of the dice in the list dieBag
for die in dieBag:
    die.setSides(10)
    die.setValue(2)
    print(die.getValue(),die.getSides())

# | gets inserted as self
# v
# d6 = MSDie(6)
# d6.value = 3
# print(d6.sides)
# print(d6.value)
# d100 = MSDie(100)

# for i in range(10):
#     d6.roll()
#     print(d6.value)

