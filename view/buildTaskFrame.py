# -*- coding: utf-8 -*-
import sys
from enum import Enum

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QPushButton, QComboBox, \
    QLabel

from view.frame import Frame
from control import func


class Category(Enum):
    Default = 0
    Sport = 1
    Trip = 2
    Eat = 3
    Sleep = 4
    Music = 5
    Game = 6
    Study = 7
    Work = 8


class BuildTask(object):

    def __init__(self):
        self.setFont()
        self.frame = Frame()
        # self.frame.setStyleSheet("background-color:rgb(255,255,254")
        self.frame.setObjectName("frame")
        self.frame.resize(800, 900)
        self.addQuitButton()
        self.addFinishButton()
        self.addImageButton()
        self.addTitleEdit()
        self.addDescriptionEdit()
        self.addDateTimeEdit()
        self.addImportance()
        self.addCheckBox()
        self.setTitleImage("./pic/默认.png")
        # self.frame.show()

    def setFont(self):
        self.font_button = QtGui.QFont()
        self.font_button.setFamily("华文楷体")
        self.font_button.setPointSize(14)
        self.font_title = QtGui.QFont()
        self.font_title.setFamily("华文楷体")
        self.font_title.setPointSize(20)
        self.font_sign = QtGui.QFont()
        self.font_sign.setFamily("华文楷体")
        self.font_sign.setPointSize(10)

    def addQuitButton(self):
        self.pushButton_quit = QPushButton(self.frame)
        self.pushButton_quit.setGeometry(QtCore.QRect(15, 15, 80, 70))
        self.pushButton_quit.setFlat(True)
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.pushButton_quit.setStyleSheet("color:blue;background-color:rgb(255,255,255);border:none")
        self.pushButton_quit.setText(QtCore.QCoreApplication.translate("ScrollArea", "取消"))
        self.pushButton_quit.setFont(self.font_button)
        self.pushButton_quit.clicked.connect(self.quit)

    def quit(self):
        self.frame.close()

    def finish(self):
        title = self.titleEdit.text()
        description = self.desEdit.toPlainText()
        deadline = self.dateTimeEdit.dateTime()
        importance = self.horizontalSlider.value()
        category = self.titleImage.objectName()
        index = self.combox.currentIndex()
        year = deadline.date().year()
        month = deadline.date().month()
        day = deadline.date().day()
        hour = deadline.time().hour()
        minute = deadline.time().minute()
        seconds = deadline.time().second()
        if category == 'Sport':
            category = '运动'
        elif category == 'Trip':
            category = '旅游'
        elif category == 'Eat':
            category = '美食'
        elif category == 'Sleep':
            category = '睡觉'
        elif category == 'Music':
            category = '音乐'
        elif category == 'Game':
            category = '游戏'
        elif category == 'Study':
            category = '学习'
        elif category == 'Work':
            category = '工作'
        else:
            category = '默认'
        func.add_task(description, year, month, day, index, title, importance, hour, minute, seconds, category)
        self.frame.close()

    def addFinishButton(self):
        self.pushButton_finish = QtWidgets.QPushButton(self.frame)
        self.pushButton_finish.setGeometry(QtCore.QRect(710, 15, 80, 70))
        self.pushButton_finish.setFlat(True)
        self.pushButton_finish.setEnabled(False)
        self.pushButton_finish.setObjectName("pushButton_finish")
        self.pushButton_finish.setStyleSheet("color:rgb(192,192,192); background-color:rgb(255,255,255);border:none")
        self.pushButton_finish.setText(QtCore.QCoreApplication.translate("ScrollArea", "完成"))
        self.pushButton_finish.setFont(self.font_button)
        self.pushButton_finish.clicked.connect(self.finish)

    def finishButtonChanged(self):
        if len(self.titleEdit.text()) != 0:
            self.pushButton_finish.setEnabled(True)
            self.pushButton_finish.setStyleSheet("color:blue")
        else:
            self.pushButton_finish.setEnabled(False)
            self.pushButton_finish.setStyleSheet("color:rgb(192, 192, 192)")

    def setTitleImage(self, path):
        self.titleImage = QtWidgets.QPushButton(self.frame)
        self.titleImage.setGeometry(QtCore.QRect(320, 50, 70, 70))
        self.titleImage.setStyleSheet(
            "min-width:120;min-height:120;max-width:120;max-height:120;"
            "border-radius:60px;background-color:rgb(242,242,242)")
        self.titleImage.setObjectName(Category(0).name)
        self.titleImage.setIcon(QtGui.QIcon(path))
        self.titleImage.setIconSize(QtCore.QSize(70, 70))
        self.titleImage.clicked.connect(lambda: self.changeTitleImage("./pic/默认.png", Category(0).name))

    def changeTitleImage(self, path, title_name):
        self.titleImage.setIcon(QtGui.QIcon(path))
        self.titleImage.setIconSize(QtCore.QSize(70, 70))
        self.titleImage.setObjectName(title_name)

    def addTitleEdit(self):
        self.titleEdit = QtWidgets.QLineEdit(self.frame)
        self.titleEdit.setGeometry(QtCore.QRect(50, 280, 700, 60))
        self.titleEdit.setObjectName("titleEdit")
        self.titleEdit.setFont(self.font_title)
        self.titleEdit.setPlaceholderText("任务名称")
        self.titleEdit.setContextMenuPolicy(Qt.DefaultContextMenu)  # 右键目录
        self.titleEdit.setCursorPosition(6)  # 设置光标位置
        self.titleEdit.setAlignment(Qt.AlignCenter)  # 居中
        self.titleEdit.setClearButtonEnabled(False)  # 清除按钮
        self.titleEdit.setStyleSheet(
            "min-width:700;min-height:60;max-width:700;max-height:60;"
            "border-radius:15;background-color:rgb(242,242,242)")
        self.titleEdit.cursorPositionChanged.connect(self.finishButtonChanged)

    def addDescriptionEdit(self):
        self.desLabel = QtWidgets.QLabel(self.frame)
        self.desLabel.setText("任务描述:")
        self.desLabel.setGeometry(QtCore.QRect(50, 345, 700, 30))
        self.desLabel.setAlignment(Qt.AlignVCenter)
        self.desLabel.setObjectName("label")
        self.desLabel.setFont(self.font_button)
        self.desEdit = QtWidgets.QTextEdit(self.frame)
        self.desEdit.setGeometry(QtCore.QRect(50, 380, 700, 180))
        self.desEdit.setPlaceholderText("\n\t在此添加任务的描述性消息\n\t点击上方图标可设置任务类别")
        self.desEdit.setObjectName("desEdit")
        self.desEdit.setFont(self.font_button)
        self.desEdit.setContextMenuPolicy(Qt.DefaultContextMenu)  # 右键目录
        self.desEdit.setAlignment(Qt.AlignVCenter)  # 居中
        self.desEdit.setTabStopWidth(32)
        self.desEdit.setStyleSheet(
            "min-width:700;min-height:150;max-width:700;max-height:180;"
            "border-radius:15;background-color:rgb(242,242,242)")

    def addDateTimeEdit(self):
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime(), self.frame)
        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setText("设置任务截止时间:")
        self.date_label.setGeometry(QtCore.QRect(50, 565, 700, 30))
        self.date_label.setAlignment(Qt.AlignVCenter)
        self.date_label.setObjectName("label")
        self.date_label.setFont(self.font_button)
        self.dateTimeEdit.setGeometry(QtCore.QRect(50, 600, 700, 60))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDisplayFormat("yyyy年-MM月-dd日   HH:mm:ss")
        self.dateTimeEdit.setFont(self.font_button)
        self.dateTimeEdit.setAlignment(Qt.AlignCenter)
        # self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setStyleSheet(
            "min-width:700;min-height:60;max-width:700;max-height:60;"
            "border-radius:15;background-color:rgb(242,242,242)")

    def addImportance(self):
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.importance_label = QtWidgets.QLabel(self.frame)
        self.importance_label.setText("设置任务优先级权重:")
        self.importance_label.setGeometry(QtCore.QRect(50,665, 900, 30))
        self.importance_label.setAlignment(Qt.AlignVCenter)
        self.importance_label.setObjectName("label")
        self.importance_label.setFont(self.font_button)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 700, 700, 70))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(9)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setSliderPosition(5)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.left_sign_label = QtWidgets.QLabel(self.frame)
        self.left_sign_label.setText("低优先级")
        self.left_sign_label.setGeometry(QtCore.QRect(50, 750, 200, 20))
        self.left_sign_label.setAlignment(Qt.AlignVCenter)
        self.left_sign_label.setObjectName("left_sign_label")
        self.left_sign_label.setFont(self.font_sign)
        self.right_sign_label = QtWidgets.QLabel(self.frame)
        self.right_sign_label.setText("高优先级")
        self.right_sign_label.setGeometry(QtCore.QRect(680, 750, 200, 20))
        self.right_sign_label.setAlignment(Qt.AlignVCenter)
        self.right_sign_label.setObjectName("right_sign_label")
        self.right_sign_label.setFont(self.font_sign)

    def addImageButton(self):
        self.imageButton1 = QPushButton(self.frame)
        self.imageButton2 = QPushButton(self.frame)
        self.imageButton3 = QPushButton(self.frame)
        self.imageButton4 = QPushButton(self.frame)
        self.imageButton5 = QPushButton(self.frame)
        self.imageButton6 = QPushButton(self.frame)
        self.imageButton7 = QPushButton(self.frame)
        self.imageButton8 = QPushButton(self.frame)
        self.setImageButton(self.imageButton1, "./pic/1.png", 1)
        self.setImageButton(self.imageButton2, "./pic/2.png", 2)
        self.setImageButton(self.imageButton3, "./pic/3.png", 3)
        self.setImageButton(self.imageButton4, "./pic/4.png", 4)
        self.setImageButton(self.imageButton5, "./pic/5.png", 5)
        self.setImageButton(self.imageButton6, "./pic/6.png", 6)
        self.setImageButton(self.imageButton7, "./pic/7.png", 7)
        self.setImageButton(self.imageButton8, "./pic/8.png", 8)

    def setImageButton(self, button, path, num):
        button.setObjectName(Category(num).name)
        button.setGeometry(QtCore.QRect(29 + (num - 1) * 96, 190, 40, 40))
        button.setObjectName(path)
        button.setStyleSheet(
            "min-width:70;min-height:70;max-width:70;max-height:70;"
            "border-radius:35px;background-color:rgb(242,242,242)")
        button.setIcon(QtGui.QIcon(path))
        button.setIconSize(QtCore.QSize(45, 45))
        button.clicked.connect(lambda: self.changeTitleImage(path, Category(num).name))

    def addCheckBox(self):
        self.boxLabel = QLabel(self.frame)
        self.boxLabel.setText("设置每日重复:")
        self.boxLabel.setFont(self.font_button)
        self.boxLabel.setGeometry(QtCore.QRect(50, 780, 300, 30))
        self.combox = QComboBox(self.frame)
        self.combox.addItem("不重复")
        self.combox.addItem("每日重复")
        self.combox.setFont(self.font_button)
        self.combox.setGeometry(QtCore.QRect(400, 780, 350, 50))
        self.combox.setStyleSheet("background-color:rgb(242,242,242)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    b = BuildTask()
    sys.exit(app.exec())
