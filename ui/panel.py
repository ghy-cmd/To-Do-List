# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_panel(object):
    def setupUi(self, panel):
        panel.setObjectName("panel")
        panel.resize(1173, 885)
        font = QtGui.QFont()
        font.setFamily("黑体")
        panel.setFont(font)
        self.stackedWidget = QtWidgets.QStackedWidget(panel)
        self.stackedWidget.setGeometry(QtCore.QRect(210, 0, 954, 885))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.pushButton = QtWidgets.QPushButton(panel)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 141, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(panel)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 70, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(panel)
        QtCore.QMetaObject.connectSlotsByName(panel)

    def retranslateUi(self, panel):
        _translate = QtCore.QCoreApplication.translate
        panel.setWindowTitle(_translate("panel", "Form"))
        self.pushButton.setText(_translate("panel", "日历系统"))
        self.pushButton_2.setText(_translate("panel", "计划内"))
