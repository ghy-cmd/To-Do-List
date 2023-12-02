import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QBrush, QPixmap, QFont
from PyQt5.QtWidgets import QPushButton, QApplication, QLabel

from data_base.analyse import registerAccount, checkAccount
from view.frame import Frame
from view.font import setFont


class RegisterFrame:
    css = "min-width:580;min-height:50;max-width:600;max-height:70;" \
          "border-radius:10px;background-color:rgb(242,242,242);"

    def __init__(self):
        self.frame = Frame()
        self.frame.resize(800, 900)
        self.frame.setObjectName("frame")
        self.setLayout()
        self.addAccountEdit()
        self.addPasswordEdit()
        self.addPasswordConfirm()
        self.addLabel()
        self.addNameEdit()
        self.addQuestionEdit()
        self.addRegisterButton()
        self.frame.addButtons()
        self.addYesButtons()
        self.addWarningLabels()
        self.invisibleGeometry()
        self.edits = [self.accountEdit, self.passwordEdit, self.passwordEditConfirm, self.nameEdit,
                      self.questionEdit_1, self.questionEdit_2]
        self.frame.show()
        self.check = [False for i in range(6)]

    def frame_init(self):
        self.palette = QPalette(self.frame)
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap(":/./pic/背景.jpg")))
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
        self.accountEdit.setPlaceholderText("设置账号名称")
        self.accountEdit.setFont(setFont(14))
        self.accountEdit.setCursorPosition(6)  # 设置光标位置
        self.accountEdit.setAlignment(Qt.AlignCenter)
        self.accountEdit.setStyleSheet(self.css)
        self.accountEdit.textEdited.connect(lambda: self.textCheck(1))
        self.accountEdit.editingFinished.connect(self.account_check)
        self.verticalLayout.addWidget(self.accountEdit)

    def account_check(self):
        text = self.accountEdit.text()
        if checkAccount(text):
            self.warningTextsLabels[0].setText("账号已存在，请重新输入")
            self.warning(1)

    def addPasswordEdit(self):
        self.passwordEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        # self.passwordEdit.setGeometry(QtCore.QRect(100, 300, 600, 60))
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit.setPlaceholderText("设置密码")
        self.passwordEdit.setFont(setFont(14))
        self.passwordEdit.setCursorPosition(6)  # 设置光标位置
        self.passwordEdit.setAlignment(Qt.AlignCenter)
        self.passwordEdit.setStyleSheet(self.css)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.textEdited.connect(lambda: self.textCheck(2))
        self.hideButton = QPushButton(self.frame)
        self.hideButton.setIcon(QIcon("./pic/隐藏.png"))
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
        # self.passwordEditConfirm.setGeometry(QtCore.QRect(100, 400, 600, 60))
        self.passwordEditConfirm.setObjectName("passwordEditConfirm")
        self.passwordEditConfirm.setPlaceholderText("重复密码")
        self.passwordEditConfirm.setFont(setFont(14))
        self.passwordEditConfirm.setCursorPosition(6)  # 设置光标位置
        self.passwordEditConfirm.setAlignment(Qt.AlignCenter)
        self.passwordEditConfirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEditConfirm.setStyleSheet(self.css)
        self.passwordEditConfirm.setVisible(False)
        self.passwordEditConfirm.textEdited.connect(lambda: self.textCheck(3))
        self.verticalLayout.addWidget(self.passwordEditConfirm)

    def addNameEdit(self):
        self.nameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.nameEdit.setFont(setFont(14))
        self.nameEdit.setAlignment(Qt.AlignCenter)
        self.nameEdit.setPlaceholderText("请输入你的名字")
        self.nameEdit.setStyleSheet(self.css)
        self.nameEdit.textEdited.connect(lambda: self.textCheck(4))
        self.verticalLayout.addWidget(self.nameEdit)

    def addQuestionEdit(self):
        self.questionEdit_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        # self.questionEdit_1.setGeometry(QtCore.QRect(100, 600, 600, 60))
        self.questionEdit_1.setObjectName("questionEdit_1")
        self.questionEdit_1.setFont(setFont(14))
        self.questionEdit_1.setAlignment(Qt.AlignCenter)
        self.questionEdit_1.setPlaceholderText("请输入你的学号")
        self.verticalLayout.addWidget(self.questionEdit_1)
        self.questionEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        # self.questionEdit_2.setGeometry(QtCore.QRect(100, 800, 600, 60))
        self.questionEdit_2.setObjectName("questionEdit_2")
        self.questionEdit_2.setFont(setFont(14))
        self.questionEdit_2.setAlignment(Qt.AlignCenter)
        self.questionEdit_2.setPlaceholderText("请输入你的身份证后六位")
        self.questionEdit_1.setStyleSheet(self.css)
        self.questionEdit_2.setStyleSheet(self.css)
        self.questionEdit_1.textEdited.connect(lambda: self.textCheck(5))
        self.questionEdit_2.textEdited.connect(lambda: self.textCheck(6))
        self.verticalLayout.addWidget(self.questionEdit_2)

    def addLabel(self):
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText("Start to make your plans!")
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

    def addRegisterButton(self):
        self.registerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setText("立即注册")
        self.registerButton.setFont(setFont(14))
        self.registerButton.setStyleSheet(self.css + "background-color:rgb(176,224,230)")
        self.registerButton.clicked.connect(self.registerCheck)
        self.verticalLayout.addWidget(self.registerButton)

    def addYesButtons(self):
        self.path = "./pic/yes.png"
        self.buttons = [QPushButton(self.frame) for i in range(6)]
        for button in self.buttons:
            button.setIcon(QIcon(self.path))
            button.setIconSize(QtCore.QSize(30, 30))
            button.setStyleSheet("border:none;color:green")
            button.setVisible(False)
            button.setObjectName("yes_button")

    def addWarningLabels(self):
        self.labelImage = QPixmap("./pic/warning.png")
        self.labelImage.scaled(30, 30)
        self.warningImageLabels = [QLabel(self.frame) for i in range(7)]
        self.warningTextsLabels = [QLabel(self.frame) for i in range(7)]
        self.warningTexts = ["用户账号长度应在4-12位", "密码应是数字和字母的组合，且至少8位", "密码不一致",
                             "请输入中文名", "学号应为8位数字串", "格式不符合要求", "注册信息不完整"]
        for i in range(7):
            self.warningImageLabels[i].setPixmap(self.labelImage)
            self.warningImageLabels[i].setScaledContents(True)
            self.warningTextsLabels[i].setText(self.warningTexts[i])
            self.warningTextsLabels[i].setFont(setFont(10))
            self.warningImageLabels[i].setVisible(False)
            self.warningTextsLabels[i].setVisible(False)
            self.warningTextsLabels[i].setStyleSheet("color:red")

    def textCheck(self, num):
        text = self.edits[num - 1].text()
        if num == 1:
            if len(text) > 12 or len(text) < 4:
                self.warningTextsLabels[num - 1].setText("用户账号长度应在4-12位")
                self.warning(num)
            else:
                self.yes(num)
        elif num == 2:
            if len(text) >= 8 and text.isalnum():
                self.edits[num].setVisible(True)
                self.visibleGeometry()
                self.yes(num)
                self.hideButton.setVisible(True)
            else:
                self.warning(num)
                self.invisibleGeometry()
                self.edits[num].setVisible(False)
                self.hideButton.setVisible(False)
        elif num == 3:
            password = self.edits[1].text()
            if text == password:
                self.yes(num)
            else:
                self.warning(num)
        elif num == 4:
            if 2 <= len(text) <= 4 and self.isChinese(text):
                self.yes(num)
            else:
                self.warning(num)
        elif num == 5:
            if len(text) == 8 and text.isdigit():
                self.yes(num)
            else:
                self.warning(num)
        else:
            if len(text) == 6 and (text.isdigit() or text[0:5].isdigit() and text[5] == 'X'):
                self.yes(num)
            else:
                self.warning(num)

    def isChinese(self, string: str):
        for i in string:
            if not ('\u4e00' <= i <= '\u9fa5'):
                return False
        return True

    def registerCheck(self):
        if False in self.check:
            self.warning(6)
        else:
            registerAccount(self.accountEdit.text(), self.passwordEdit.text(), self.nameEdit.text(),
                            self.questionEdit_1.text(), self.questionEdit_2.text())
            self.frame.close()

    def warning(self, num):
        self.warningImageLabels[num - 1].setVisible(True)
        self.warningTextsLabels[num - 1].setVisible(True)
        self.buttons[num - 1].setVisible(False)
        self.check[num - 1] = False

    def yes(self, num):
        self.buttons[num - 1].setVisible(True)
        self.warningImageLabels[num - 1].setVisible(False)
        self.warningTextsLabels[num - 1].setVisible(False)
        self.check[num - 1] = True
        if False not in self.check:
            self.warningImageLabels[5].setVisible(False)
            self.warningTextsLabels[5].setVisible(False)

    def visibleGeometry(self):
        for i in range(6):
            self.buttons[i].setGeometry(QtCore.QRect(50, 240 + i * 135, 30, 30))
            self.warningImageLabels[i].setGeometry(QtCore.QRect(130, 295 + i * 135, 30, 30))
            self.warningTextsLabels[i].setGeometry(QtCore.QRect(180, 295 + i * 135, 500, 30))
        self.warningImageLabels[6].setGeometry(QtCore.QRect(130, 295 + 6 * 135, 30, 30))
        self.warningTextsLabels[6].setGeometry(QtCore.QRect(180, 295 + 6 * 135, 500, 30))

    def invisibleGeometry(self):
        for i in range(2):
            self.buttons[i].setGeometry(QtCore.QRect(50, 245 + i * 155, 30, 30))
            self.warningImageLabels[i].setGeometry(QtCore.QRect(130, 315 + i * 155, 30, 30))
            self.warningTextsLabels[i].setGeometry(QtCore.QRect(180, 315 + i * 155, 500, 30))
        for i in range(3, 6):
            self.buttons[i].setGeometry(QtCore.QRect(50, 245 + (i - 1) * 155, 30, 30))
            self.warningImageLabels[i].setGeometry(QtCore.QRect(130, 315 + (i - 1) * 155, 30, 30))
            self.warningTextsLabels[i].setGeometry(QtCore.QRect(180, 315 + (i - 1) * 155, 500, 30))
        self.warningImageLabels[6].setGeometry(QtCore.QRect(130, 315 + 5 * 155, 30, 30))
        self.warningTextsLabels[6].setGeometry(QtCore.QRect(180, 315 + 5 * 155, 500, 30))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = RegisterFrame()
    sys.exit(app.exec())
