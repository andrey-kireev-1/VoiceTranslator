################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect,
    QSize)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QGridLayout, QLabel,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextBrowser, QWidget)

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Переводчик")
        MainWindow.resize(1051, 342)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #212529;\n"
"	font-family: Rubik;\n"
"	font-weight: 400;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #888;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 80, 1031, 211))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.right_text = QTextBrowser(self.gridLayoutWidget)
        self.right_text.setObjectName(u"right_text")
        self.right_text.setStyleSheet(u"background-color: #161b22;")

        self.gridLayout.addWidget(self.right_text, 1, 2, 1, 1)

        self.left_text = QTextBrowser(self.gridLayoutWidget)
        self.left_text.setObjectName(u"left_text")
        self.left_text.setStyleSheet(u"background-color: #161b22;")

        self.gridLayout.addWidget(self.left_text, 1, 0, 1, 1)

        self.btn_lang = QPushButton(self.gridLayoutWidget)
        self.btn_lang.setObjectName(u"btn_lang")
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(12)
        font.setBold(False)
        self.btn_lang.setFont(font)

        self.gridLayout.addWidget(self.btn_lang, 0, 1, 1, 1)

        self.left_label = QLabel(self.gridLayoutWidget)
        self.left_label.setObjectName(u"left_label")
        self.left_label.setFont(font)

        self.gridLayout.addWidget(self.left_label, 0, 0, 1, 1)

        self.right_label = QLabel(self.gridLayoutWidget)
        self.right_label.setObjectName(u"right_label")
        self.right_label.setFont(font)

        self.gridLayout.addWidget(self.right_label, 0, 2, 1, 1)

        self.btn_trans = QPushButton(self.gridLayoutWidget)
        self.btn_trans.setObjectName(u"btn_trans")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_trans.sizePolicy().hasHeightForWidth())
        self.btn_trans.setSizePolicy(sizePolicy)
        self.btn_trans.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/mic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_trans.setIcon(icon)
        self.btn_trans.setIconSize(QSize(50, 50))
        self.btn_trans.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btn_trans, 1, 1, 2, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 221, 61))
        font1 = QFont()
        font1.setFamilies([u"Rubik"])
        font1.setPointSize(22)
        font1.setBold(False)
        self.label.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1051, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Переводчик", None))
        self.btn_lang.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043c\u0435\u043d\u0438\u0442\u044c \u044f\u0437\u044b\u043a", None))
        self.left_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439", None))
        self.right_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0443\u0441\u0441\u043a\u0438\u0439", None))
        self.btn_trans.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0434\u0447\u0438\u043a", None))
    # retranslateUi

