import sys
from PyQt5.QtWidgets import *
from gene import g
from control import show
from init import init
from control import func
from view.logInFrame import LogInFrame
from view.personalInfo import PersonalInfoFrame

if __name__ == "__main__":
    # init.init_all()
    show.show_mainwindow()
    # func.shuaxin()
    init.init_all()
    sys.exit(g.app.exec_())
