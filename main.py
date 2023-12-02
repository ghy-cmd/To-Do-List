import sys

from PyQt5.QtWidgets import QApplication

from view.personalInfo import PersonalInfoFrame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    b = PersonalInfoFrame("ghyh")
    b.frame.show()
    sys.exit(app.exec())
