import random
import os


class rock_paper_scissors(object):
    def __init__(self):
        self.vibir = ['k', 'n', 'p']
        self.x = None
        self.y = None

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

    def main_game(self):
        win = 0
        lose = 0
        nowin = 0
        i = 0
        os.system('cls')
        while i != 5:
            self.round()
            if self.x == self.y:
                print("\nНичья")
                nowin += 1
            elif (self.x == "k" and self.y == "n") or \
(self.x =="n" and self.y =="p") or (self.x == "p" and self.y =="k"):
                print("\nИгрок победил")
                win += 1
            else:
                print("\nИгрок проиграл")
                lose += 1
            i += 1
        print('\nИгрок выиграл %i раз, проиграл %i раз, \
сыграл в ничью %i раз' % (win, lose, nowin))
        input('\nтыкни \'Enter\' для продолжения')
        os.system('cls')


play = rock_paper_scissors()
play.game_menu()
