import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
# from pyqt5_plugins.examplebutton import QtWidgets
from common.communication import find_rows

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data
from gui.segreteria_dialog_inserisci_laurea_gui import Ui_segreteria_dialog_inserisci_laurea


class SegreteriaHomeLogic(QMainWindow):
    user = None
    lauree = find_rows("db\\esami\\laurea.csv", None)
    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_segreteria_dialog_inserisci_laurea()
        self.ui.setupUi(self)
        self.ui.InsertLaureaButton.clicked.connect(self.insertLaureaIntoServer)
    def insertLaureaIntoServer(self):
        return False
def run(user):
    window = SegreteriaHomeLogic(user)
    window.show()


if __name__ == "__main__":
    run('["0124002584", "Vittorio", "Picone", "vittorio.picone001@studenti.uniparthenope.it", "1914752590"]')
