import random
import os


class rock_paper_scissors(object):
    def __init__(self):
        self.vibir = ['k', 'n', 'p']
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
        while True:
            self.x = input('\nКамень (k), Ножницы (n), Бумага (p) : ')
            while self.x not in self.vibir:
                print('\nВы не выбрали k, n, p')
                self.x = input('\nКамень (k), Ножницы (n), Бумага (p) : ')
            self.y = random.choice(self.vibir)
            return

    def get_check_winner(self):
        winner_map = {'k': 'n', 'n': 'p', 'p': 'k'}
        self.round()
        if self.x == self.y:
            self.nowin += 1
            return 'nowin'
        for arg1, arg2 in winner_map.items():
            if self.x == arg1 and self.y == arg2:
                self.win += 1
                return 'win'
        self.lose += 1
        return 'lose'

    def main_game(self):
        i = 0
        message = {'nowin': 'Ничья', 'win': 'Победа', 'lose': 'Проигрыш'}
        os.system('cls')
        while i != 5:
            print(message[self.get_check_winner()])
            i += 1
        print('\nИгрок выиграл %i раз, проиграл %i раз, \
сыграл в ничью %i раз' % (self.win, self.lose, self.nowin))
        input('\nтыкни \'Enter\' для продолжения')
        os.system('cls')


play = rock_paper_scissors()
play.game_menu()
