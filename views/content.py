from PyQt5.QtWidgets import QWidget


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.notes = QTextEdit()
        self.buildWindow()
        self.builder()
        self.__readNotes()
        self.__addEventHandlers()
