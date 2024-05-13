import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
#from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str
from gui.students_home_gui import Ui_Students_Home


class StudentsHomeLogic(QMainWindow):
    user = None
    def __init__(self,user):
        self.user = user
        super().__init__()
        self.ui = Ui_Students_Home()
        self.ui.setupUi(self)

    def openMainWindow(self):
        print("open")
        '''self.main_window = MetaphaseWindow()
        self.close()
        self.main_window.show()
        self.main_window.ui.nameLabel.setText(self.ui.usernameTextField.text())'''

def run(user):
    window = StudentsHomeLogic(user)
    window.show()

if __name__ == "__main__":
    run('["0124002584", "Vittorio", "Picone", "vittorio.picone001@studenti.uniparthenope.it", "1914752590"]')