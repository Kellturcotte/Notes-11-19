import random

class Bot():
    def __init__(self,name,):
        self.name = name
        self.hp = 100

    def punch(self):
        self.hp = self.hp + random.randint(-10,10)
bruce = Bot('Bruce')
garth = Bot('Garth')


while bruce.hp > -100 or garth > -100:
    bruce.punch()
    print(f'Bruce: {bruce.hp}')
    garth.punch()
    print(f'Garth: {bruce.hp}')
    if bruce.hp > garth.hp:
        print('bruce wins')
        else:
            print