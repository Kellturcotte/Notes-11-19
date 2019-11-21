
import random

class CardDeck():
    # build the deck
    suits = ['hearts','Clubs','Spades','Diamonds']
    values = ['Ace','two','three','Four','Five','six','Seven','Eight','Nine','ten','Jack','Queen','King']
    
    def __init__(self):
        self.deck = []
        for suit in self.suits:
            for value in self.values:
                self.deck.append([value,suit])
    # shuffle
    def shuffleDeck(self):
        for i in range(1000):
            random.shuffle(self.deck)
    # deal a card
    def deal(self):
        return self.deck.pop()
    # display the deck
    def displayDeck(self):
        for card in self.deck:
            print(card)

def main():
    players = [[], [], [], []] 

    theDeck = CardDeck()
    # print(theDeck)
    # theDeck.displayDeck()
    theDeck.shuffleDeck()
    # theDeck.displayDeck()
    for i in range(13):
        # print(f'Card dealt: {theDeck.deal()}')
        players[0].append(theDeck.deal())
        players[1].append(theDeck.deal())
        players[2].append(theDeck.deal())
        players[3].append(theDeck.deal())
        
    count = 0  
    for player in players:
        print(f'Player {count}')
        for card in player:
            print(card)
        count += 1
main()