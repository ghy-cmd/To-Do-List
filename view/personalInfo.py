import json
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication

from view.font import setFont
from view.frame import Frame

css = "border-style:solid;border-top-width:0px;border-right-width:" + \
      "0px;border-bottom-width:1px;border-left-width:0px;"


class PersonalInfoFrame(object):
    def __init__(self, account):
        self.frame = Frame()
        self.frame.resize(800, 1000)
        self.frame.addButtons()
        self.getPersonInfo(account)
        self.addEdits()
        # self.frame.show()

    def addEdits(self):
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 200, 600, 700))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("Account")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("Name")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("StudentId")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("PersonId")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label.setText("Account   :")
        self.label_2.setText("Name      :")
        self.label_3.setText("StudentId :")
        self.label_4.setText("PersonId  :")
        self.lineEdit.setText(self.personInfo['account'])
        self.lineEdit_2.setText(self.personInfo['name'])
        self.lineEdit_3.setText(self.personInfo['stu_num'])
        self.lineEdit_4.setText(self.personInfo['per_num'])
        self.label.setFont(setFont(14))
        self.label_2.setFont(setFont(14))
        self.label_3.setFont(setFont(14))
        self.label_4.setFont(setFont(14))
        self.lineEdit.setFont(setFont(14))
        self.lineEdit_2.setFont(setFont(14))
        self.lineEdit_3.setFont(setFont(14))
        self.lineEdit_4.setFont(setFont(14))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit_2.setAlignment(Qt.AlignCenter)
        self.lineEdit_3.setAlignment(Qt.AlignCenter)
        self.lineEdit_4.setAlignment(Qt.AlignCenter)
        self.lineEdit.setStyleSheet(css)
        self.lineEdit_2.setStyleSheet(css)
        self.lineEdit_3.setStyleSheet(css)
        self.lineEdit_4.setStyleSheet(css)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4.setReadOnly(True)
        self.label.setStyleSheet("color:red")
        self.label_2.setStyleSheet("color:red")
        self.label_3.setStyleSheet("color:red")
        self.label_4.setStyleSheet("color:red")
        self.title = QtWidgets.QLabel(self.frame)
        self.title.setText("个人信息")
        font = QFont()
        font.setFamily("方正舒体")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setGeometry(QtCore.QRect(100, 50, 600, 200))
        self.title.setStyleSheet("color:red")


    def getPersonInfo(self, account):
        user_info_file = open("./data_base/user_info.json", "r", encoding="GBK")
        user_info = json.load(user_info_file)
        user_info_file.close()
        for info in user_info:
            if info['account'] == account:
                self.personInfo = info
                break
        user_info_file = open("./data_base/user_info.json", "w")
        json.dump(user_info, user_info_file, indent=2, ensure_ascii=False)
        user_info_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = PersonalInfoFrame("wit23")
    sys.exit(app.exec())
