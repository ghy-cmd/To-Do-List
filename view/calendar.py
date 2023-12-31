# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1304, 885)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(370, 15, 681, 306))
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 330, 1181, 546))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 40)
        self.tableWidget.setColumnWidth(2, 125)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setColumnWidth(4, 180)
        self.tableWidget.setColumnWidth(5, 80)
        self.tableWidget.setColumnWidth(6, 464)
        self.tableWidget.setColumnWidth(7, 160)
        # self.tableWidget.resizeRowsToContents()
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.tableWidget.horizontalHeader().setDefaultSectionSize(139)
        # self.tableWidget.horizontalHeader().setMinimumSectionSize(31)
        self.tableWidget.verticalHeader().setVisible(False)
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 280, 151, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(font)
        self.comboBox.addItem('所有')
        self.comboBox.addItem('未完成')
        self.comboBox.addItem('已完成')
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(52, 250, 100, 20))
        font.setFamily("幼圆")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 15, 271, 31))
        font.setFamily("楷体")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:rgb(0,47,167)")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(55, 55, 271, 20))
        font.setFamily("幼圆")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color:rgb(72,61,139)")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setFont(font)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setFont(font)
        item.setText(_translate("Form", "任务"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setFont(font)
        item.setText(_translate("Form", "状态"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setFont(font)
        item.setText(_translate("Form", "截止时间"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setFont(font)
        item.setText(_translate("Form", "类别"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setFont(font)
        item.setText(_translate("Form", "内容"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setFont(font)
        item.setText(_translate("Form", "操作"))
        self.label.setText(_translate("Form", "状态："))
        self.label_2.setText(_translate("Form", "日历系统"))
        # self.label_3.setText(_translate("Form", "根据日期筛选，可视化每日任务"))


