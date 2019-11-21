import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

from model import window_model
from views.main_window import MainWindow


class noteController:

    def __init__(self):
        super().__init__()
        self.model = window_model.windowModel()
        self.view = MainWindow()
        self.view.updateScreen(self.model.readDB())
        self.__addEventHandlers()



    def __addEventHandlers(self):
        self.view.notes.textChanged.connect(lambda: self.__getNotes())
        # self.view.notes.textChanged.connect(lambda: self.view.addPointer())

        # self.view.notes.keyPressEvent(self)

    def __getNotes(self):
        notes=self.view.getNotes()
        self.model.uploadToDB(notes)

