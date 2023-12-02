# -*- coding: utf-8 -*-
import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QAction, QLineEdit, QLabel

from data_base.analyse import settings, settings_init_check, getAccountTmp, getPasswordTmp, loginAccount, \
    reservePassword
from view.frame import Frame
from view.font import setFont
from view.registerFrame import RegisterFrame
from view.resetPasswordFrame import ResetPasswordFrame
from control import func


# from init import init


class LogInFrame(object):
    # qss = "border:dotted;border-color:red"
    def __init__(self):
        self.frame = Frame()
        self.frame.resize(900, 780)
        self.frame.setFixedSize(self.frame.width(), self.frame.height())
        self.frame.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.addAccount()
        self.addPassword()
        self.addLoginButton()
        self.addRegisterButton()
        self.addForgetPasswordButton()
        self.addLoginAutoCheckBox()
        self.addRemPasswordCheckBox()
        self.addMovingBack()
        self.frame.addButtons()
        self.settings_init()
        self.addWarningLabel()
        # self.frame.show()
        self.counter = 0
        self.frame.quitButton.clicked.connect(
            lambda: reservePassword(self.accountEdit.text(), self.passwordEdit.text()))
        self.timer = QTimer()
        self.timer.timeout.connect(self.loginAutoCheck)
        self.timer.start(1000)

    def settings_init(self):
        check_list = settings_init_check()
        self.loginAutoCheckBox.setChecked(check_list[0])
        self.remPasswordCheckBox.setChecked(check_list[1])
        self.accountEdit.setText(getAccountTmp())
        if check_list[1]:
            self.passwordEdit.setText(getPasswordTmp())
        # if check_list[0] and len(self.passwordEdit.text()) > 0:
        #     # time.sleep(1)
        #     self.login_check()

    def loginAutoCheck(self):
        check_list = settings_init_check()
        self.timer.stop()
        if check_list[0] and len(self.passwordEdit.text()) > 0:
            self.login_check()

    def addAccount(self):
        self.accountEdit = QtWidgets.QLineEdit(self.frame)
        self.accountEdit.setGeometry(QtCore.QRect(200, 430, 500, 60))
        self.accountEdit.setObjectName("accountEdit")
        self.accountAction = QAction(self.accountEdit)
        self.accountAction.setIcon(QIcon("./pic/账号.png"))
        self.accountEdit.addAction(self.accountAction, QLineEdit.LeadingPosition)
        self.accountEdit.setPlaceholderText("账号")
        self.accountEdit.setFont(setFont(14))
        self.accountEdit.setCursorPosition(0)  # 设置光标位置
        self.accountEdit.setAlignment(Qt.AlignCenter)
        self.accountEdit.setStyleSheet("border-style:solid;border-top-width:0px;border-right-width:"
                                       "0px;border-bottom-width:2px;border-left-width:0px;")

    def addPassword(self):
        self.passwordEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordEdit.setGeometry(QtCore.QRect(200, 500, 500, 60))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordAction = QAction(self.accountEdit)
        self.passwordAction.setIcon(QIcon("./pic/密码.png"))
        self.passwordEdit.addAction(self.passwordAction, QLineEdit.LeadingPosition)
        self.passwordEdit.setPlaceholderText("密码")
        self.passwordEdit.setFont(setFont(14))
        self.passwordEdit.setCursorPosition(6)  # 设置光标位置
        self.passwordEdit.setAlignment(Qt.AlignCenter)
        self.passwordEdit.setStyleSheet("border-style:solid;border-top-width:0px;border-right-width:"
                                        "0px;border-bottom-width:2px;border-left-width:0px;")

    def addLoginButton(self):
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(200, 630, 500, 60))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setText("登录")
        self.loginButton.setFont(setFont(12))
        self.loginButton.clicked.connect(self.login_check)
        self.loginButton.setStyleSheet(
            "min-width:480;min-height:40;max-width:500;max-height:60;"
            "border-radius:10;background-color:rgb(176,224,230)")

    def addRegisterButton(self):
        self.registerButton = QtWidgets.QPushButton(self.frame)
        self.registerButton.setGeometry(QtCore.QRect(0, 700, 200, 50))
        self.registerButton.setFlat(True)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setText("注册账号")
        self.registerButton.setFont(setFont(10))
        self.registerButton.clicked.connect(self.register)

    def register(self):
        re = RegisterFrame()

    def addForgetPasswordButton(self):
        self.forgetPasswordButton = QtWidgets.QPushButton(self.frame)
        self.forgetPasswordButton.setGeometry(QtCore.QRect(550, 570, 200, 50))
        self.forgetPasswordButton.setFlat(True)
        self.forgetPasswordButton.setObjectName("forgetPasswordButton")
        self.forgetPasswordButton.setText("忘记密码")
        self.forgetPasswordButton.setFont(setFont(10))
        self.forgetPasswordButton.clicked.connect(self.forgetPassword)

    def forgetPassword(self):
        fp = ResetPasswordFrame()

    def addLoginAutoCheckBox(self):
        self.loginAutoCheckBox = QtWidgets.QCheckBox(self.frame)
        self.loginAutoCheckBox.setGeometry(QtCore.QRect(200, 570, 200, 50))
        self.loginAutoCheckBox.setObjectName("loginAutoCheckBox")
        self.loginAutoCheckBox.setText("自动登录")
        self.loginAutoCheckBox.setFont(setFont(10))
        self.loginAutoCheckBox.stateChanged.connect(lambda: settings("loginAuto", self.loginAutoCheckBox.isChecked()))

    def addRemPasswordCheckBox(self):
        self.remPasswordCheckBox = QtWidgets.QCheckBox(self.frame)
        self.remPasswordCheckBox.setGeometry(QtCore.QRect(390, 570, 200, 50))
        self.remPasswordCheckBox.setObjectName("remPasswordCheckBox")
        self.remPasswordCheckBox.setText("记住密码")
        self.remPasswordCheckBox.setFont(setFont(10))
        self.remPasswordCheckBox.stateChanged.connect(
            lambda: settings("reservePassword", self.remPasswordCheckBox.isChecked()))

    def addMovingBack(self):
        self.image_label = QLabel(self.frame)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 900, 400))
        self.image_label.move(int(self.image_label.width() / 2 - self.image_label.width() / 2), 0)
        self.pm = QPixmap("./pic/background/b1.jpg")
        self.pm.scaled(900, 400)
        self.image_label.setPixmap(self.pm)
        self.timer = QTimer(self.frame)
        self.timer.timeout.connect(self.timer_out)
        self.timer.start(2000)
        self.image_label.setScaledContents(True)

    def timer_out(self):
        self.counter += 1
        if self.counter > 5:
            self.counter = 1
        self.image_label.move(self.image_label.width() / 2 - self.image_label.width() / 2, 0)
        self.cur_pic_path = "./pic/background/b" + str(self.counter) + ".jpg"
        self.pm = QPixmap(self.cur_pic_path)
        self.pm.scaled(900, 400)
        self.image_label.setPixmap(self.pm)

    def login_check(self):
        check = loginAccount(self.accountEdit.text(), self.passwordEdit.text())
        if check:
            func.user = self.accountEdit.text()
            func.changepage()
            # stats.window.show()
            reservePassword(self.accountEdit.text(), self.passwordEdit.text())
            self.frame.close()
        else:
            self.warningTextsLabel.setVisible(True)
            self.warningImageLabel.setVisible(True)

    def addWarningLabel(self):
        self.labelImage = QPixmap("./pic/warning.png")
        self.labelImage.scaled(30, 30)
        self.warningImageLabel = QLabel(self.frame)
        self.warningTextsLabel = QLabel(self.frame)
        self.warningImageLabel.setPixmap(self.labelImage)
        self.warningImageLabel.setScaledContents(True)
        self.warningTextsLabel.setText("账号不存在或密码错误")
        self.warningTextsLabel.setFont(setFont(10))
        self.warningImageLabel.setVisible(False)
        self.warningTextsLabel.setVisible(False)
        self.warningTextsLabel.setGeometry(QtCore.QRect(320, 700, 500, 30))
        self.warningImageLabel.setGeometry(QtCore.QRect(270, 700, 30, 30))
        self.warningTextsLabel.setStyleSheet("color:red")
