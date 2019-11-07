import sys
from PyQt5.QtWidgets import QApplication

from controller.note_controller import noteController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = noteController()
    sys.exit(app.exec_())
