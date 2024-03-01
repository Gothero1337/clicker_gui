# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resqrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"background-color: #2A2B2B;\n"
"font-family: Montserrat;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.score_text = QLabel(self.centralwidget)
        self.score_text.setObjectName(u"score_text")
        self.score_text.setStyleSheet(u"color: #F6F6F6;\n"
"font-weight: bold;\n"
"font-size: 12pt;\n"
"padding-left: 5%;\n"
"")

        self.verticalLayout.addWidget(self.score_text)

        self.score = QLabel(self.centralwidget)
        self.score.setObjectName(u"score")
        self.score.setStyleSheet(u"color: #F6F6F6;\n"
"padding-left: 5%;\n"
"font-size: 18pt;\n"
"padding-bottom: 450%")

        self.verticalLayout.addWidget(self.score)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sawka_img = QLabel(self.centralwidget)
        self.sawka_img.setObjectName(u"sawka_img")
        self.sawka_img.setMinimumSize(QSize(439, 434))
        self.sawka_img.setMaximumSize(QSize(439, 434))
        self.sawka_img.setStyleSheet(u"background-color: green;\n"
"\n"
"margin-left: 30%;\n"
"margin-right: 30%;")
        self.sawka_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.sawka_img)

        self.btn_main = QPushButton(self.centralwidget)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setStyleSheet(u"QPushButton {\n"
"background-color: #F6F6F6;\n"
"font-size: 30pt;\n"
"border-radius: 30px;\n"
"padding: 10%;\n"
"color: #2A2B2B;\n"
"font-weight: bold;\n"
"margin: 15%;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(246,246,246, 20);\n"
"color: #F6F6F6;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.btn_main)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"border: 1px solid grey;\n"
"border-radius: 10px;\n"
"background-color: #f6f6f6;\n"
"padding: 5%;\n"
"}\n"
"QProgressBar::chunk {\n"
"background-color: #37c0fa;\n"
"width: 10px;\n"
"margin: 0px;\n"
"}")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.img_beer = QLabel(self.centralwidget)
        self.img_beer.setObjectName(u"img_beer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img_beer.sizePolicy().hasHeightForWidth())
        self.img_beer.setSizePolicy(sizePolicy1)
        self.img_beer.setMinimumSize(QSize(157, 225))
        self.img_beer.setMaximumSize(QSize(157, 225))
        self.img_beer.setStyleSheet(u"background-color: none;")
        self.img_beer.setPixmap(QPixmap(u":/icons/icons/essa.png"))
        self.img_beer.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.img_beer)

        self.btn_beer = QPushButton(self.centralwidget)
        self.btn_beer.setObjectName(u"btn_beer")
        self.btn_beer.setStyleSheet(u"QPushButton {\n"
"background-color: #F6F6F6;\n"
"font-size: 10pt;\n"
"border-radius: 10px;\n"
"padding: 10%;\n"
"color: #2A2B2B;\n"
"font-weight: bold;\n"
"margin: 10%;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(246,246,246, 20);;\n"
"color: #F6F6F6\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_beer)

        self.img_hqd = QLabel(self.centralwidget)
        self.img_hqd.setObjectName(u"img_hqd")
        self.img_hqd.setMaximumSize(QSize(157, 225))
        self.img_hqd.setStyleSheet(u"background-color: none;")
        self.img_hqd.setPixmap(QPixmap(u":/icons/icons/hqd.png"))
        self.img_hqd.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.img_hqd)

        self.btn_hqd = QPushButton(self.centralwidget)
        self.btn_hqd.setObjectName(u"btn_hqd")
        self.btn_hqd.setStyleSheet(u"QPushButton {\n"
"background-color: #F6F6F6;\n"
"font-size: 10pt;\n"
"border-radius: 10px;\n"
"padding: 10%;\n"
"color: #2A2B2B;\n"
"font-weight: bold;\n"
"margin: 10%;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(246,246,246, 20);\n"
"color: #F6F6F6\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_hqd)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SAWKA2D", None))
        self.score_text.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0440\u0443\u043f\u044b \u0420\u044b\u0431\u0438\u043d\u0441\u043a\u0430:", None))
        self.score.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.sawka_img.setText("")
        self.btn_main.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0410\u0412\u0418\u0422\u042c", None))
        self.img_beer.setText("")
        self.btn_beer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0420\u041e\u041f\u0418\u0422\u042c", None))
        self.img_hqd.setText("")
        self.btn_hqd.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041b\u041e\u041f\u041d\u0423\u0422\u042c \u0422\u042f\u0413\u0423", None))
    # retranslateUi

