import json
import sys
import os

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
# from pyqt5_plugins.examplebutton import QtWidgets
from common.communication import find_rows

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data
from gui.segreteria_dialog_fornisci_date import Ui_fornisciDate


class SegreteriaDialogFornisciDateLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_fornisciDate()
        self.ui.setupUi(self)



