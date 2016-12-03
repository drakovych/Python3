import random
import os
from game_winner_map import winner_map, choice_map, choice_show


class rock_paper_scissors(object):
    def __init__(self):
        self.vibir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.x = None
        self.y = None
        self.win = 0
        self.lose = 0
        self.nowin = 0

    def game_menu(self):
        choice = 0
        while choice != '2':
            print('\n1 - Начать игру.\n2 - Выйти.')
            choice = input('\nВаш выбор : ')
            if choice == '1':
                self.main_game()
            if choice == '2':
                os.system('cls')
                print('Пока!')
                print('\a')

    def round(self):
        self.x = None
        while True:
            try:
                self.x = int(input('Ваш выбор : '))
            except (TypeError, ValueError):
                print('Это не целое число')
            while self.x not in self.vibir:
                os.system('cls')
                print('Вы не выбрали число!')
                try:
                    self.x = int(input('Ваш выбор : '))
                except (TypeError, ValueError):
                    print('Это не целое число')
            self.y = random.choice(self.vibir)
            return

    def get_check_winner(self):
        self.round()
        print('\nИгрок выбрал: ', choice_map[self.x],
              '\tКомп выбрал: ', choice_map[self.y])
        if self.x == self.y:
            self.nowin += 1
            return 'nowin'
        for arg1, arg2 in winner_map.items():
            if self.x == arg1:
                for x in arg2:
                    if x == self.y:
                        self.win += 1
                        return 'win'
        self.lose += 1
        return 'lose'

    def main_game(self):
        i = 0
        message = {'nowin': '\nНичья', 'win': '\nВы выиграли',
                   'lose': '\nВы проиграли'}
        os.system('cls')
        print(choice_show)
        while i != 5:
            print(message[self.get_check_winner()])
            i += 1
        # print()
        print('\nИгрок выиграл %i раз, проиграл %i раз, сыграл в ничью %i раз'
              % (self.win, self.lose, self.nowin))
        input('\nтыкни \'Enter\' для продолжения')
        os.system('cls')


play = rock_paper_scissors()
play.game_menu()
