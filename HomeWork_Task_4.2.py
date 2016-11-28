# Card game 21
import random
import os

x = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
     'JC', 'QC', 'KC', 'AC',
     '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
     'JD', 'QD', 'KD', 'AD',
     '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
     'JH', 'QH', 'KH', 'AH',
     '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
     'JS', 'QS', 'KS', 'AS'
     ]
score = [0, 0]


class Deck(object):
    def __init__(self, deck, selected_cards_check=[]):
        self.deck_cards = deck
        self.selected_cards_check = selected_cards_check
        self.x = x

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
            if i in ('2C', '2D', '2H', '2S', 'JC', 'JD', 'JH', 'JS'):
                x += 2
            if i in ('3C', '3D', '3H', '3S', 'QC', 'QD', 'QH', 'QS'):
                x += 3
            if i in ('4C', '4D', '4H', '4S', 'KC', 'KD', 'KH', 'KS'):
                x += 4
            if i in ('5C', '5D', '5H', '5S'):
                x += 5
            if i in ('6C', '6D', '6H', '6S'):
                x += 6
            if i in ('7C', '7D', '7H', '7S'):
                x += 7
            if i in ('8C', '8D', '8H', '8S'):
                x += 8
            if i in ('9C', '9D', '9H', '9S'):
                x += 9
            if i in ('10C', '10D', '10H', '10S'):
                x += 10
            if i in ('AC', 'AD', 'AH', 'AS'):
                x += 11
        return x

    def sum_cards_check(self):
        if self.sum_cards() > 21:
            sum_cards_check = 0
            return sum_cards_check
        if self.sum_cards() == 21:
            sum_cards_check = 1
            return sum_cards_check
        if self.sum_cards() < 19:
            sum_cards_check = 2
            return sum_cards_check

    def who_win_check():
        sum_cp = Deck(PlayerCards)
        sum_cc = Deck(CompCards)
        if (sum_cp.sum_cards() and sum_cc.sum_cards) < 21:
            if sum_cp.sum_cards() > sum_cc.sum_cards:
                who_win_check = 0
                return who_win_check
            if sum_cp.sum_cards() < sum_cc.sum_cards:
                who_win_check = 1
                return who_win_check
            if sum_cp.sum_cards() == sum_cc.sum_cards:
                who_win_check = 2
                return who_win_check


def game_21():
    os.system('cls')
    print(PlayerCards)
    print(CompCards)
    input('\nPress \'Enter\' for exit!')


def game_menu():
    print('\n1 - Start Game.\n2 - Exit.')
    choice = input('\nYour choice : ')
    while choice != '2':
        # os.system('cls')
        if choice == 1:
            game_21()
        if choice == '2':
            os.system('cls')
            print('Goodby!')
            print('\a')


# PlayerCards = []
# CompCards = []
y = Deck(x)
PlayerCards = y.choose_cards()
CompCards = y.choose_cards()
#game_21()
game_menu()

input('\nPress \'Enter\' for exit!')