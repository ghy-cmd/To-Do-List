import sys

from PyQt5.QtCore import *

from gene import g
from control import func


# def init_mainwindow():
#     window = g.mainWindow
#     g.mainWindowDecorate.setupUi(window)  # 启动程序

# g.mainWindowDecorate.pushButton.clicked.connect(
#     lambda: func.changepage()
# )


# def init_calendar():
#     decorate = g.CalendarDecorate
#     decorate.setupUi(g.CalendarPage)
#     # decorate1 = g.PanelDecorate
#     # decorate1.setupUi(g.PanelPage)
#     # decorate1.stackedWidget.addWidget(g.PanelPage)
#     func.add_item(decorate.calendarWidget.selectedDate())
#     decorate.calendarWidget.setMinimumDate(QDate(2021, 1, 1))
#     decorate.calendarWidget.setMaximumDate(QDate(2089, 1, 1))
#     decorate.calendarWidget.setGridVisible(True)
#     decorate.calendarWidget.clicked.connect(
#         lambda: func.add_item(decorate.calendarWidget.selectedDate())
#     )


def init_panel():
    decorate = g.PanelDecorate
    decorate.setupUi(g.PanelPage)
    func.shuaxin()
    decorate.pageDecorate_ca.calendarWidget.setMinimumDate(QDate(2021, 1, 1))
    decorate.pageDecorate_ca.calendarWidget.setMaximumDate(QDate(2089, 1, 1))
    decorate.pageDecorate_ca.calendarWidget.setGridVisible(True)
    decorate.pageDecorate_ca.calendarWidget.clicked.connect(
        lambda: func.add_item(decorate.pageDecorate_ca.calendarWidget.selectedDate(),
                              decorate.pageDecorate_ca.comboBox.currentText())
    )
    decorate.pageDecorate_ca.comboBox.currentIndexChanged.connect(
        lambda: func.add_item(decorate.pageDecorate_ca.calendarWidget.selectedDate(),
                              decorate.pageDecorate_ca.comboBox.currentText())
    )
    decorate.pageDecorate_plan.comboBox.currentIndexChanged.connect(
        lambda: func.add_item_onplan(decorate.pageDecorate_plan.comboBox.currentText())
    )
    decorate.pageDecorate_today.comboBox.currentIndexChanged.connect(
        lambda: func.today_page()
    )
    decorate.pageDecorate_all.comboBox.currentIndexChanged.connect(
        lambda: func.all_page()
    )
    decorate.pageDecorate_all.comboBox_txet.currentIndexChanged.connect(
        lambda: func.all_page()
    )
    decorate.pushButton.clicked.connect(
        lambda: decorate.change(0)
    )
    decorate.pushButton_2.clicked.connect(
        lambda: decorate.change(1)
    )
    decorate.pushButton_3.clicked.connect(
        lambda: decorate.change(2)
    )
    decorate.pushButton_4.clicked.connect(
        lambda: decorate.change(3)
    )
    # decorate.pushButton_5.clicked.connect(
    #     lambda: decorate.change(4)
    # )
    decorate.pushButton_add.clicked.connect(
        lambda: func.add_task_panel()
    )
    decorate.pushButton_user.clicked.connect(
        lambda: func.userinfo_show()
    )
    decorate.pushButton_min.clicked.connect(
        lambda: g.PanelPage.showMinimized()
    )
    # decorate.pushButton_max.clicked.connect(
    #     lambda: g.PanelPage.showMaximized()
    # )
    decorate.pushButton_close.clicked.connect(
        lambda: close()
    )
    decorate.pageDecorate_today.timer.timeout.connect(
        lambda: func.today_page()
    )


def init_info():
    decorate = g.infoDecorate
    decorate.setupUi(g.info_page)
    g.info_page.addButtons()
    g.info_page.setWindowTitle("USER_INFO")
    # func.userinfo_show()


def init_all():
    # init_mainwindow()
    # init_calendar()
    init_panel()
    init_info()


def close():
    sys.exit(g.app.exec_())
