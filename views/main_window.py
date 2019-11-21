from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pymongo import cursor

from common import constants
from model import window_model

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.model = window_model.windowModel()
        self.notes = QTextEdit()
        self.notes.installEventFilter(self)

        self.buildWindow()
        self.builder()

    def buildWindow(self):

        # Setup
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().topRight()
        qtRectangle.setWidth(constants.WIDTH)
        qtRectangle.setHeight(constants.HEIGHT)
        qtRectangle.moveCenter(centerPoint)
        self.setWindowTitle(constants.SYSTEM_TITLE)
        self.setGeometry(qtRectangle)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("background-color : rgba(0,0,0,25%); color : white;")
        self.show()

    def builder(self):
        font = QtGui.QFont()
        font.setPointSize(12)
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
            if "-" not in i:
                string = "- "
                string += i
                self.notes.textCursor().insertText(string)
            else:
                self.notes.textCursor().insertText(i)

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.notes:
            if event.key() == QtCore.Qt.Key_Return:
                self.notes.textCursor().insertText('-')

        return super().eventFilter(obj, event)

