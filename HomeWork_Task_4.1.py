# Card game 21
import random
# import os

x = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
     'JC', 'QC', 'KC', 'AC',
     '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
     'JD', 'QD', 'KD', 'AD',
     '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
     'JH', 'QH', 'KH', 'AH',
     '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
     'JS', 'QS', 'KS', 'AS'
     ]


class Deck(object):
    def __init__(self, deck, selected_cards_check=[]):
        self.deck_cards = deck
        self.selected_cards_check = selected_cards_check

    def choose_cards(self):
        x = 2
        card = []
        while x:
            y = random.choice(self.deck_cards)
            if self.selected_cards_check.count(y) == 0:
                card.append(y)
                self.selected_cards_check.append(y)
                x -= 1
        return card

    def add_cards(self):
        x = 1
        while x:
            card = random.choice(self.deck_cards)
            if self.selected_cards_check.count(card) == 0:
                self.selected_cards_check.append(card)
                x -= 1
        return card

    def sum_cards(self):
        x = 0
        for i in self.deck_cards:
            if (i == '2C' or i == '2D' or i == '2H' or i == '2S' or i == 'JC' or i == 'JD' or i == 'JH' or i == 'JS'):
                x += 2
            if (i == '3C' or i == '3D' or i == '3H' or i == '3S' or i == 'QC' or i == 'QD' or i == 'QH' or i == 'QS'):
                x += 3
            if (i == '4C' or i == '4D' or i == '4H' or i == '4S' or i == 'KC' or i == 'KD' or i == 'KH' or i == 'KS'):
                x += 4
            if (i == '5C' or i == '5D' or i == '5H' or i == '5S'):
                x += 5
            if (i == '6C' or i == '6D' or i == '6H' or i == '6S'):
                x += 6
            if (i == '7C' or i == '7D' or i == '7H' or i == '7S'):
                x += 7
            if (i == '8C' or i == '8D' or i == '8H' or i == '8S'):
                x += 8
            if (i == '9C' or i == '9D' or i == '9H' or i == '9S'):
                x += 9
            if (i == '10C' or i == '10D' or i == '10H' or i == '10S'):
                x += 10
            if (i == 'AC' or i == 'AD' or i == 'AH' or i == 'AS'):
                x += 11
        return x


y = Deck(x)
PlayerCards = []
print(PlayerCards)
PlayerCards.append(y.add_cards())
print(PlayerCards)
PlayerCards = Deck(PlayerCards)
sum = PlayerCards.sum_cards()
print(sum)
PlayerCards = y.choose_cards()
print(PlayerCards)
input('\nPress \'Enter\' for exit!')
