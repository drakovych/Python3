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


def main():
    score = [0, 0]
    choise = None
    while choise != 2:
        print('''
            1 - Start Game.
            2 - Exit.
            ''')
        choise = int(input('Your choice : '))
        if choise == 1:
            PlayerCards = []
            CompCards = []
            PlayerCards = y.choose_cards()
            CompCards = y.choose_cards()
            sumP = Deck(PlayerCards)
            sumC = Deck(CompCards)
            os.system('cls')
            print('Score player: ', score[0], 'comp: ', score[1])
            print('\n\nYou have this cards : ', PlayerCards,
                  '\nHis sum = ', sumP.sum_cards())
            Take_Card = input('\n\nTake more cards yes/no? : ')
            while Take_Card == 'yes':
                os.system('cls')
                PlayerCards.append(y.add_cards())
                sumP = Deck(PlayerCards)
                print('Score player: ', score[0], 'comp: ', score[1])
                print('\n\nYou have this cards : ', PlayerCards,
                      '\nHis sum = ', sumP.sum_cards())
                if sumP.sum_cards() == 21:
                    score[0] += 1
                    os.system('cls')
                    print('\nYou WIN!')
                    print('\nScore player: ', score[0], 'comp: ', score[1])
                    break
                if sumP.sum_cards() > 21:
                    score[1] += 1
                    os.system('cls')
                    print('\nYou loss!')
                    print('\nScore player: ', score[0], 'comp: ', score[1])
                    break
                if sumC.sum_cards() < 19:
                    CompCards.append(y.add_cards())
                    sumC = Deck(CompCards)
                    if sumC.sum_cards() == 21:
                        score[1] += 1
                        os.system('cls')
                        print('\nComp WIN!')
                        print('\nComputer have this cards : ', CompCards)
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                        break
                    if sumC.sum_cards() > 21:
                        score[0] += 1
                        os.system('cls')
                        print('\nComp loss!')
                        print('\nComputer have this cards : ', CompCards)
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                        break
                Take_Card = input('\n\nTake more cards yes/no? : ')
            else:
                while sumC.sum_cards() < 19:
                    CompCards.append(y.add_cards())
                    sumC = Deck(CompCards)
                    if sumC.sum_cards() == 21:
                        score[1] += 1
                        os.system('cls')
                        print('\nComp WIN!')
                        print('\nComputer have this cards : ', CompCards)
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                        break
                    if sumC.sum_cards() > 21:
                        score[0] += 1
                        os.system('cls')
                        print('\nComp loss!')
                        print('\nComputer have this cards : ', CompCards)
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                        break
                if sumP.sum_cards() <= 21 and sumC.sum_cards() <= 21:
                    if sumP.sum_cards() > sumC.sum_cards():
                        score[0] += 1
                        os.system('cls')
                        print('\nYou Win')
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                    elif sumP.sum_cards() < sumC.sum_cards():
                        score[1] += 1
                        os.system('cls')
                        print('\nComp Win')
                        print('\nComputer have this cards : ', CompCards)
                        print('\nScore player: ', score[0], 'comp: ', score[1])
                    elif sumP.sum_cards() == sumC.sum_cards():
                        os.system('cls')
                        print('\nDraw!!!')
        if choise == 2:
            os.system('cls')
            print('Goodby!')
            print('\a')


y = Deck(x)
main()
input('\nPress \'Enter\' for exit!')
