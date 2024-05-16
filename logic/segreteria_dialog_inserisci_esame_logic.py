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
from gui.segreteria_dialog_inserisci_esame_gui import Ui_segreteria_dialog_inserisci_esame


class SegreteriaDialogInserisciEsameLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_segreteria_dialog_inserisci_esame()
        self.ui.setupUi(self)
        result = launchMethod(request_constructor_str({}, "GetLauree"), "127.0.0.1", 5000)
        result = json.loads(result)
        for item in result["result"]:
            self.ui.comboBoxLaurea.addItem(f"{item[0]} - {item[1]}")
            self.ui.comboBoxLaurea.setItemData(self.ui.comboBoxLaurea.count() - 1, item[0])
        self.ui.InsertEsameButton.clicked.connect(self.insertEsameIntoServer)

    def insertEsameIntoServer(self):
        selected_index = self.ui.comboBoxLaurea.currentIndex()
        item_data = self.ui.comboBoxLaurea.itemData(selected_index)
        toSend = {"CFU": str(self.ui.CFUSpinBox.text()), "NomeCorso": str(self.ui.NomeEsameField.text()), "IdCorso": str(self.ui.IDEsame.text()).upper(), "NomeProfessore": str(self.ui.NomeProfessoreField.text()), "Laurea":str(item_data)}
        result = launchMethod(request_constructor_str(toSend, "InsertCorso"), "127.0.0.1", 5000)
        result = json.loads(result)

        if result["result"] != "True":
            QMessageBox.critical(None, "Insert - Error",
                                 f"L'esame inserito è già presente nel database\n{result['result'][0]} - {result['result'][1]} - {result['result'][2]} - {result['result'][3]} - {result['result'][4]}")
        else:
            QMessageBox.information(None, "Insert - Success",
                                 f"Esame Inserito correttamente")

def run():
    dialog = SegreteriaDialogInserisciEsameLogic()
    dialog.exec_()


if __name__ == "__main__":
    run()
