import json
import sys
import os

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QVBoxLayout, QPushButton, QLabel
# from pyqt5_plugins.examplebutton import QtWidgets
from common.communication import find_rows

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data
from gui.segreteria_dialog_inoltra_prenotazione import Ui_InoltraPrenotazione


class SegreteriaDialogInoltraPrenotazioneLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_InoltraPrenotazione()
        self.ui.setupUi(self)







if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = SegreteriaDialogInoltraPrenotazioneLogic()
    window.show()
    sys.exit(app.exec_())