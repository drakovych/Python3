import sys
import random

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from game_variables import *


class Ui_MainWindow(object):
    def __init__(self):
        self.vibir = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.x = None
        self.y = None
        self.win = 0
        self.lose = 0
        self.nowin = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(303, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_1.setObjectName('radioButton_1')
        self.radioButton_1.toggled.connect(self.get_radio1_clicked)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_2.setObjectName('radioButton_2')
        self.radioButton_2.toggled.connect(self.get_radio2_clicked)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_3.setObjectName('radioButton_3')
        self.radioButton_3.toggled.connect(self.get_radio3_clicked)
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.radioButton_4.setObjectName('radioButton_4')
        self.radioButton_4.toggled.connect(self.get_radio4_clicked)
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_5.setObjectName('radioButton_5')
        self.radioButton_5.toggled.connect(self.get_radio5_clicked)
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(120, 70, 82, 17))
        self.radioButton_6.setObjectName('radioButton_6')
        self.radioButton_6.toggled.connect(self.get_radio6_clicked)
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(120, 90, 82, 17))
        self.radioButton_7.setObjectName('radioButton_7')
        self.radioButton_7.toggled.connect(self.get_radio7_clicked)
        self.radioButton_8 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_8.setGeometry(QtCore.QRect(120, 110, 82, 17))
        self.radioButton_8.setObjectName('radioButton_8')
        self.radioButton_8.toggled.connect(self.get_radio8_clicked)
        self.radioButton_9 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_9.setGeometry(QtCore.QRect(120, 130, 82, 17))
        self.radioButton_9.setObjectName('radioButton_9')
        self.radioButton_9.toggled.connect(self.get_radio9_clicked)
        self.radioButton_10 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_10.setGeometry(QtCore.QRect(120, 150, 82, 17))
        self.radioButton_10.setObjectName('radioButton_10')
        self.radioButton_10.toggled.connect(self.get_radio10_clicked)
        self.radioButton_11 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_11.setGeometry(QtCore.QRect(220, 70, 82, 17))
        self.radioButton_11.setObjectName('radioButton_11')
        self.radioButton_11.toggled.connect(self.get_radio11_clicked)
        self.radioButton_12 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_12.setGeometry(QtCore.QRect(220, 90, 82, 17))
        self.radioButton_12.setObjectName('radioButton_12')
        self.radioButton_12.toggled.connect(self.get_radio12_clicked)
        self.radioButton_13 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_13.setGeometry(QtCore.QRect(220, 110, 82, 17))
        self.radioButton_13.setObjectName('radioButton_13')
        self.radioButton_13.toggled.connect(self.get_radio13_clicked)
        self.radioButton_14 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_14.setGeometry(QtCore.QRect(220, 130, 82, 17))
        self.radioButton_14.setObjectName('radioButton_14')
        self.radioButton_14.toggled.connect(self.get_radio14_clicked)
        self.radioButton_15 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_15.setGeometry(QtCore.QRect(220, 150, 82, 17))
        self.radioButton_15.setObjectName('radioButton_15')
        self.radioButton_15.toggled.connect(self.get_radio15_clicked)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 167, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName('line')
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 58, 301, 10))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName('line_2')
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 30, 64, 23))
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(140, 30, 64, 23))
        self.lcdNumber_2.setObjectName('lcdNumber_2')
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(220, 30, 64, 23))
        self.lcdNumber_3.setObjectName('lcdNumber_3')
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 10, 301, 16))
        self.label.setObjectName('label')
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 200, 113, 20))
        self.lineEdit.setObjectName('lineEdit')
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 200, 113, 20))
        self.lineEdit_2.setObjectName('lineEdit_2')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 240, 81, 23))
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(self.handleButton)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 180, 281, 20))
        self.label_2.setObjectName('label_2')
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 20))
        self.menubar.setObjectName('menubar')
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName('menuMenu')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName('actionHelp')
        self.actionHelp.triggered.connect(self.menu_help)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName('actionExit')
        self.actionExit.triggered.connect(self.menu_exit)
        self.menuMenu.addAction(self.actionHelp)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        return

    def setupUi_help_window(self, help_window):
        help_window.setObjectName('help_window')
        help_window.resize(553, 431)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        help_window.setFont(font)
        self.pushButton = QtWidgets.QPushButton(help_window)
        self.pushButton.setGeometry(QtCore.QRect(460, 400, 75, 23))
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(self.close_button)
        self.label = QtWidgets.QLabel(help_window)
        self.label.setGeometry(QtCore.QRect(10, 10, 541, 391))
        self.label.setObjectName('label')

        self.retranslateUi_help(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('MainWindow',
                                             'Rock Paper Scissors'))
        self.radioButton_1.setText(_translate('MainWindow', 'Камень'))
        self.radioButton_2.setText(_translate('MainWindow', 'Огонь'))
        self.radioButton_3.setText(_translate('MainWindow', 'Ножницы'))
        self.radioButton_4.setText(_translate('MainWindow', 'Змея'))
        self.radioButton_5.setText(_translate('MainWindow', 'Человек'))
        self.radioButton_6.setText(_translate('MainWindow', 'Дерево'))
        self.radioButton_7.setText(_translate('MainWindow', 'Волк'))
        self.radioButton_8.setText(_translate('MainWindow', 'Губка'))
        self.radioButton_9.setText(_translate('MainWindow', 'Бумага'))
        self.radioButton_10.setText(_translate('MainWindow', 'Воздух'))
        self.radioButton_11.setText(_translate('MainWindow', 'Вода'))
        self.radioButton_12.setText(_translate('MainWindow', 'Дракон'))
        self.radioButton_13.setText(_translate('MainWindow', 'Дьявол'))
        self.radioButton_14.setText(_translate('MainWindow', 'Молния'))
        self.radioButton_15.setText(_translate('MainWindow', 'Пистолет'))
        self.label.setText(_translate(
            'MainWindow', 'Score:   \
            YourWin            CompWin                NoWin'))
        self.pushButton.setText(_translate('MainWindow', 'Начать'))
        self.label_2.setText(_translate(
            'MainWindow', '        Вы выбрали\
                                    Комп выбрал '))
        self.menuMenu.setTitle(_translate('MainWindow', 'Menu'))
        self.actionHelp.setText(_translate('MainWindow', 'Help'))
        self.actionExit.setText(_translate('MainWindow', 'Exit'))

    def retranslateUi_help(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate('help_window', 'Help'))
        self.pushButton.setText(_translate('help_window', 'Close'))
        # str111 = str(self.rules_str())
        # self.label.setText(str111)
        self.label.setText(_translate('help_window',
'Камень побеждает: Огонь, Ножницы, Змею, Человека, Дерево, Волка, Губку.\n\n'
'Огонь побеждает: Ножницы, Змею, Человека, Дерево, Волка, Губку, Бумагу.\n\n'
'Ножницы побеждают: Змею, Человека, Дерево, Волка, Губку, Бумагу, Воздух.\n\n'
'Змея побеждает: Человека, Дерево, Волка, Губку, Бумагу, Воздух, Воду.\n\n'
'Человек побеждает: Дерево, Волка, Губку, Бумагу, Воздух, Воду, Дракона.\n\n'
'Дерево побеждает: Волка, Губку, Бумагу, Воздух, Воду, Дракона, Дьявола.\n\n'
'Волк побеждает: Губку, Бумагу, Воздух, Воду, Дракона, Дьявола, Молнию.\n\n'
'Губка побеждает: Бумагу, Воздух, Воду, Дракона, Дьявола, Молнию, Пистолет.\n\n'
'Бумага побеждает: Воздух, Воду, Дракона, Дьявола, Молнию, Пистолет, Камень.\n\n'
'Воздух побеждает: Воду, Дракона, Дьявола, Молнию, Пистолет, Камень, Огонь.\n\n'
'Вода побеждает: Дракона, Дьявола, Молнию, Пистолет, Камень, Огонь, Ножницы.\n\n'
'Дракон побеждает: Дьявола, Молнию, Пистолет, Камень, Огонь, Ножницы, Змею.\n\n'
'Дьявол побеждает: Молнию, Пистолет, Камень, Огонь, Ножницы, Змею, Человека.\n\n'
'Молния побеждает: Пистолет, Камень, Огонь, Ножницы, Змею, Человека, Дерево.\n\n'
'Пистолет побеждает: Камень, Огонь, Ножницы, Змею, Человека, Дерево, Волка.'))

    # def rules_str(self):
    #     z = ''
    #     for key, value in rules.items():
    #         for y in value:
    #             z = z + y + ' '
    #         x = str(print(key, ' : ', z))
    #         z = ''

    def close_button(self):
        help_window.close()

    def menu_exit(self):
        sys.exit(app.exec())

    def menu_help(self):
        ui.setupUi_help_window(help_window)
        help_window.show()

    def showLCD(self, win, lose, nowin):
        self.lcdNumber.display(win)
        self.lcdNumber_2.display(lose)
        self.lcdNumber_3.display(nowin)

    def handleButton(self):
        if self.x != None:
            self.y = self.get_comp_choose()
            self.lineEdit_2.setText(choice_map[self.y])
            self.get_check_winner()
            self.showLCD(self.win, self.lose, self.nowin)

    def get_radio1_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Камень')
            self.x = 1
            return

    def get_radio2_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Огонь')
            self.x = 2
            return

    def get_radio3_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Ножницы')
            self.x = 3
            return

    def get_radio4_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Змея')
            self.x = 4
            return

    def get_radio5_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Человек')
            self.x = 5
            return

    def get_radio6_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Дерево')
            self.x = 6
            return

    def get_radio7_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Волк')
            self.x = 7
            return

    def get_radio8_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Губка')
            self.x = 8
            return

    def get_radio9_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Бумага')
            self.x = 9
            return

    def get_radio10_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Воздух')
            self.x = 10
            return

    def get_radio11_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Вода')
            self.x = 11
            return

    def get_radio12_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Дракон')
            self.x = 12
            return

    def get_radio13_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Дьявол')
            self.x = 13
            return

    def get_radio14_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Молния')
            self.x = 14
            return

    def get_radio15_clicked(self, enabled):
        if enabled:
            self.lineEdit.setText('Пистолет')
            self.x = 15
            return

    def get_comp_choose(self):
        self.y = random.choice(self.vibir)
        return self.y

    def get_check_winner(self):
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

    def get_lcd_number(self):
        ui.showLCD(self.win, self.lose, self.nowin)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
help_window = QtWidgets.QWidget()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
