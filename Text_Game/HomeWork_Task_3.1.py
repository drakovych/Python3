import os


class for_text_game(object):

    def __init__(self):
        self.time = 0
        self.karma = 0
        self.clothes = 0

    def qestion_1(self):
        file_q1 = open('HomeWork_Task_3.q1.txt', 'r')
        print(file_q1.read(568))
        x = 1
        while x:
            answer = str(input('\nЧто-то сделать : '))
            if answer == 'убить гадину':
                os.system('cls')
                file_q1.seek(576)
                print(file_q1.read(220))
                self.time += 0
                self.karma += 1
                x = 0
                break
            if answer == 'попытаться заснуть':
                os.system('cls')
                file_q1.seek(800)
                print(file_q1.read(246))
                self.time += 10
                self.karma -= 1
                x = 0
                break
            print('\nВы делали явно что-то не то')
        file_q1.close()
        input('\nтыкни \'Enter\' для продолжения')

    def qestion_2(self):
        os.system('cls')
        file_q2 = open('HomeWork_Task_3.q2.txt', 'r')
        print(file_q2.read(179))
        answer_1 = (input('\nПринять душ, да или нет, вот в чём вопрос: '))
        if answer_1 == 'да':
            self.time += 10
            self.karma += 1
            print('\nОтлично!')
        elif answer_1 == 'нет':
            self.time += 0
            self.karma -= 1
            print('\nДа ну нафиг с тем душем')
        else:
            file_q2.seek(181)
            print(file_q2.read(82))
            self.time += -5
            self.karma -= 1
        answer_2 = (input('\nПричесаться и побриться : '))
        if answer_2 == 'да':
            self.time += 10
            self.karma += 1
            print('\nОтлично!')
        elif answer_2 == 'нет':
            self.time += 0
            self.karma -= 1
            print('\nДа ну нафиг с этим всем')
        else:
            file_q2.seek(181)
            print(file_q2.read(82))
            self.time += -5
            self.karma -= 1
        answer_3 = (input('\nПочистить зубы : '))
        if answer_3 == 'да':
            self.time += 5
            self.karma += 1
            print('\nОтлично!')
        elif answer_3 == 'нет':
            self.time += 0
            self.karma -= 1
            print('\nДа ну нафиг с этим всем')
        else:
            file_q2.seek(181)
            print(file_q2.read(82))
            self.time -= 5
            self.karma -= 1
        file_q2.close()
        input('\nтыкни \'Enter\' для продолжения')

    def qestion_3(self):
        os.system('cls')
        file_q3 = open('HomeWork_Task_3.q3.txt', 'r')
        print(file_q3.read(483))
        self.clothes = int(input('\nВыбирай уже : '))
        if self.clothes == 1:
            self.karma -= 10
        if self.clothes == 2:
            self.karma += 10
        if self.clothes == 3:
            self.karma += 1000
        file_q3.close()
        input('\nтыкни \'Enter\' для продолжения')

    def qestion_4(self):
        os.system('cls')
        file_q4 = open('HomeWork_Task_3.q4.txt', 'r')
        print(file_q4.read(535))
        breakfast = str(input('\nНу и....: '))
        if breakfast == 'кофе и яичница':
            print('\nК чёрту шефа, завтрак важнее! Работа подождёт!')
            self.time += 20
            self.karma += 0
        elif breakfast == '\nкофе':
            print('\nДа блин времени и так нет!!! Кофе и погнали.')
            self.time += 5
            self.karma -= 10
        else:
            file_q4.seek(544)
            print(file_q4.read(100))
        self.time += 0
        self.karma -= 50
        file_q4.close()
        input('\nтыкни \'Enter\' для продолжения')

    def qestion_5(self):
        os.system('cls')
        file_q5 = open('HomeWork_Task_3.q5.txt', 'r')
        print(file_q5.read(551))
        timer = 0
        for i in range(10):
            code = input('\nНакрутить код : ')
            timer += 1
            if code == '905':
                print('\nЯ шмогла!!! Бегу на работу!!!')
                break
            elif timer == 10:
                os.system('cls')
                file_q5.seek(552)
                print(file_q5.read(103))
                os.abort()
        file_q5.close()

    def final_game(self):
        os.system('cls')
        file_q6 = open('HomeWork_Task_3.q6.txt', 'r')
        if self.clothes == 3:
            print(file_q6.read(241))
        if self.clothes == 4:
            file_q6.seek(241)
            print(file_q6.reed(235))
            os.abort()
        file_q6.close()
        if self.karma < 0:
            print('%s %i %s' % ('\tДобравшись до работы шеф негодовал,\
\nа вы еще и опоздали на', self.time, 'минут. Вопшем шеф себе сделал подарок\
\nна день рожденье и уволил вас.\n\nКонец!!!'))
        if self.karma > 0 and self.karma < 500:
            print('%s %i %s' % ('\tДобравшись до работы шев уже начал отмечает\
\nднюху был недоволен что вы опоздали на', self.time, 'минут. Вы отделались\
\nнебольшим штрафом и сумели похмелится с шефом вопщем жизнь в понедельник\
\nпотихоньку начала налаживаться.\n\nКонец!!!'))
        if self.karma > 500:
            print('\tДобравшись до работы шеф уже изрядно напразновался в свой\
\nдень рожденье. Когда вы вошли в офис в вечернем платье он долго ржал. Сказал\
\nчто так не смеялся давно. Вы получили премию и нормально похмелились с\
\nшефом. Но просил больше так его не смешить.\n\nКонец!!!')

game = for_text_game()
game.qestion_1()
game.qestion_2()
game.qestion_3()
game.qestion_4()
game.qestion_5()
game.final_game()

input('\nтыкни \'Enter\' для продолжения')
