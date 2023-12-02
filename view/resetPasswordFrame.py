import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel

from data_base.analyse import checkAccountInfo, resetPassword
from view.frame import Frame
from view.font import setFont


class ResetPasswordFrame:
    css = "min-width:580;min-height:50;max-width:600;max-height:70;" \
          "border-radius:10px;background-color:rgb(242,242,242);"

    def __init__(self):
        self.flag = False
        self.frame = Frame()
        self.frame.resize(800, 900)
        self.frame.setObjectName("frame")
        self.setLayout()
        self.addAccountEdit()
        self.addLabel()
        self.addNameEdit()
        self.addQuestionEdit()
        self.addPasswordEdit()
        self.addPasswordConfirm()
        self.addCheckInfoErrorLabel()
        self.addResetButton()
        self.frame.addButtons()
        self.addWarningLabel()
        self.addHideButton()
        self.frame.show()
        self.check = [False for i in range(2)]

    def frame_init(self):
        self.palette = QPalette(self.frame)
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/../pic/背景.jpg")))
        self.frame.setPalette(self.palette)

    def setLayout(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 100, 600, 800))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

    def addAccountEdit(self):
        self.accountEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.accountEdit.setObjectName("accountEdit")
        self.accountEdit.setPlaceholderText("输入账号名称")
        self.accountEdit.setFont(setFont(14))
        self.accountEdit.setCursorPosition(6)  # 设置光标位置
        self.accountEdit.setAlignment(Qt.AlignCenter)
        self.accountEdit.setStyleSheet(self.css)
        self.verticalLayout.addWidget(self.accountEdit)

    def addPasswordEdit(self):
        self.passwordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit.setPlaceholderText("设置密码")
        self.passwordEdit.setFont(setFont(14))
        self.passwordEdit.setCursorPosition(6)  # 设置光标位置
        self.passwordEdit.setAlignment(Qt.AlignCenter)
        self.passwordEdit.setStyleSheet(self.css)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.textEdited.connect(lambda: self.textCheck(1))
        self.passwordEdit.setVisible(False)
        self.hideButton = QPushButton(self.frame)
        self.hideButton.setIcon(QIcon("../../pic/隐藏.png"))
        self.hideButton.setIconSize(QtCore.QSize(30, 30))
        self.hideButton.setGeometry(QtCore.QRect(700, 490, 60, 60))
        self.hideButton.setFlat(True)
        self.hideButton.setVisible(False)
        self.hideButton.clicked.connect(self.changeVisibility)
        self.hideButton.setStyleSheet("background-color:transparent")
        self.verticalLayout.addWidget(self.passwordEdit)

    def changeVisibility(self):
        if self.passwordEditConfirm.echoMode() == QtWidgets.QLineEdit.Password:
            self.passwordEditConfirm.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordEditConfirm.setEchoMode(QtWidgets.QLineEdit.Password)

    def addPasswordConfirm(self):
        self.passwordEditConfirm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passwordEditConfirm.setObjectName("passwordEditConfirm")
        self.passwordEditConfirm.setPlaceholderText("重复密码")
        self.passwordEditConfirm.setFont(setFont(14))
        self.passwordEditConfirm.setCursorPosition(6)  # 设置光标位置
        self.passwordEditConfirm.setAlignment(Qt.AlignCenter)
        self.passwordEditConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEditConfirm.setStyleSheet(self.css)
        self.passwordEditConfirm.setVisible(False)
        self.passwordEditConfirm.textEdited.connect(lambda: self.textCheck(2))
        self.verticalLayout.addWidget(self.passwordEditConfirm)

    def addNameEdit(self):
        self.nameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setFont(setFont(14))
        self.nameEdit.setAlignment(Qt.AlignCenter)
        self.nameEdit.setPlaceholderText("请输入你的名字")
        self.nameEdit.setStyleSheet(self.css)
        self.verticalLayout.addWidget(self.nameEdit)

    def addQuestionEdit(self):
        self.questionEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.questionEdit_1.setObjectName("questionEdit_1")
        self.questionEdit_1.setFont(setFont(14))
        self.questionEdit_1.setAlignment(Qt.AlignCenter)
        self.questionEdit_1.setPlaceholderText("请输入你的学号")
        self.verticalLayout.addWidget(self.questionEdit_1)
        self.questionEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.questionEdit_2.setObjectName("questionEdit_2")
        self.questionEdit_2.setFont(setFont(14))
        self.questionEdit_2.setAlignment(Qt.AlignCenter)
        self.questionEdit_2.setPlaceholderText("请输入你的身份证后六位")
        self.questionEdit_1.setStyleSheet(self.css)
        self.questionEdit_2.setStyleSheet(self.css)
        self.verticalLayout.addWidget(self.questionEdit_2)

    def addLabel(self):
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("Reset your password!")
        self.label.setGeometry(QtCore.QRect(100, 0, 600, 150))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setFamily("方正舒体")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setStyleSheet("color:#FA8072")
        self.label.setFont(font)

    def addResetButton(self):
        self.resetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.resetButton.setFont(setFont(10))
        self.resetButton.setObjectName("registerButton")
        self.resetButton.setText("下一步")
        self.resetButton.setStyleSheet(self.css + "background-color:rgb(176,224,230)")
        self.resetButton.clicked.connect(self.resetCheck)
        self.verticalLayout.addWidget(self.resetButton)

    def resetCheck(self):
        if self.flag is False:
            account = self.accountEdit.text()
            name = self.nameEdit.text()
            answer1 = self.questionEdit_1.text()
            answer2 = self.questionEdit_2.text()
            if checkAccountInfo(account, name, answer1, answer2):
                self.flag = True
                self.accountEdit.setReadOnly(True)
                self.nameEdit.setReadOnly(True)
                self.questionEdit_1.setReadOnly(True)
                self.questionEdit_2.setReadOnly(True)
                self.resetButton.setText("重置密码")
                self.passwordEdit.setVisible(True)
                self.errorImageLabel.setVisible(False)
                self.errorTextLabel.setVisible(False)
            else:
                self.errorImageLabel.setVisible(True)
                self.errorTextLabel.setVisible(True)
        else:
            if False in self.check:
                self.warningImageLabels[2].setVisible(True)
                self.warningTextsLabels[2].setVisible(True)
            else:
                resetPassword(self.accountEdit.text(), self.passwordEdit.text())
                self.frame.close()

    def textCheck(self, num):
        text = self.passwordEdit.text()
        if num == 1:
            if len(text) >= 8 and text.isalnum():
                self.passwordEditConfirm.setVisible(True)
                self.notHidden()
                self.hideButton.setVisible(True)
                self.check[0] = True
                self.warningTextsLabels[0].setVisible(False)
                self.warningImageLabels[0].setVisible(False)
            else:
                self.passwordEditConfirm.setVisible(False)
                self.hideButton.setVisible(False)
                self.hidden()
                self.check[0] = False
                self.warningTextsLabels[0].setVisible(True)
                self.warningImageLabels[0].setVisible(True)
        else:
            password = self.passwordEditConfirm.text()
            if password == text:
                self.warningTextsLabels[1].setVisible(True)
                self.warningImageLabels[1].setVisible(True)
                self.check[1] = True
            else:
                self.warningTextsLabels[1].setVisible(True)
                self.warningImageLabels[1].setVisible(True)
                self.check[1] = False

    def addCheckInfoErrorLabel(self):
        self.errorImageLabel = QLabel(self.frame)
        self.labelImage = QPixmap("../pic/warning.png")
        self.labelImage.scaled(30, 30)
        self.errorImageLabel.setPixmap(self.labelImage)
        self.errorImageLabel.setScaledContents(True)
        self.errorTextLabel = QLabel(self.frame)
        self.errorTextLabel.setText("账号信息有误，请再次检查")
        self.errorImageLabel.setVisible(False)
        self.errorTextLabel.setVisible(False)
        self.errorTextLabel.setFont(setFont(10))
        self.errorTextLabel.setStyleSheet("color:red")
        self.errorTextLabel.setGeometry(QtCore.QRect(250, 1070, 500, 30))
        self.errorImageLabel.setGeometry(QtCore.QRect(200, 1070, 30, 30))

    def addWarningLabel(self):
        self.labelImage = QPixmap("../pic/warning.png")
        self.labelImage.scaled(30, 30)
        self.warningImageLabels = [QLabel(self.frame) for i in range(3)]
        self.warningTextsLabels = [QLabel(self.frame) for i in range(3)]
        self.warningTexts = ["密码应是数字和字母的组合，且至少8位", "密码不一致", "请正确设置密码"]
        for i in range(3):
            self.warningImageLabels[i].setPixmap(self.labelImage)
            self.warningImageLabels[i].setScaledContents(True)
            self.warningTextsLabels[i].setText(self.warningTexts[i])
            self.warningTextsLabels[i].setFont(setFont(10))
            self.warningImageLabels[i].setVisible(False)
            self.warningTextsLabels[i].setVisible(False)
            self.warningTextsLabels[i].setStyleSheet("color:red")
        self.notHidden()
        self.warningTextsLabels[1].setGeometry(QtCore.QRect(200, 960, 500, 30))
        self.warningImageLabels[1].setGeometry(QtCore.QRect(150, 960, 30, 30))

    def hidden(self):
        self.warningTextsLabels[0].setGeometry(QtCore.QRect(200, 920, 500, 30))
        self.warningImageLabels[0].setGeometry(QtCore.QRect(150, 920, 30, 30))
        self.warningTextsLabels[2].setGeometry(QtCore.QRect(200, 1090, 500, 30))
        self.warningImageLabels[2].setGeometry(QtCore.QRect(150, 1090, 30, 30))

    def notHidden(self):
        self.warningTextsLabels[2].setGeometry(QtCore.QRect(200, 1100, 500, 30))
        self.warningImageLabels[2].setGeometry(QtCore.QRect(150, 1100, 30, 30))

    def addHideButton(self):
        self.hideButton = QPushButton(self.frame)
        self.hideButton.setIcon(QIcon("../pic/隐藏.png"))
        self.hideButton.setIconSize(QtCore.QSize(30, 30))
        self.hideButton.setGeometry(QtCore.QRect(690, 900, 60, 60))
        self.hideButton.setFlat(True)
        self.hideButton.setVisible(False)
        self.hideButton.clicked.connect(self.changeVisibility)
        self.hideButton.setStyleSheet("background-color:transparent")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = ResetPasswordFrame()
    sys.exit(app.exec())
