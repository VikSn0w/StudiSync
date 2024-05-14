import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
#from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data
from gui.segreteria_home_gui import Ui_Segreteria_Home


class SegreteriaHomeLogic(QMainWindow):
    user = None
    def __init__(self,user):
        self.user = user
        super().__init__()
        self.ui = Ui_Segreteria_Home()
        self.ui.setupUi(self)

    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.MtrLabel.setText(user[0])
        self.ui.NameLastnameLabel.setText(f"{user[1]}, {user[2]}")
        self.ui.DateLabel.setText(f"{formato_data()}")
def run(user):
    window = SegreteriaHomeLogic(user)
    window.show()

if __name__ == "__main__":
    run('["0124002584", "Vittorio", "Picone", "vittorio.picone001@studenti.uniparthenope.it", "1914752590"]')