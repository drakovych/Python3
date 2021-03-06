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

    def sum_player_cards_check(self):
        if self.sum_cards() > 21:
            score[1] += 1
            print('\nComp Win! Player have cards sum > 21.')
            return True
        elif self.sum_cards() == 21:
            score[0] += 1
            print('\nPlayer Win! Player have cards sum = 21.')
            return True

    def sum_comp_cards_check(self):
        if self.sum_cards() > 21:
            score[0] += 1
            print('\nPlayer Win! Comp have cards sum > 21.')
            return True
        elif self.sum_cards() == 21:
            score[1] += 1
            print('\nComp Win! Comp have cards sum = 21.')
            return True

    def print_cards_sum(self, player_card):
        print('\nPlayer score : ', score[0], '\tComp score : ', score[1])
        print('\nPlayer have the cards : ', player_card,
              '\nTheir sum : ', self.sum_cards())


def who_win_check(player_card, comp_card):
    sum_cp = Deck(player_card)
    sum_cc = Deck(comp_card)
    if (sum_cp.sum_cards() and sum_cc.sum_cards()) < 21:
        if sum_cp.sum_cards() > sum_cc.sum_cards():
            score[0] += 1
            print('\nPlayer score : ', score[0],
                  '\tComp score : ', score[1])
            print('\nPlayer Win! Player have cards sum more.')
        elif sum_cp.sum_cards() < sum_cc.sum_cards():
            score[1] += 1
            print('\nPlayer score : ', score[0],
                  '\tComp score : ', score[1])
            print('\nComp Win! Comp have cards sum more.')
        elif sum_cp.sum_cards() == sum_cc.sum_cards():
            print('\nNo winner, draw. Sum cards equal.')


def game_21():
    os.system('cls')
    deck_in_game = Deck(x, selected_cards_check=[])
    player_card = deck_in_game.choose_cards()
    player_cards_hand = Deck(player_card)
    comp_card = deck_in_game.choose_cards()
    comp_cards_hand = Deck(comp_card)
    player_cards_hand.print_cards_sum(player_card)
    answer = input('\nYou want to take an additional card (yes/no)? : ')
    while answer == 'yes':
        if answer == 'yes':
            player_card.append(deck_in_game.add_cards())
            player_cards_hand = Deck(player_card)
            if player_cards_hand.sum_player_cards_check() == True:
                break
            if comp_cards_hand.sum_cards() < 19:
                comp_card.append(deck_in_game.add_cards())
                comp_cards_hand = Deck(comp_card)
                if comp_cards_hand.sum_comp_cards_check() == True:
                    break
        player_cards_hand.print_cards_sum(player_card)
        answer = input('\nYou want to take an additional card (yes/no)? : ')
    else:
        while comp_cards_hand.sum_cards() < 19:
            comp_card.append(deck_in_game.add_cards())
            comp_cards_hand = Deck(comp_card)
            if comp_cards_hand.sum_comp_cards_check() == True:
                break
    who_win_check(player_card, comp_card)


def game_menu():
    choice = 0

    while choice != '2':
        print('\n1 - Start Game.\n2 - Exit.')
        choice = input('\nYour choice : ')
        # os.system('cls')
        if choice == '1':
            game_21()
        if choice == '2':
            os.system('cls')
            print('Goodby!')
            print('\a')


game_menu()

input('\nPress \'Enter\' for exit!')
