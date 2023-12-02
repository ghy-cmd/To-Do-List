import json
import sys

from PyQt5.QtChart import QChart, QBarCategoryAxis, QBarSet, QBarSeries, QValueAxis, QDateTimeAxis, QLineSeries, \
    QPieSeries
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QTimer, QDateTime, QDate, QTime, QPointF
from PyQt5.QtWidgets import QApplication

from gene import g
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime
from view.buildTaskFrame import BuildTask
from view.alterTaskFrame import AlterTaskFrame
from view.personalInfo import PersonalInfoFrame

user = "ghyh"
index = 0


def index_change(self, ind):
    self.index = ind


def changepage():
    shuaxin()
    g.PanelPage.show()


def add_task_panel():
    BuildTask().frame.show()


def shuaxin():
    set_state()
    today_page()
    add_item(g.PanelDecorate.pageDecorate_ca.calendarWidget.selectedDate(),
             g.PanelDecorate.pageDecorate_ca.comboBox.currentText())
    add_item_onplan(g.PanelDecorate.pageDecorate_plan.comboBox.currentText())
    all_page()
    # show_data()


def set_state():
    cur = g.conn.cursor()
    sql = 'SELECT * FROM TASK WHERE USER=? AND COMPLETE=0 AND EVERYDAY=0'
    cur.execute(sql, (user,))
    res = cur.fetchall()
    for i in range(0, len(res)):
        c_time = datetime.datetime.now()
        if c_time.second > res[i][12] and c_time.minute == res[i][11] and c_time.hour == res[i][10] and c_time.year == \
                res[i][2] and c_time.month == res[i][3] and c_time.day == res[i][4]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.minute > res[i][11] and c_time.hour == res[i][10] and c_time.year == \
                res[i][2] and c_time.month == res[i][3] and c_time.day == res[i][4]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.hour > res[i][10] and c_time.year == \
                res[i][2] and c_time.month == res[i][3] and c_time.day == res[i][4]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.year == res[i][2] and c_time.month == res[i][3] and c_time.day > res[i][4]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.year == res[i][2] and c_time.month > res[i][3]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.year > res[i][2]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        else:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('进行中', res[i][0]))
            g.conn.commit()
    sql = 'SELECT * FROM TASK WHERE USER=? AND EVERYDAY=1'
    cur.execute(sql, (user,))
    res = cur.fetchall()
    for i in range(0, len(res)):
        c_time = datetime.datetime.now()
        if c_time.year == res[i][2] and c_time.month == res[i][3] and c_time.day > res[i][4]:
            sql = 'UPDATE TASK SET STATE=?,YEAR=?,MONTH=?,DAY=?,COMPLETE=? WHERE ID=?'
            cur.execute(sql, ('进行中', c_time.year, c_time.month, c_time.day, 0, res[i][0]))
            g.conn.commit()
        elif c_time.year == res[i][2] and c_time.month > res[i][3]:
            sql = 'UPDATE TASK SET STATE=?,YEAR=?,MONTH=?,DAY=?,COMPLETE=? WHERE ID=?'
            cur.execute(sql, ('进行中', c_time.year, c_time.month, c_time.day, 0, res[i][0]))
            g.conn.commit()
        elif c_time.year > res[i][2]:
            sql = 'UPDATE TASK SET STATE=?,YEAR=?,MONTH=?,DAY=?,COMPLETE=? WHERE ID=?'
            cur.execute(sql, ('进行中', c_time.year, c_time.month, c_time.day, 0, res[i][0]))
            g.conn.commit()
    sql = 'SELECT * FROM TASK WHERE USER=? AND COMPLETE=0 AND EVERYDAY=1'
    cur.execute(sql, (user,))
    res = cur.fetchall()
    for i in range(0, len(res)):
        c_time = datetime.datetime.now()
        if c_time.second > res[i][12] and c_time.minute == res[i][11] and c_time.hour == res[i][10]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.minute > res[i][11] and c_time.hour == res[i][10]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        elif c_time.hour > res[i][10]:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('已过期', res[i][0]))
            g.conn.commit()
        else:
            sql = 'UPDATE TASK SET STATE=? WHERE ID=?'
            cur.execute(sql, ('进行中', res[i][0]))
            g.conn.commit()


def today_page():
    cur = g.conn.cursor()
    c_time = datetime.datetime.now()
    year = c_time.year
    month = c_time.month
    day = c_time.day
    DECORATE = g.PanelDecorate.pageDecorate_today
    text = DECORATE.comboBox.currentText()
    if text == '所有':
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND COMPLETE=0 AND STATE!="已过期" ORDER BY HOUR, MINUTE, SECONDS'
        cur.execute(sql, (year, month, day, user))
        res_everyday_plan = cur.fetchall()
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND STATE="已过期" ORDER BY HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (year, month, day, user))
        res_everyday_outdate = cur.fetchall()
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND COMPLETE=1 ORDER BY HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (year, month, day, user))
        res_everyday_com = cur.fetchall()
    else:
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND COMPLETE=0 AND STATE!="已过期" AND CATEGORY=? ORDER BY HOUR, MINUTE, SECONDS'
        cur.execute(sql, (year, month, day, user, text))
        res_everyday_plan = cur.fetchall()
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND STATE="已过期" AND CATEGORY=? ORDER BY HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (year, month, day, user, text))
        res_everyday_outdate = cur.fetchall()
        sql = 'SELECT * FROM TASK WHERE ((YEAR=? AND MONTH=? AND DAY=?) OR EVERYDAY=1) AND USER=? AND COMPLETE=1 AND CATEGORY=? ORDER BY HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (year, month, day, user, text))
        res_everyday_com = cur.fetchall()
    DECORATE.tableWidget.setRowCount(len(res_everyday_plan) + len(res_everyday_outdate) + len(res_everyday_com))
    for i in range(0, len(res_everyday_plan)):
        c_time = QDateTime.currentDateTime()
        totalTime = -3600 * (c_time.time().hour() - res_everyday_plan[i][10]) - 60 * (
                c_time.time().minute() - res_everyday_plan[i][11]) - (
                            c_time.time().second() - res_everyday_plan[i][12])
        col_1 = QtWidgets.QTableWidgetItem(str(res_everyday_plan[i][0]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res_everyday_plan[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res_everyday_plan[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(0, 0, 255))
        if res_everyday_plan[i][5] == 0:
            col_4 = QtWidgets.QTableWidgetItem(
                str(res_everyday_plan[i][2]) + '-' + str(res_everyday_plan[i][3]) + '-' + str(
                    res_everyday_plan[i][4]) + '  ' + str(res_everyday_plan[i][10]) + ':' + str(
                    res_everyday_plan[i][11]) + ':' + str(res_everyday_plan[i][12]))
        else:
            col_4 = QtWidgets.QTableWidgetItem('每天  ' + str(res_everyday_plan[i][10]) + ':' + str(
                res_everyday_plan[i][11]) + ':' + str(res_everyday_plan[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res_everyday_plan[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res_everyday_plan[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        col_7 = QtWidgets.QTableWidgetItem(f'{totalTime // 3600}时{totalTime // 60 % 60}分{totalTime % 60}秒')
        col_7.setTextAlignment(QtCore.Qt.AlignCenter)
        col_7.setForeground(QtGui.QColor(50, 205, 50))
        checkBox = checkForRow(res_everyday_plan[i][0], res_everyday_plan[i][8])
        DECORATE.tableWidget.setItem(i, 1, col_1)
        DECORATE.tableWidget.setItem(i, 2, col_2)
        DECORATE.tableWidget.setItem(i, 3, col_3)
        DECORATE.tableWidget.setItem(i, 4, col_4)
        DECORATE.tableWidget.setItem(i, 5, col_5)
        DECORATE.tableWidget.setItem(i, 6, col_6)
        DECORATE.tableWidget.setItem(i, 7, col_7)
        DECORATE.tableWidget.setCellWidget(i, 0, checkBox)
        DECORATE.tableWidget.setRowHeight(i, 40)
    j = len(res_everyday_plan)
    for i in range(0, len(res_everyday_outdate)):
        c_time = QDateTime.currentDateTime()
        totalTime = 3600 * (c_time.time().hour() - res_everyday_outdate[i][10]) + 60 * (
                c_time.time().minute() - res_everyday_outdate[i][11]) + (
                            c_time.time().second() - res_everyday_outdate[i][12])
        col_1 = QtWidgets.QTableWidgetItem(str(res_everyday_outdate[i][0]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res_everyday_outdate[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res_everyday_outdate[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(255, 0, 0))
        if res_everyday_outdate[i][5] == 0:
            col_4 = QtWidgets.QTableWidgetItem(
                str(res_everyday_outdate[i][2]) + '-' + str(res_everyday_outdate[i][3]) + '-' + str(
                    res_everyday_outdate[i][4]) + '  ' + str(res_everyday_outdate[i][10]) + ':' + str(
                    res_everyday_outdate[i][11]) + ':' + str(res_everyday_outdate[i][12]))
        else:
            col_4 = QtWidgets.QTableWidgetItem('每天  ' + str(res_everyday_outdate[i][10]) + ':' + str(
                res_everyday_outdate[i][11]) + ':' + str(res_everyday_outdate[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res_everyday_outdate[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res_everyday_outdate[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        col_7 = QtWidgets.QTableWidgetItem(f'已超时 {totalTime // 3600}时{totalTime // 60 % 60}分{totalTime % 60}秒')
        col_7.setTextAlignment(QtCore.Qt.AlignCenter)
        col_7.setForeground(QtGui.QColor(255, 0, 0))
        checkBox = checkForRow(res_everyday_outdate[i][0], res_everyday_outdate[i][8])
        DECORATE.tableWidget.setItem(j, 1, col_1)
        DECORATE.tableWidget.setItem(j, 2, col_2)
        DECORATE.tableWidget.setItem(j, 3, col_3)
        DECORATE.tableWidget.setItem(j, 4, col_4)
        DECORATE.tableWidget.setItem(j, 5, col_5)
        DECORATE.tableWidget.setItem(j, 6, col_6)
        DECORATE.tableWidget.setItem(j, 7, col_7)
        DECORATE.tableWidget.setCellWidget(j, 0, checkBox)
        DECORATE.tableWidget.setRowHeight(j, 40)
        j += 1
    for i in range(0, len(res_everyday_com)):
        col_1 = QtWidgets.QTableWidgetItem(str(res_everyday_com[i][0]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res_everyday_com[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res_everyday_com[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(255, 0, 0))
        if res_everyday_com[i][5] == 0:
            col_4 = QtWidgets.QTableWidgetItem(
                str(res_everyday_com[i][2]) + '-' + str(res_everyday_com[i][3]) + '-' + str(
                    res_everyday_com[i][4]) + '  ' + str(res_everyday_com[i][10]) + ':' + str(
                    res_everyday_com[i][11]) + ':' + str(res_everyday_com[i][12]))
        else:
            col_4 = QtWidgets.QTableWidgetItem('每天  ' + str(res_everyday_com[i][10]) + ':' + str(
                res_everyday_com[i][11]) + ':' + str(res_everyday_com[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res_everyday_com[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res_everyday_com[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        col_7 = QtWidgets.QTableWidgetItem("")
        col_7.setTextAlignment(QtCore.Qt.AlignCenter)
        checkBox = checkForRow(res_everyday_com[i][0], res_everyday_com[i][8])
        checkBox.setChecked(True)
        col_1.setForeground(QtGui.QColor(140, 140, 140))
        col_2.setForeground(QtGui.QColor(140, 140, 140))
        col_3.setForeground(QtGui.QColor(140, 140, 140))
        col_4.setForeground(QtGui.QColor(140, 140, 140))
        col_5.setForeground(QtGui.QColor(140, 140, 140))
        col_6.setForeground(QtGui.QColor(140, 140, 140))
        DECORATE.tableWidget.setItem(j, 1, col_1)
        DECORATE.tableWidget.setItem(j, 2, col_2)
        DECORATE.tableWidget.setItem(j, 3, col_3)
        DECORATE.tableWidget.setItem(j, 4, col_4)
        DECORATE.tableWidget.setItem(j, 5, col_5)
        DECORATE.tableWidget.setItem(j, 6, col_6)
        DECORATE.tableWidget.setItem(j, 7, col_7)
        DECORATE.tableWidget.setCellWidget(j, 0, checkBox)
        DECORATE.tableWidget.setRowHeight(j, 40)
        j += 1


def add_item(date, text):
    day = date.day()
    month = date.month()
    year = date.year()
    cur = g.conn.cursor()
    if text == '所有':
        sql = 'SELECT * FROM TASK WHERE YEAR=? AND MONTH=? AND DAY=? AND USER=? AND EVERYDAY=0 ORDER BY COMPLETE ASC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (year, month, day, user))
    else:
        sql = 'SELECT * FROM TASK WHERE YEAR=? AND MONTH=? AND DAY=? AND USER=? AND COMPLETE=? AND EVERYDAY=0 ORDER BY COMPLETE ASC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        if text == '未完成':
            com = 0
        else:
            com = 1
        cur.execute(sql, (year, month, day, user, com))
    res = cur.fetchall()
    DECORATE = g.PanelDecorate.pageDecorate_ca
    DECORATE.tableWidget.setRowCount(len(res))
    for i in range(0, len(res)):
        col_1 = QtWidgets.QTableWidgetItem(str(res[i][0]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(0, 0, 255))
        col_4 = QtWidgets.QTableWidgetItem(
            str(res[i][2]) + '-' + str(res[i][3]) + '-' + str(res[i][4]) + '  ' + str(res[i][10]) + ':' + str(
                res[i][11]) + ':' + str(res[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        checkBox = checkForRow(res[i][0], res[i][8])
        btn = buttonForRow(res[i][0])
        if res[i][8] == 1:
            checkBox.setChecked(True)
            col_1.setForeground(QtGui.QColor(140, 140, 140))
            col_2.setForeground(QtGui.QColor(140, 140, 140))
            col_3.setForeground(QtGui.QColor(140, 140, 140))
            col_4.setForeground(QtGui.QColor(140, 140, 140))
            col_5.setForeground(QtGui.QColor(140, 140, 140))
            col_6.setForeground(QtGui.QColor(140, 140, 140))
        elif res[i][9] == '已过期':
            col_3.setForeground(QtGui.QColor(255, 0, 0))
        DECORATE.tableWidget.setItem(i, 1, col_1)
        DECORATE.tableWidget.setItem(i, 2, col_2)
        DECORATE.tableWidget.setItem(i, 3, col_3)
        DECORATE.tableWidget.setItem(i, 4, col_4)
        DECORATE.tableWidget.setItem(i, 5, col_5)
        DECORATE.tableWidget.setItem(i, 6, col_6)
        DECORATE.tableWidget.setCellWidget(i, 0, checkBox)
        DECORATE.tableWidget.setCellWidget(i, 7, btn)
        DECORATE.tableWidget.setRowHeight(i, 40)


def add_item_onplan(text):
    cur = g.conn.cursor()
    if text == '按时间':
        sql = 'SELECT * FROM TASK WHERE COMPLETE=0 AND STATE!="已过期" AND USER=? ORDER BY YEAR,MONTH,DAY,HOUR,MINUTE,SECONDS'
        cur.execute(sql, (user,))
    else:
        sql = 'SELECT * FROM TASK WHERE COMPLETE=0 AND STATE!="已过期" AND USER=? ORDER BY IMPORTANCE DESC '
        cur.execute(sql, (user,))
    res = cur.fetchall()
    DECORATE = g.PanelDecorate.pageDecorate_plan
    DECORATE.tableWidget.setRowCount(len(res))
    for i in range(0, len(res)):
        col_1 = QtWidgets.QTableWidgetItem(str(res[i][7]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(0, 0, 255))
        if res[i][5] == 0:
            col_4 = QtWidgets.QTableWidgetItem(
                str(res[i][2]) + '-' + str(res[i][3]) + '-' + str(
                    res[i][4]) + '  ' + str(res[i][10]) + ':' + str(
                    res[i][11]) + ':' + str(res[i][12]))
        else:
            col_4 = QtWidgets.QTableWidgetItem('每天  ' + str(res[i][10]) + ':' + str(
                res[i][11]) + ':' + str(res[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        checkBox = checkForRow(res[i][0], res[i][8])
        btn = buttonForRow(res[i][0])
        DECORATE.tableWidget.setItem(i, 1, col_1)
        DECORATE.tableWidget.setItem(i, 2, col_2)
        DECORATE.tableWidget.setItem(i, 3, col_3)
        DECORATE.tableWidget.setItem(i, 4, col_4)
        DECORATE.tableWidget.setItem(i, 5, col_5)
        DECORATE.tableWidget.setItem(i, 6, col_6)
        DECORATE.tableWidget.setCellWidget(i, 0, checkBox)
        DECORATE.tableWidget.setRowHeight(i, 40)
        DECORATE.tableWidget.setCellWidget(i, 7, btn)


def all_page():
    text1 = g.PanelDecorate.pageDecorate_all.comboBox_txet.currentText()
    text2 = g.PanelDecorate.pageDecorate_all.comboBox.currentText()
    cur = g.conn.cursor()
    if text1 == '所有' and text2 == '所有':
        sql = 'SELECT * FROM TASK WHERE USER=? ORDER BY COMPLETE ASC, YEAR DESC, MONTH DESC, DAY DESC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (user,))
    elif text1 == '所有' and text2 != '所有':
        sql = 'SELECT * FROM TASK WHERE USER=? AND CATEGORY=? ORDER BY COMPLETE ASC, YEAR DESC, MONTH DESC, DAY DESC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (user, text2))
    elif text1 != '所有' and text2 == '所有':
        sql = 'SELECT * FROM TASK WHERE USER=? AND STATE=? ORDER BY COMPLETE ASC, YEAR DESC, MONTH DESC, DAY DESC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (user, text1))
    else:
        sql = 'SELECT * FROM TASK WHERE USER=? AND CATEGORY=? AND STATE=? ORDER BY COMPLETE ASC, YEAR DESC, MONTH DESC, DAY DESC, HOUR DESC, MINUTE DESC, SECONDS DESC'
        cur.execute(sql, (user, text2, text1))
    res = cur.fetchall()
    DECORATE = g.PanelDecorate.pageDecorate_all
    DECORATE.tableWidget.setRowCount(len(res))
    for i in range(0, len(res)):
        col_1 = QtWidgets.QTableWidgetItem(str(res[i][0]))
        col_1.setTextAlignment(QtCore.Qt.AlignCenter)
        col_2 = QtWidgets.QTableWidgetItem(res[i][6])
        col_2.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3 = QtWidgets.QTableWidgetItem(res[i][9])
        col_3.setTextAlignment(QtCore.Qt.AlignCenter)
        col_3.setForeground(QtGui.QColor(0, 0, 255))
        if res[i][5] == 0:
            col_4 = QtWidgets.QTableWidgetItem(
                str(res[i][2]) + '-' + str(res[i][3]) + '-' + str(
                    res[i][4]) + '  ' + str(res[i][10]) + ':' + str(
                    res[i][11]) + ':' + str(res[i][12]))
        else:
            col_4 = QtWidgets.QTableWidgetItem('每天  ' + str(res[i][10]) + ':' + str(
                res[i][11]) + ':' + str(res[i][12]))
        col_4.setTextAlignment(QtCore.Qt.AlignCenter)
        col_5 = QtWidgets.QTableWidgetItem(res[i][13])
        col_5.setTextAlignment(QtCore.Qt.AlignCenter)
        col_6 = QtWidgets.QTableWidgetItem(res[i][1])
        col_6.setTextAlignment(QtCore.Qt.AlignCenter)
        checkBox = checkForRow(res[i][0], res[i][8])
        btn = buttonForRow(res[i][0])
        if res[i][8] == 1:
            checkBox.setChecked(True)
            col_1.setForeground(QtGui.QColor(140, 140, 140))
            col_2.setForeground(QtGui.QColor(140, 140, 140))
            col_3.setForeground(QtGui.QColor(140, 140, 140))
            col_4.setForeground(QtGui.QColor(140, 140, 140))
            col_5.setForeground(QtGui.QColor(140, 140, 140))
            col_6.setForeground(QtGui.QColor(140, 140, 140))
        elif res[i][9] == '已过期':
            col_3.setForeground(QtGui.QColor(255, 0, 0))
        DECORATE.tableWidget.setItem(i, 1, col_1)
        DECORATE.tableWidget.setItem(i, 2, col_2)
        DECORATE.tableWidget.setItem(i, 3, col_3)
        DECORATE.tableWidget.setItem(i, 4, col_4)
        DECORATE.tableWidget.setItem(i, 5, col_5)
        DECORATE.tableWidget.setItem(i, 6, col_6)
        DECORATE.tableWidget.setCellWidget(i, 0, checkBox)
        DECORATE.tableWidget.setCellWidget(i, 7, btn)
        DECORATE.tableWidget.setRowHeight(i, 40)


def checkForRow(id, bool):
    checkBox = QtWidgets.QCheckBox()
    checkBox.setText("")
    checkBox.setStyleSheet('QCheckBox{margin-left:10}')
    checkBox.clicked.connect(
        lambda: task_state_change(id, bool)
    )
    return checkBox


def task_state_change(id, bool):
    cur = g.conn.cursor()
    if bool == 0:
        sql = 'UPDATE TASK SET COMPLETE=1,STATE=? WHERE ID=?'
        cur.execute(sql, ('已完成', id))
    else:
        sql = 'UPDATE TASK SET COMPLETE=0,STATE=? WHERE ID=?'
        cur.execute(sql, ('进行中', id))
    g.conn.commit()
    shuaxin()


def buttonForRow(id):
    widget = QtWidgets.QWidget()
    pushButton_update = QtWidgets.QPushButton()
    pushButton_update.setText("修改")
    # pushButton_update.setStyleSheet(''' text-align : center;
    #                                         background-color : NavajoWhite;
    #                                         height : 30px;
    #                                         border-style: outset;
    #                                        font : 17px  ''')
    pushButton_update.setStyleSheet('''QPushButton{font-family:'黑体';text-align : center;
                                            background-color : NavajoWhite;
                                            color:rgb(139,69,19);
                                            height : 30px;
                                            border-style: outset;
                                           font : 17px}''')
    pushButton_update.clicked.connect(
        lambda: up_date(id)
    )

    pushButton_delete = QtWidgets.QPushButton()
    pushButton_delete.setText("删除")
    # pushButton_delete.setStyleSheet(''' text-align : center;
    #                                  background-color : LightCoral;
    #                                  height : 30px;
    #                                  border-style: outset;
    #                                  font : 17px; ''')
    pushButton_delete.setStyleSheet('''QPushButton{font-family:'黑体';text-align : center;
                                            background-color : LightCoral;
                                            color:rgb(250,250,210);
                                            height : 30px;
                                            border-style: outset;
                                            font : 17px}''')
    pushButton_delete.clicked.connect(
        lambda: task_delete(id)
    )

    hLayout = QtWidgets.QHBoxLayout()
    hLayout.addWidget(pushButton_update)
    hLayout.addWidget(pushButton_delete)
    hLayout.setContentsMargins(5, 2, 5, 2)
    widget.setLayout(hLayout)
    return widget


def add_task(contend, year, month, day, everyday, title, importance, hour, minute, seconds, category):
    cur = g.conn.cursor()
    sql = 'INSERT INTO TASK(contend,year,month,day,everyday,title,importance,hour,minute,seconds,category,user) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'
    cur.execute(sql, (contend, year, month, day, everyday, title, importance, hour, minute, seconds, category, user))
    g.conn.commit()
    shuaxin()


def task_delete(id):
    cur = g.conn.cursor()
    sql = 'DELETE FROM TASK WHERE ID=?'
    cur.execute(sql, (id,))
    g.conn.commit()
    shuaxin()


def up_date(id):
    cur = g.conn.cursor()
    sql = 'SELECT * FROM TASK WHERE ID=?'
    cur.execute(sql, (id,))
    res = cur.fetchall()
    date = QDate(res[0][2], res[0][3], res[0][4])
    time = QTime(res[0][10], res[0][11], res[0][12])
    b = AlterTaskFrame()
    b.setText(res[0][6], res[0][1], date, time, res[0][7], res[0][5], res[0][13])
    b.set_id(id)
    b.frame.show()


def update_coon(contend, year, month, day, everyday, title, importance, hour, minute, seconds, category, id):
    cur = g.conn.cursor()
    sql = 'UPDATE TASK SET contend=?,year=?,month=?,day=?,everyday=?,title=?,importance=?,hour=?,minute=?,seconds=?,category=?,user=? WHERE ID=?'
    cur.execute(sql,
                (contend, year, month, day, everyday, title, importance, hour, minute, seconds, category, user, id))
    g.conn.commit()
    shuaxin()


def userinfo_show():
    user_info_file = open("./data_base/user_info.json", "r", encoding="GBK")
    user_info = json.load(user_info_file)
    user_info_file.close()
    for info in user_info:
        if info['account'] == user:
            personInfo = info
            break
        else:
            personInfo = {}
    user_info_file = open("./data_base/user_info.json", "w")
    json.dump(user_info, user_info_file, indent=2, ensure_ascii=False)
    user_info_file.close()
    g.infoDecorate.lineEdit.setText(personInfo['account'])
    g.infoDecorate.lineEdit_2.setText(personInfo['name'])
    g.infoDecorate.lineEdit_3.setText(personInfo['stu_num'])
    g.infoDecorate.lineEdit_4.setText(personInfo['per_num'])
    g.info_page.show()
    # g.infoDecorate.set_con(personInfo)
    # PersonalInfoFrame(user)
    # BuildTask().frame.show()


