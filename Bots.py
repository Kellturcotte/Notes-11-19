import random

class Bot():
    def __init__(self,name,):
        self.name = name
        self.hp = 100

    def punch(self):
        self.hp = self.hp + random.randint(-10,0)
bruce = Bot('Bruce')
garth = Bot('Garth')


while bruce.hp > 0 and garth.hp > 0:
    bruce.punch()
    print(f'Bruce: {bruce.hp}')
    garth.punch()
    print(f'Garth: {garth.hp}')
if bruce.hp > garth.hp:
    print('Bruce wins')
else:
    print('Garth wins')
