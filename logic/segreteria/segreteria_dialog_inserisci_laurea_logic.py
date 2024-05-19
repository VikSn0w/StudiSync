import json

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox, QDialog
# from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import request_constructor_str
from gui.segreteria.segreteria_dialog_inserisci_laurea_gui import Ui_segreteria_dialog_inserisci_laurea


class SegreteriaDialogInserisciLaureaLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_segreteria_dialog_inserisci_laurea()
        self.ui.setupUi(self)
        reg_ex = QRegExp("[0-9]+")
        input_validator = QRegExpValidator(reg_ex, self.ui.MtrLaurea)
        self.ui.MtrLaurea.setValidator(input_validator)
        self.ui.InsertLaureaButton.clicked.connect(self.insertLaureaIntoServer)

    def insertLaureaIntoServer(self):
        toSend = {"MtrLaurea": str(self.ui.MtrLaurea.text()), "NomeLaurea": str(self.ui.NomeLaurea.text())}
        result = launchMethod(request_constructor_str(toSend, "InsertLaurea"), "127.0.0.1", 5000)

        result = json.loads(result)

        if result["result"] != "True":
            QMessageBox.critical(None, "Insert - Error",
                                 f"La laurea inserita è già presente nel database\n{result['result'][0]} - {result['result'][1]}")
        else:
            QMessageBox.information(None, "Insert - Success",
                                 f"La laurea inserita correttamente")

def run():
    dialog = SegreteriaDialogInserisciLaureaLogic()
    dialog.exec_()


if __name__ == "__main__":
    run()
