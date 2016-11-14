# Card game 21
import random
import os
selected_cards_check = []


def choice_card():
    deck_cards = ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C',
                  'JC', 'QC', 'KC', 'AC',
                  '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D',
                  'JD', 'QD', 'KD', 'AD',
                  '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H',
                  'JH', 'QH', 'KH', 'AH',
                  '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S',
                  'JS', 'QS', 'KS', 'AS'
                  ]
    card = random.choice(deck_cards)
    return card


# Второй способ, каждый раз генерирует колоду (((
def choice_card_2():
    suits = "HDCS"
    ranks = "23456789TJQKA"
    deck = [x + y for x in suits for y in ranks]
    card = random.choice(deck)
    return card


def select_cards():
    card_list = []
    x = 2
    while x:
        card = choice_card()
        if selected_cards_check.count(card) == 0:
            card_list.append(card)
            selected_cards_check.append(card)
            x -= 1
    return card_list


def take_a_card():
    x = 1
    while x:
        card = choice_card()
        if selected_cards_check.count(card) == 0:
            selected_cards_check.append(card)
            x -= 1
    return card


def sum_cards(sum):
    x = 0
    for i in sum:
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


score = [0, 0]
choise = None

while choise != 2:
    print('''
        1 - Начать игру
        2 - Выйти
        ''')
    choise = int(input('Ваш выбор: '))
    if choise == 1:
        os.system('cls')
        PlayerCards = select_cards()
        CompCards = select_cards()
        print('Score player: ', score[0], 'comp: ', score[1])
        print('\n\nYou have this cards : ', PlayerCards,
              '\nHis sum = ', sum_cards(PlayerCards))
        x = input('\n\nTake more cards yes/no? : ')
        while x == 'yes':
            os.system('cls')
            PlayerCards.append(take_a_card())
            print('Score player: ', score[0], 'comp: ', score[1])
            print('\n\nYou have this cards : ', PlayerCards,
                  '\nHis sum = ', sum_cards(PlayerCards))
            if sum_cards(PlayerCards) == 21:
                score[0] += 1
                os.system('cls')
                print('\nYou WIN!')
                print('\nScore player: ', score[0], 'comp: ', score[1])
                break
            elif sum_cards(PlayerCards) >= 21:
                score[1] += 1
                os.system('cls')
                print('\nYou loss!')
                print('\nScore player: ', score[0], 'comp: ', score[1])
                break
            CompCards.append(take_a_card())
            if sum_cards(CompCards) == 21:
                score[1] += 1
                os.system('cls')
                print('\nComputer Win!')
                print('\nScore player: ', score[0], 'comp: ', score[1])
                break
            elif sum_cards(PlayerCards) >= 21:
                score[0] += 1
                os.system('cls')
                print('\nComputer loss!')
                print('\nScore player: ', score[0], 'comp: ', score[1])
                break
            x = input('\n\nTake more cards yes/no? : ')
        else:
            if sum_cards(PlayerCards) > sum_cards(CompCards):
                score[0] += 1
                os.system('cls')
                print('\nYou Win')
                print('\nScore player: ', score[0], 'comp: ', score[1])
            elif sum_cards(PlayerCards) < sum_cards(CompCards):
                score[1] += 1
                os.system('cls')
                print('\nComp Win')
                print('\nScore player: ', score[0], 'comp: ', score[1])
            elif sum_cards(PlayerCards) == sum_cards(CompCards):
                os.system('cls')
                print('\nDraw!!!')
    if choise == 2:
        print('До свидания!')
        print('\a')
        input('\nPress \'Enter\' for exit!')
