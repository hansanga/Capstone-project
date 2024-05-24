# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledgobUlr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QStackedWidget, QLabel, QPushButton, QMenuBar, QStatusBar, QApplication
from PyQt5.QtGui import QFont, QPixmap, QMovie  # QFont 사용을 위해 추가
from PyQt5.QtCore import QRect, QTimer, Qt, QCoreApplication, QMetaObject  # QRect 사용을 위해 추가
import sys



class Ui_ColorLog(object):
    def setupUi(self, ColorLog):
        if not ColorLog.objectName():
            ColorLog.setObjectName(u"ColorLog")
        ColorLog.resize(1920, 1080)
        ColorLog.setStyleSheet(u"background-color: #f8fbff;")
        self.centralwidget = QWidget(ColorLog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #f8fbff;")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(11, 11, 1898, 1007))
        font = QFont()
        font.setPointSize(9)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet(u"background-color: #f3f8ff;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.MainLogo = QLabel(self.page)
        self.MainLogo.setObjectName(u"MainLogo")
        self.MainLogo.setGeometry(QRect(645, 286, 631, 222))
        font1 = QFont()
        font1.setFamily(u"Bookman Old Style")
        font1.setPointSize(80)
        font1.setBold(False)
        font1.setWeight(50)
        self.MainLogo.setFont(font1)
        self.MainLogo.setStyleSheet(u"text-shadow: 2px 2px 2px black;")
        self.MainLogo.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(770, 620, 401, 111))
        font2 = QFont()
        font2.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font2.setPointSize(30)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.stackedWidget.addWidget(self.page)

        #page2
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.smallLogo1 = QLabel(self.page_2)
        self.smallLogo1.setObjectName(u"smallLogo1")
        self.smallLogo1.setGeometry(QRect(20, 20, 181, 51))
        font3 = QFont()
        font3.setFamily(u"Bookman Old Style")
        font3.setPointSize(22)
        font3.setBold(False)
        font3.setWeight(50)
        self.smallLogo1.setFont(font3)
        self.smallLogo1.setAlignment(Qt.AlignCenter)
        self.welcome = QLabel(self.page_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(470, 140, 981, 591))
        font4 = QFont()
        font4.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font4.setPointSize(17)
        self.welcome.setFont(font4)
        self.welcome.setStyleSheet(u"padding: 15px; border: 2px solid #c8c8c8; background-color: #ffffff; border-radius: 10px;  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.welcome.setAlignment(Qt.AlignCenter)
        self.pushButton_1 = QPushButton(self.page_2)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(820, 790, 281, 91))
        font5 = QFont()
        font5.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font5.setPointSize(20)
        self.pushButton_1.setFont(font5)
        self.pushButton_1.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.timer1 = QLabel(self.page_2)
        self.timer1.setObjectName(u"timer1")
        self.timer1.setGeometry(QRect(1650, 10, 121, 51))
        font6 = QFont()
        font6.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font6.setPointSize(15)
        font6.setBold(False)
        font6.setWeight(50)
        self.timer1.setFont(font6)
        self.timer1.setAlignment(Qt.AlignCenter)
        self.timer_1 = QLabel(self.page_2)
        self.timer_1.setObjectName(u"timer_1")
        self.timer_1.setGeometry(QRect(1774, 19, 101, 41))
        font7 = QFont()
        font7.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font7.setPointSize(15)
        self.timer_1.setFont(font7)
        self.timer_1.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.timer_1.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_2)

        #page3
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.ex1 = QLabel(self.page_3)
        self.ex1.setObjectName(u"ex1")
        self.ex1.setGeometry(QRect(620, 120, 681, 80))
        self.ex1.setFont(font4)
        self.ex1.setAlignment(Qt.AlignCenter)
        self.camera = QLabel(self.page_3)
        self.camera.setObjectName(u"camera")
        self.camera.setGeometry(QRect(515, 240, 891, 501))
        font8 = QFont()
        font8.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font8.setPointSize(16)
        self.camera.setFont(font8)
        self.camera.setStyleSheet(u"border: 2px solid ")
        self.camera.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(820, 800, 280, 90))
        self.pushButton_2.setFont(font5)
        self.pushButton_2.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.timer2 = QLabel(self.page_3)
        self.timer2.setObjectName(u"timer2")
        self.timer2.setGeometry(QRect(1650, 10, 121, 51))
        self.timer2.setFont(font6)
        self.timer2.setAlignment(Qt.AlignCenter)
        self.smallLogo2 = QLabel(self.page_3)
        self.smallLogo2.setObjectName(u"smallLogo2")
        self.smallLogo2.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo2.setFont(font3)
        self.smallLogo2.setAlignment(Qt.AlignCenter)
        self.timer_2 = QLabel(self.page_3)
        self.timer_2.setObjectName(u"timer_2")
        self.timer_2.setGeometry(QRect(1774, 19, 101, 41))
        self.timer_2.setFont(font7)
        self.timer_2.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.timer_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)

        #page4
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.camera2 = QLabel(self.page_4)
        self.camera2.setObjectName(u"camera2")
        self.camera2.setGeometry(QRect(515, 240, 891, 501))
        self.camera2.setFont(font8)
        self.camera2.setStyleSheet(u"border: 2px solid ")
        self.camera2.setAlignment(Qt.AlignCenter)
        self.ex2 = QLabel(self.page_4)
        self.ex2.setObjectName(u"ex2")
        self.ex2.setGeometry(QRect(795, 120, 431, 51))
        font9 = QFont()
        font9.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font9.setPointSize(19)
        self.ex2.setFont(font9)
        self.ex2.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.page_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1490, 430, 181, 51))
        font10 = QFont()
        font10.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font10.setPointSize(18)
        self.label.setFont(font10)
        self.label.setAlignment(Qt.AlignCenter)
        self.num = QLabel(self.page_4)
        self.num.setObjectName(u"num")
        self.num.setGeometry(QRect(1520, 500, 131, 61))
        self.num.setFont(font4)
        self.num.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.num.setAlignment(Qt.AlignCenter)
        self.loading = QLabel(self.page_4)
        self.loading.setObjectName(u"loading")
        self.loading.setGeometry(QRect(660, 70, 90, 150))
        self.loading_movie = QMovie("media/loading_1.gif")
        self.loading.setMovie(self.loading_movie)
        self.loading_movie.start()
        # self.pushButton_3 = QPushButton(self.page_4)
        # self.pushButton_3.setObjectName(u"pushButton_3")
        # self.pushButton_3.setGeometry(QRect(820, 800, 280, 90))
        # self.pushButton_3.setFont(font5)
        # self.pushButton_3.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.smallLogo3 = QLabel(self.page_4)
        self.smallLogo3.setObjectName(u"smallLogo3")
        self.smallLogo3.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo3.setFont(font3)
        self.smallLogo3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)

        #page5
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.intro = QLabel(self.page_5)
        self.intro.setObjectName(u"intro")
        self.intro.setGeometry(QRect(470, 210, 981, 511))
        self.intro.setFont(font4)
        self.intro.setStyleSheet(u"padding: 15px; border: 2px solid #c8c8c8; background-color: #ffffff; border-radius: 10px;  box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.intro.setAlignment(Qt.AlignCenter)
        self.ex3 = QLabel(self.page_5)
        self.ex3.setObjectName(u"ex3")
        self.ex3.setGeometry(QRect(765, 110, 450, 71))
        font11 = QFont()
        font11.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font11.setPointSize(16)
        self.ex3.setFont(font11)
        self.ex3.setAlignment(Qt.AlignCenter)
        self.loading2 = QLabel(self.page_5)
        self.loading2.setObjectName(u"loading2")
        self.loading2.setGeometry(QRect(710, 90, 90, 90))
        self.loading2_movie = QMovie("media/loading_1.gif")
        self.loading2.setMovie(self.loading2_movie)
        self.loading2_movie.start()        
        self.pushButton_4 = QPushButton(self.page_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(820, 800, 280, 90))
        self.pushButton_4.setFont(font5)
        self.pushButton_4.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.smallLogo4 = QLabel(self.page_5)
        self.smallLogo4.setObjectName(u"smallLogo4")
        self.smallLogo4.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo4.setFont(font3)
        self.smallLogo4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_5)

        #page6
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.back2 = QLabel(self.page_6)
        self.back2.setObjectName(u"back2")
        self.back2.setGeometry(QRect(1251, 0, 650, 1011))
        font12 = QFont()
        font12.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Medium")
        font12.setPointSize(10)
        self.back2.setFont(font12)
        self.back2.setStyleSheet(u"padding: 15px; border-left: 2px solid #c8c8c8; background-color: #ffffff;   box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.back2.setAlignment(Qt.AlignCenter)
        self.back1 = QLabel(self.page_6)
        self.back1.setObjectName(u"back1")
        self.back1.setGeometry(QRect(0, 90, 1251, 781))
        self.back1.setFont(font12)
        self.back1.setStyleSheet(u"padding: 15px; border-bottom: 3px solid #c8c8c8; background-color: #ffffff;   box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.back1.setAlignment(Qt.AlignCenter)
        self.ex5 = QLabel(self.page_6)
        self.ex5.setObjectName(u"ex5")
        self.ex5.setGeometry(QRect(1340, 220, 478, 101))
        font13 = QFont()
        font13.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font13.setPointSize(19)
        self.ex5.setFont(font13)
        self.ex5.setStyleSheet(u"background-color: #ffffff;")
        self.ex5.setAlignment(Qt.AlignCenter)
        self.next = QLabel(self.page_6)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(1340, 370, 478, 91))
        self.next.setFont(font4)
        self.next.setStyleSheet(u"background-color: #ffffff;")
        self.next.setAlignment(Qt.AlignCenter)
        self.ex6 = QLabel(self.page_6)
        self.ex6.setObjectName(u"ex6")
        self.ex6.setGeometry(QRect(1340, 480, 478, 81))
        font14 = QFont()
        font14.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Light")
        font14.setPointSize(14)
        self.ex6.setFont(font14)
        self.ex6.setStyleSheet(u"background-color: #ffffff;")
        self.ex6.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.page_6)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(430, 140, 391, 35))
        self.title.setFont(font5)
        self.title.setStyleSheet(u"background-color: #ffffff;")
        self.title.setAlignment(Qt.AlignCenter)
        self.faceColor = QLabel(self.page_6)
        self.faceColor.setObjectName(u"faceColor")
        self.faceColor.setGeometry(QRect(670, 280, 331, 61))
        font15 = QFont()
        font15.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Light")
        font15.setPointSize(16)
        self.faceColor.setFont(font15)
        self.faceColor.setStyleSheet(u"background-color: #ffffff;")
        self.faceColor.setAlignment(Qt.AlignCenter)
        self.facePhoto = QLabel(self.page_6)
        self.facePhoto.setObjectName(u"facePhoto")
        self.facePhoto.setGeometry(QRect(280, 230, 271, 341))
        self.facePhoto.setFont(font8)
        self.facePhoto.setStyleSheet(u"border: 2px solid ")
        self.facePhoto.setAlignment(Qt.AlignCenter)
        self.recoColor = QLabel(self.page_6)
        self.recoColor.setObjectName(u"recoColor")
        self.recoColor.setGeometry(QRect(680, 370, 311, 91))
        self.recoColor.setFont(font8)
        self.recoColor.setStyleSheet(u"border: 2px solid ")
        self.recoColor.setAlignment(Qt.AlignCenter)
        self.colorPalette = QLabel(self.page_6)
        self.colorPalette.setObjectName(u"colorPalette")
        self.colorPalette.setGeometry(QRect(390, 700, 471, 81))
        self.colorPalette.setFont(font8)
        self.colorPalette.setStyleSheet(u"border: 2px solid ")
        self.colorPalette.setAlignment(Qt.AlignCenter)
        self.ex4 = QLabel(self.page_6)
        self.ex4.setObjectName(u"ex4")
        self.ex4.setGeometry(QRect(435, 630, 381, 51))
        self.ex4.setFont(font15)
        self.ex4.setStyleSheet(u"background-color: #ffffff;")
        self.ex4.setAlignment(Qt.AlignCenter)
        self.pushButton_5 = QPushButton(self.page_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(1460, 630, 241, 71))
        self.pushButton_5.setFont(font10)
        self.pushButton_5.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.smallLogo5 = QLabel(self.page_6)
        self.smallLogo5.setObjectName(u"smallLogo5")
        self.smallLogo5.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo5.setFont(font3)
        self.smallLogo5.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_6)

        #page7
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.pushButton_6 = QPushButton(self.page_7)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(820, 750, 280, 90))
        self.pushButton_6.setFont(font5)
        self.pushButton_6.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.light = QLabel(self.page_7)
        self.light.setObjectName(u"light")
        self.light.setGeometry(QRect(420, 200, 1081, 71))
        font16 = QFont()
        font16.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font16.setPointSize(18)
        self.light.setFont(font16)
        self.light.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.light.setAlignment(Qt.AlignCenter)
        self.ex7 = QLabel(self.page_7)
        self.ex7.setObjectName(u"ex7")
        self.ex7.setGeometry(QRect(735, 110, 451, 51))
        self.ex7.setFont(font9)
        self.ex7.setAlignment(Qt.AlignCenter)
        self.select2 = QPushButton(self.page_7)
        self.select2.setObjectName(u"select2")
        self.select2.setGeometry(QRect(845, 340, 230, 230))
        self.select2.setStyleSheet(u"background-color: #feffd9; border-radius: 110px; border: 1px solid #c8c8c8;")
        self.select3 = QPushButton(self.page_7)
        self.select3.setObjectName(u"select3")
        self.select3.setGeometry(QRect(1180, 330, 230, 230))
        self.select3.setStyleSheet(u"background-color: #ded9ff; border-radius: 110px; border: 1px solid #c8c8c8;")
        self.select1 = QPushButton(self.page_7)
        self.select1.setObjectName(u"select1")
        self.select1.setGeometry(QRect(510, 340, 230, 230))
        self.select1.setStyleSheet(u"background-color: #d9f1ff; border-radius: 110px; border: 1px solid #c8c8c8;")
        self.select_1 = QLabel(self.page_7)
        self.select_1.setObjectName(u"select_1")
        self.select_1.setGeometry(QRect(560, 610, 121, 61))
        self.select_1.setFont(font10)
        self.select_1.setAlignment(Qt.AlignCenter)
        self.select_2 = QLabel(self.page_7)
        self.select_2.setObjectName(u"select_2")
        self.select_2.setGeometry(QRect(910, 610, 101, 51))
        self.select_2.setFont(font10)
        self.select_2.setAlignment(Qt.AlignCenter)
        self.select_3 = QLabel(self.page_7)
        self.select_3.setObjectName(u"select_3")
        self.select_3.setGeometry(QRect(1240, 610, 121, 41))
        self.select_3.setFont(font10)
        self.select_3.setAlignment(Qt.AlignCenter)
        self.timer3 = QLabel(self.page_7)
        self.timer3.setObjectName(u"timer3")
        self.timer3.setGeometry(QRect(1650, 10, 121, 51))
        self.timer3.setFont(font6)
        self.timer3.setAlignment(Qt.AlignCenter)
        self.smallLogo6 = QLabel(self.page_7)
        self.smallLogo6.setObjectName(u"smallLogo6")
        self.smallLogo6.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo6.setFont(font3)
        self.smallLogo6.setAlignment(Qt.AlignCenter)
        self.timer_3 = QLabel(self.page_7)
        self.timer_3.setObjectName(u"timer_3")
        self.timer_3.setGeometry(QRect(1774, 19, 101, 41))
        self.timer_3.setFont(font7)
        self.timer_3.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.timer_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_7)

        
        #page8
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.loading3 = QLabel(self.page_8)
        self.loading3.setObjectName(u"loading3")
        self.loading3.setGeometry(QRect(610, 100, 90, 90))
        self.loading3_movie = QMovie("media/loading_1.gif")
        self.loading3.setMovie(self.loading3_movie)
        self.loading3_movie.start()        
        self.ex8 = QLabel(self.page_8)
        self.ex8.setObjectName(u"ex8")
        self.ex8.setGeometry(QRect(695, 120, 591, 51))
        self.ex8.setFont(font4)
        self.ex8.setAlignment(Qt.AlignCenter)
        self.camera3 = QLabel(self.page_8)
        self.camera3.setObjectName(u"camera3")
        self.camera3.setGeometry(QRect(515, 240, 891, 501))
        self.camera3.setFont(font8)
        self.camera3.setStyleSheet(u"border: 2px solid ")
        self.camera3.setAlignment(Qt.AlignCenter)
        # self.pushButton_7 = QPushButton(self.page_8)
        # self.pushButton_7.setObjectName(u"pushButton_7")
        # self.pushButton_7.setGeometry(QRect(820, 800, 280, 90))
        # self.pushButton_7.setFont(font13)
        # self.pushButton_7.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.smallLogo7 = QLabel(self.page_8)
        self.smallLogo7.setObjectName(u"smallLogo7")
        self.smallLogo7.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo7.setFont(font3)
        self.smallLogo7.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.page_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1490, 430, 181, 51))
        self.label_2.setFont(font10)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.num_2 = QLabel(self.page_8)
        self.num_2.setObjectName(u"num_2")
        self.num_2.setGeometry(QRect(1520, 500, 131, 61))
        self.num_2.setFont(font4)
        self.num_2.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.num_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_8)

        #page9
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.finalPhoto = QLabel(self.page_9)
        self.finalPhoto.setObjectName(u"finalPhoto")
        self.finalPhoto.setGeometry(QRect(1010, 160, 750, 500))
        self.finalPhoto.setFont(font8)
        self.finalPhoto.setStyleSheet(u"border: 2px solid #c8c8c8")
        self.finalPhoto.setAlignment(Qt.AlignCenter)
        self.pushButton_8 = QPushButton(self.page_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(820, 760, 280, 90))
        self.pushButton_8.setFont(font13)
        self.pushButton_8.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.color1 = QPushButton(self.page_9)
        self.color1.setObjectName(u"color1")
        self.color1.setGeometry(QRect(140, 410, 191, 191))
        self.color1.setFont(font8)
        self.color1.setStyleSheet(u"border: 2px solid #c8c8c8")
        # self.color1.setAlignment(Qt.AlignCenter)
        self.ex9 = QLabel(self.page_9)
        self.ex9.setObjectName(u"ex9")
        self.ex9.setGeometry(QRect(320, 180, 361, 51))
        self.ex9.setFont(font11)
        self.ex9.setAlignment(Qt.AlignCenter)
        self.frame = QLabel(self.page_9)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(130, 250, 731, 61))
        self.frame.setFont(font8)
        self.frame.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.frame.setAlignment(Qt.AlignCenter)
        self.timer_4 = QLabel(self.page_9)
        self.timer_4.setObjectName(u"timer_4")
        self.timer_4.setGeometry(QRect(1774, 19, 101, 41))
        self.timer_4.setFont(font7)
        self.timer_4.setStyleSheet(u"border-radius: 15px; border-bottom: 2px solid #c8c8c8; border-right: 2px solid #c8c8c8; background-color: #ffffff;")
        self.timer_4.setAlignment(Qt.AlignCenter)
        self.smallLogo8 = QLabel(self.page_9)
        self.smallLogo8.setObjectName(u"smallLogo8")
        self.smallLogo8.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo8.setFont(font3)
        self.smallLogo8.setAlignment(Qt.AlignCenter)
        self.timer4 = QLabel(self.page_9)
        self.timer4.setObjectName(u"timer4")
        self.timer4.setGeometry(QRect(1650, 10, 121, 51))
        self.timer4.setFont(font6)
        self.timer4.setAlignment(Qt.AlignCenter)
        self.color2 = QPushButton(self.page_9)
        self.color2.setObjectName(u"color2")
        self.color2.setGeometry(QRect(400, 410, 191, 191))
        self.color2.setFont(font8)
        self.color2.setStyleSheet(u"border: 2px solid #c8c8c8")
        # self.color2.setAlignment(Qt.AlignCenter)
        self.color3 = QPushButton(self.page_9)
        self.color3.setObjectName(u"color3")
        self.color3.setGeometry(QRect(660, 410, 191, 191))
        self.color3.setFont(font8)
        self.color3.setStyleSheet(u"border: 2px solid #c8c8c8")
        # self.color3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_9)

        #page10
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.back3 = QLabel(self.page_10)
        self.back3.setObjectName(u"back3")
        self.back3.setGeometry(QRect(1251, 0, 650, 1011))
        self.back3.setFont(font12)
        self.back3.setStyleSheet(u"padding: 15px; border-left: 2px solid #c8c8c8; background-color: #ffffff;   box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")
        self.back3.setAlignment(Qt.AlignCenter)
        self.ex12 = QLabel(self.page_10)
        self.ex12.setObjectName(u"ex12")
        self.ex12.setGeometry(QRect(1350, 520, 478, 91))
        self.ex12.setFont(font4)
        self.ex12.setStyleSheet(u"background-color: #ffffff;")
        self.ex12.setAlignment(Qt.AlignCenter)
        self.ex11 = QLabel(self.page_10)
        self.ex11.setObjectName(u"ex11")
        self.ex11.setGeometry(QRect(1350, 290, 478, 191))
        font17 = QFont()
        font17.setFamily(u"KoPubWorld\ub3cb\uc6c0\uccb4 Bold")
        font17.setPointSize(17)
        self.ex11.setFont(font17)
        self.ex11.setStyleSheet(u"background-color: #ffffff;")
        self.ex11.setAlignment(Qt.AlignCenter)
        self.ex10 = QLabel(self.page_10)
        self.ex10.setObjectName(u"ex10")
        self.ex10.setGeometry(QRect(500, 140, 321, 51))
        self.ex10.setFont(font4)
        self.ex10.setAlignment(Qt.AlignCenter)
        self.loading4 = QLabel(self.page_10)
        self.loading4.setObjectName(u"loading4")
        self.loading4.setGeometry(QRect(430, 120, 90, 90))
        self.loading4_movie = QMovie("media/loading_1.gif")
        self.loading4.setMovie(self.loading4_movie)
        self.loading4_movie.start()        
        self.pushButton_9 = QPushButton(self.page_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(480, 780, 280, 90))
        self.pushButton_9.setFont(font13)
        self.pushButton_9.setStyleSheet(u"border-radius: 15px; border-bottom: 3px solid #c8c8c8;; background-color: #efefef;")
        self.smallLogo9 = QLabel(self.page_10)
        self.smallLogo9.setObjectName(u"smallLogo9")
        self.smallLogo9.setGeometry(QRect(20, 20, 181, 51))
        self.smallLogo9.setFont(font3)
        self.smallLogo9.setAlignment(Qt.AlignCenter)
        self.finalPhoto2 = QLabel(self.page_10)
        self.finalPhoto2.setObjectName(u"finalPhoto2")
        self.finalPhoto2.setGeometry(QRect(260, 240, 750, 500))
        self.finalPhoto2.setFont(font8)
        self.finalPhoto2.setStyleSheet(u"border: 2px solid ")
        self.finalPhoto2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_10)
        ColorLog.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ColorLog)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        ColorLog.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ColorLog)
        self.statusbar.setObjectName(u"statusbar")
        ColorLog.setStatusBar(self.statusbar)
        # QWidget.setTabOrder(self.pushButton, self.pushButton_1)
        # QWidget.setTabOrder(self.pushButton_1, self.pushButton_7)
        # QWidget.setTabOrder(self.pushButton_7, self.pushButton_3)
        # QWidget.setTabOrder(self.pushButton_3, self.pushButton_4)
        # QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        # QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        # QWidget.setTabOrder(self.pushButton_6, self.pushButton_2)
        # QWidget.setTabOrder(self.pushButton_2, self.pushButton_8)
        # QWidget.setTabOrder(self.pushButton_8, self.pushButton_9)

        self.retranslateUi(ColorLog)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(ColorLog.NextBtn)
        self.pushButton_1.clicked.connect(ColorLog.NextBtn)
        self.pushButton_2.clicked.connect(ColorLog.NextBtn)
        # self.pushButton_3.clicked.connect(ColorLog.NextBtn)
        self.pushButton_4.clicked.connect(ColorLog.NextBtn)
        self.pushButton_5.clicked.connect(ColorLog.NextBtn)
        self.pushButton_6.clicked.connect(ColorLog.NextBtn)
        # self.pushButton_7.clicked.connect(ColorLog.NextBtn)
        self.pushButton_8.clicked.connect(ColorLog.NextBtn)
        self.pushButton_9.clicked.connect(ColorLog.NextBtn)
        self.select1.clicked.connect(lambda: ColorLog.SelectBtn(1))
        self.select2.clicked.connect(lambda: ColorLog.SelectBtn(2))
        self.select3.clicked.connect(lambda: ColorLog.SelectBtn(3))
        self.color1.clicked.connect(lambda: ColorLog.SelectFrame(1))
        self.color2.clicked.connect(lambda: ColorLog.SelectFrame(2))
        self.color3.clicked.connect(lambda: ColorLog.SelectFrame(3))


        QMetaObject.connectSlotsByName(ColorLog)
    # setupUi

    def retranslateUi(self, ColorLog):
        ColorLog.setWindowTitle(QCoreApplication.translate("ColorLog", u"MainWindow", None))
        self.MainLogo.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.pushButton.setText(QCoreApplication.translate("ColorLog", u"\uc2dc\uc791\ud558\uae30", None))
        self.smallLogo1.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.welcome.setText(QCoreApplication.translate("ColorLog", u"\uceec\ub7ec\ub85c\uadf8\uc5d0 \uc624\uc2e0 \uac83\uc744 \ud658\uc601\ud569\ub2c8\ub2e4.\n"
"\n"
" \ud37c\uc2a4\ub110 \uceec\ub7ec \uc9c4\ub2e8\uc744 \ud1b5\ud574 \ub098\uc5d0\uac8c \uaf2d \ub9de\ub294 \ud504\ub808\uc784\uacfc \uc0c9\uc0c1\uc870\uba85\uc744 \ud65c\uc6a9\ud574\n"
" \uc0ac\uc9c4\uc744 \ucd2c\uc601\ud574 \ubcf4\uc138\uc694.\n"
"\n"
" \uc0ac\uc9c4\uacfc \ud568\uaed8 \ucd9c\ub825\ub41c QR \ucf54\ub4dc\ub97c \ud1b5\ud574 \uc9c4\ub2e8 \uacb0\uacfc\uc640\n"
" \ucd94\ucc9c \ud654\uc7a5\ud488 \ub9ac\uc2a4\ud2b8\ub97c \ud655\uc778\ud558\uc138\uc694.\n"
"\n"
" \uc9c4\ub2e8 \uc2dc\uc791\uc744 \uc6d0\ud558\uc2dc\uba74 \uc544\ub798\uc758 \ubc84\ud2bc\uc744 \ub20c\ub7ec\uc11c \uc2dc\uc791\ud574\uc8fc\uc138\uc694.\n"
"\n"
" \u203b \ubaa8\ub4e0 \ud654\uba74\uc5d0 \uc81c\ud55c\uc2dc\uac04\uc774 \uc788\uc2b5\ub2c8\ub2e4. \uc8fc\uc758\ud574\uc8fc\uc138\uc694 \u203b", None))
        self.pushButton_1.setText(QCoreApplication.translate("ColorLog", u"\ub2e4\uc74c\uc73c\ub85c", None))
        self.timer1.setText(QCoreApplication.translate("ColorLog", u"\uc81c\ud55c\uc2dc\uac04", None))
        self.timer_1.setText(QCoreApplication.translate("ColorLog", u"30", None))
        self.ex1.setText(QCoreApplication.translate("ColorLog", u"\ud37c\uc2a4\ub110\uceec\ub7ec \uc9c4\ub2e8\uc744 \uc704\ud55c \uc5bc\uad74 \uc0ac\uc9c4 \ucd2c\uc601\uc774 \uace7 \uc2dc\uc791\ub429\ub2c8\ub2e4.\n"
" \uc815\ud655\ud55c \uc9c4\ub2e8\uc744 \uc704\ud574 \uc815\uba74\uc744 \uc751\uc2dc\ud574\uc8fc\uc138\uc694.", None))
        self.camera.setText(QCoreApplication.translate("ColorLog", u"\uce74\uba54\ub77c\ub97c \ubd88\ub7ec\uc624\ub294 \uc911\uc785\ub2c8\ub2e4", None)) # changed
        self.pushButton_2.setText(QCoreApplication.translate("ColorLog", u"\uc9c4\ub2e8 \uc2dc\uc791\ud558\uae30", None))
        self.timer2.setText(QCoreApplication.translate("ColorLog", u"\uc81c\ud55c\uc2dc\uac04", None))
        self.smallLogo2.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.timer_2.setText(QCoreApplication.translate("ColorLog", u"30", None))
        self.camera2.setText(QCoreApplication.translate("ColorLog", u"\uce74\uba54\ub77c\ub97c \ubd88\ub7ec\uc624\ub294 \uc911\uc785\ub2c8\ub2e4", None)) # changed
        self.ex2.setText(QCoreApplication.translate("ColorLog", u"\uc9c4\ub2e8\uc744 \uc704\ud55c \uc0ac\uc9c4 \ucd2c\uc601 \uc911\uc785\ub2c8\ub2e4.", None))
        self.label.setText(QCoreApplication.translate("ColorLog", u"\ub0a8\uc740 \ucd2c\uc601 \uc218", None))
        self.num.setText(QCoreApplication.translate("ColorLog", u"0 / 1", None))
        self.loading.setText("")
        # self.pushButton_3.setText(QCoreApplication.translate("ColorLog", u"\ub118\uc5b4\uac00\uae30", None))
        self.smallLogo3.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.intro.setText(QCoreApplication.translate("ColorLog", u"\uceec\ub7ec\ub85c\uadf8(color log)\n"
"\n"
" \uc774 \ucee8\ud150\uce20\ub294 \uc21c\ucc9c\ud5a5\ub300\ud559\uad50\n"
" \uc0ac\ubb3c\uc778\ud130\ub137\ud559\uacfc \uc878\uc5c5\uc791\ud488\uc124\uacc4\ub97c \uc704\ud574 \uc81c\uc791\ub41c\n"
" \ud37c\uc2a4\ub110 \uceec\ub7ec \uc9c4\ub2e8 \ud3ec\ud1a0\ubd80\uc2a4 \uc785\ub2c8\ub2e4.\n"
" \ud37c\uc2a4\ub110 \uceec\ub7ec \uc9c4\ub2e8 \ubc1b\uace0 \uadf8 \uacb0\uacfc\uc5d0 \ub9de\uac8c \uc0ac\uc9c4 \ucd2c\uc601\uc744 \ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.\n"
" \uc790\uc2e0\uc5d0\uac8c \ub9de\ub294 \uc0c9\uc744 \ucc3e\uc544\uac00\uc138\uc694.\n"
"\n"
" -\uc0ac\ubb3c\uc778\ud130\ub137\ud559\uacfc 20\ud559\ubc88 \uc784\uc11c\ud604-     -\uc0ac\ubb3c\uc778\ud130\ub137\ud559\uacfc 20\ud559\ubc88 \uc1a1\ud76c\uc218-\n"
" -\uc0ac\ubb3c\uc778\ud130\ub137\ud559\uacfc 20\ud559\ubc88 \ud55c\uc0c1\uc544-     -\uc0ac\ubb3c\uc778\ud130\ub137\ud559\uacfc 20\ud559\ubc88 \uc5ec\ud558\ub298-", None))
        self.ex3.setText(QCoreApplication.translate("ColorLog", u"\uc9c4\ub2e8 \uacb0\uacfc\uac00 \ub098\uc624\ub294 \uc911\uc785\ub2c8\ub2e4.\n"
" \uc7a0\uc2dc\ub9cc \uae30\ub2e4\ub824 \uc8fc\uc138\uc694.", None))
        self.loading2.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("ColorLog", u"\ub118\uc5b4\uac00\uae30", None))
        self.smallLogo4.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.back2.setText("")
        self.back1.setText("")
        self.ex5.setText(QCoreApplication.translate("ColorLog", u"\ub2f9\uc2e0\uc5d0\uac8c \uaf2d \ub9de\ub294\n"
"\ub124\ucef7 \uc0ac\uc9c4\uc744 \ucd2c\uc601\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.next.setText(QCoreApplication.translate("ColorLog", u"\uc0ac\uc9c4 \ucd2c\uc601\uc73c\ub85c\n"
"\ub118\uc5b4\uac00\uc2dc\uaca0\uc2b5\ub2c8\uae4c?", None))
        self.ex6.setText(QCoreApplication.translate("ColorLog", u"\uc9c4\ub2e8 \uacb0\uacfc\ub294 \ucd2c\uc601 \uc774\ud6c4 QR\ucf54\ub4dc\ub97c \ud1b5\ud574\n"
"\ub2e4\uc2dc \ud655\uc778\ud558\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        self.title.setText(QCoreApplication.translate("ColorLog", u"\ub2f9\uc2e0\uc758 \ud37c\uc2a4\ub110\uceec\ub7ec\ub294?", None))
        self.faceColor.setText(QCoreApplication.translate("ColorLog", u"\ub2f9\uc2e0\uc758 \uc5bc\uad74\uc5d0 \ub9de\ub294 \uc0c9\uc0c1", None))
        self.facePhoto.setText(QCoreApplication.translate("ColorLog", u"\uc5bc\uad74\uc0ac\uc9c4", None))
        self.recoColor.setText(QCoreApplication.translate("ColorLog", u"\uc0c9\uc0c1\ucd94\ucc9c", None))
        self.colorPalette.setText(QCoreApplication.translate("ColorLog", u"\uceec\ub7ec\ud314\ub808\ud2b8", None))
        self.ex4.setText(QCoreApplication.translate("ColorLog", u"\ub2f9\uc2e0\uc758 \uc5bc\uad74\uc5d0\uc11c \ucd94\ucd9c\ud55c \uc0c9\uc0c1", None))
        self.pushButton_5.setText(QCoreApplication.translate("ColorLog", u"80 \u2192", None))
        self.smallLogo5.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.pushButton_6.setText(QCoreApplication.translate("ColorLog", u"\ucd2c\uc601\ud558\uae30", None))
        self.light.setText(QCoreApplication.translate("ColorLog", u"\uc5b4\uc6b8\ub9ac\ub294 \uc870\uba85", None))
        self.ex7.setText(QCoreApplication.translate("ColorLog", u"\uc870\uba85\uc744 \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.select2.setText("")
        self.select3.setText("")
        self.select1.setText("")
        self.select_1.setText(QCoreApplication.translate("ColorLog", u"\ud30c\ub780\uc0c9", None))
        self.select_2.setText(QCoreApplication.translate("ColorLog", u"\ub178\ub780\uc0c9", None))
        self.select_3.setText(QCoreApplication.translate("ColorLog", u"\ubcf4\ub77c\uc0c9", None))
        self.timer3.setText(QCoreApplication.translate("ColorLog", u"\uc81c\ud55c\uc2dc\uac04", None))
        self.smallLogo6.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.timer_3.setText(QCoreApplication.translate("ColorLog", u"30", None))
        self.loading3.setText("")
        self.ex8.setText(QCoreApplication.translate("ColorLog", u"\uc0ac\uc9c4 \ucd2c\uc601 \uc911\uc785\ub2c8\ub2e4. \uc790\uc720\ub86d\uac8c \ud3ec\uc988\ub97c \ucde8\ud574 \uc8fc\uc138\uc694.", None))
        self.camera3.setText(QCoreApplication.translate("ColorLog", u"\uce74\uba54\ub77c\ub97c \ubd88\ub7ec\uc624\ub294 \uc911\uc785\ub2c8\ub2e4", None)) # changed
        # self.pushButton_7.setText(QCoreApplication.translate("ColorLog", u"\ub118\uc5b4\uac00\uae30", None))
        self.smallLogo7.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.label_2.setText(QCoreApplication.translate("ColorLog", u"\ub0a8\uc740 \ucd2c\uc601 \uc218", None))
        self.num_2.setText(QCoreApplication.translate("ColorLog", u"0 / 4", None))
        self.finalPhoto.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784", None))
        self.pushButton_8.setText(QCoreApplication.translate("ColorLog", u"\ucd9c\ub825\ud558\uae30", None))
        self.color1.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784", None))
        self.ex9.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784\uc744 \uc120\ud0dd\ud574\uc8fc\uc138\uc694.", None))
        self.frame.setText(QCoreApplication.translate("ColorLog", u"\uc5b4\uc6b8\ub9ac\ub294 \ud504\ub808\uc784", None))
        self.timer_4.setText(QCoreApplication.translate("ColorLog", u"30", None))
        self.smallLogo8.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.timer4.setText(QCoreApplication.translate("ColorLog", u"\uc81c\ud55c\uc2dc\uac04", None))
        self.color2.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784", None))
        self.color3.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784", None))
        self.back3.setText("")
        self.ex12.setText(QCoreApplication.translate("ColorLog", u"\ub193\uace0 \uac00\uc2dc\ub294 \ubb3c\uac74\uc774 \uc5c6\ub294\uc9c0 \n"
"\ud655\uc778\ud574\uc8fc\uc138\uc694.", None))
        self.ex11.setText(QCoreApplication.translate("ColorLog", u"\ucd2c\uc601\uc774 \uc644\ub8cc\ub418\uc5c8\uc2b5\ub2c8\ub2e4.\n"
"\uc544\ub798\uc5d0\uc11c \ucd9c\ub825\ub418\ub294 \uc0ac\uc9c4\uc744 \n"
"\ucc59\uaca8\uc8fc\uc138\uc694.", None))
        self.ex10.setText(QCoreApplication.translate("ColorLog", u"\uc0ac\uc9c4\uc744 \ucd9c\ub825 \uc911\uc785\ub2c8\ub2e4.", None))
        self.loading4.setText("")
        self.pushButton_9.setText(QCoreApplication.translate("ColorLog", u"\uc885\ub8cc", None))
        self.smallLogo9.setText(QCoreApplication.translate("ColorLog", u"ColorLog", None))
        self.finalPhoto2.setText(QCoreApplication.translate("ColorLog", u"\ud504\ub808\uc784", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ColorLog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
