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
        self.notes.setTabStopWidth(30)
        # self.notes.setTabChangesFocus(True)
        self.notes.installEventFilter(self)
        self.colors = self.colors()
        # self.notes.setTextColor(self.colors[11])
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
        self.setStyleSheet("background-color : rgba(0,0,0,10%)")
        self.show()

    def builder(self):
        font = QtGui.QFont()
        font.setPointSize(12)

        # font.setFamily("Courier")
        # font.setStyleHint()
        # font.setFixedPitch()
        # font.setPointSize(10)

        self.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout()
        self.notes.setStyleSheet("background-color : rgba(0,0,0,10%); color : white;")
        self.gridLayout.addWidget(self.notes, 0, 0, 1, 1)
        self.setLayout(self.gridLayout)


    def getNotes(self):
        return self.notes.toPlainText()

    def updateScreen(self, text):
        count =0
        for i in text:
            if count == 11:
                count = 0
            self.notes.setTextColor(self.colors[count])
            # if "-" not in i:
            #     string = "- "
            #     string += i


            # self.notes.textCursor().insertText(string)
            # else:
            self.notes.textCursor().insertText(i)
            count = count +1

    def keyPressEvent(self, e):

        if e.key() == Qt.Key_Escape:
            self.close()

    def eventFilter(self, obj, event):
        # end = self.notes.cursor().selectionEnd()

        if event.type() == QtCore.QEvent.KeyPress and obj is self.notes:
            if event.key() == QtCore.Qt.Key_Tab:
                # pass
                self.tabPressed()
                return True

        return super().eventFilter(obj, event)

    def addPointer(self):

        self.notes.textCursor().insertText('-')

    def cursorPosition(self):

        # cursor = self.notes.textCursor()
        #
        # # Mortals like 1-indexed things
        # line = cursor.blockNumber() + 1
        # col = cursor.columnNumber()
        # # Set the cursor to select the text
        # cursor = editor.textCursor()
        #
        # cursor.setPosition(loc)
        # cursor.movePosition(cursor.Right, cursor.KeepAnchor, line_len)
        # # self.notes.textCursor().
        # print("Line: {} | Column: {}".format(line, col))
        pass

    def colors(self):
        colors = []
        red = QColor(255, 0, 0)
        Orange = QColor(255, 153, 51)
        Yellow = QColor(255, 255, 51)
        lime = QColor(153, 255, 51)
        Green = QColor(51, 255, 51)
        gb = QColor(51, 255, 153)
        cyan = QColor(51, 255, 255)
        Blue = QColor(51, 153,255)
        Bluedark = QColor(51, 51 ,255)
        purple = QColor(153, 51, 255)
        Violet = QColor(255, 102, 155)
        # white = QColor(255, 255, 255)

        colors.append(red)
        colors.append(Orange)
        colors.append(Yellow)
        colors.append(lime)
        colors.append(Green)
        colors.append(gb)
        colors.append(cyan)
        colors.append(Blue)
        colors.append(Bluedark)
        colors.append(purple)
        colors.append(Violet)
        # colors.append(white)

        return colors

    def tabPressed(self):

        textLine = self.getLineText()
        self.cleanLine()

        if "-" not in textLine:
            tab = "\t-"
            tab += textLine
        else:
            tab = "\t"
            tab += textLine

        # print(tab)
        self.notes.textCursor().insertText(tab)

    def cleanLine(self):
        cursor = self.notes.textCursor()
        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        cursor.setPosition(start)
        cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
        cursor.select(QTextCursor.LineUnderCursor)
        cursor.removeSelectedText()
        self.notes.setTextCursor(cursor)

    def getLine(self):

        cursor = self.notes.textCursor()
        line = cursor.blockNumber() + 1
        return  line

    def getPrevLine(self):

        cursor = self.notes.textCursor()
        line = cursor.blockNumber()
        return line

    def getLineText(self):

        text = self.notes.toPlainText().split('\n')
        line = self.getLine()
        # print(text[line-1], "---------")
        return text[line-1]
