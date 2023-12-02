from PyQt5 import QtGui

font = QtGui.QFont()
font.setFamily("华文楷体")


def setFont(size):
    font.setPointSize(size)
    return font
