import sys

from PyQt5.QtCore import QTime, QDate
from PyQt5.QtWidgets import QApplication

from view.buildTaskFrame import BuildTask
from control import func

categories = ["默认", "运动", "旅游", "美食", "睡觉", "音乐", "游戏", "学习", "工作"]


class AlterTaskFrame(BuildTask):
    def __init__(self):
        super(AlterTaskFrame, self).__init__()
        self.pushButton_finish.clicked.disconnect(self.finish)
        self.pushButton_finish.clicked.connect(self.update)
        # self.search()
        # self.connect()
        # self.frame.show()

    # def search(self, id):
    #     # TODO:搜索数据库，获取数据，随后调用setText函数
    #
    #     # self.setText("123", "123", "2022-8-20   18:12:11", 10, 1, "Default")
    #     pass

    def setText(self, title, description, date, time, importance, routine, category):
        self.titleEdit.setText(title)
        self.desEdit.setText(description)
        # TODO:需要解析deadline字符串

        # self.dateTimeEdit.setDate(QDate(年， 月， 日))
        # self.dateTimeEdit.setTime(QTime(小时， 分钟， 秒钟))
        self.dateTimeEdit.setDate(date)
        self.dateTimeEdit.setTime(time)
        self.horizontalSlider.setValue(importance)
        self.combox.setCurrentIndex(1 if routine else 0)
        index = categories.index(category)
        if index == 0:
            path = "./pic/默认.png"
        else:
            path = "./pic/" + str(index) + ".png"
        self.changeTitleImage(path, category)

    def set_id(self, iii):
        self.iii = iii

    def update(self):
        # TODO: 重写完成按钮的connect，关闭页面，修改数据库
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
        func.update_coon(description, year, month, day, index, title, importance, hour, minute, seconds,
                         category, self.iii)
        self.frame.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = AlterTaskFrame()
    sys.exit(app.exec())
