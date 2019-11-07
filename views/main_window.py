from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore


from common import constants
from model import window_model

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.model = window_model.windowModel()
        self.notes = QTextEdit()
        self.buildWindow()
        self.builder()

    def buildWindow(self):

        # Setup
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.setWidth(constants.WIDTH)
        qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)
        self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.show()

    def builder(self):
        font = QtGui.QFont()
        font.setPointSize(32)
        self.setFont(font)
        # self.notes = QTextEdit()
        self.gridLayout = QtWidgets.QGridLayout()
        self.notes.setStyleSheet("background-color : rgba(0,0,0,25%); color : white;")
        self.gridLayout.addWidget(self.notes, 0, 0, 1, 1)
        self.setLayout(self.gridLayout)


    def getNotes(self):
        return self.notes.toPlainText()

    def updateScreen(self, text):
        for i in text:
            string = "- "
            string += i
            self.notes.textCursor().insertText(string)

