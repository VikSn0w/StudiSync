import json
import re
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog
# from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data,request_constructor_obj
from gui.students_home_gui import Ui_Students_Home
from gui.students_dialog_invio_richiesta_date_esami_gui import Ui_Invio_Richiesta_Date_Esami


class StudentsHomeLogic(QMainWindow):
    user = None

    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_Students_Home()
        self.ui.setupUi(self)
        self.ui.InvioRichiestaButton.clicked.connect(self.openDialogInvioRichiestaDateEsami)



    def inviaRichiesta(self):

        selected = self.ui_dialog.comboBox.currentText()
        pattern = r'\[(.*?)\]'
        selected = re.search(pattern, selected)
        selected = selected.group(1)
        payload = {"EsameRichiesto": selected, "MatricolaRichiedente": self.user[0]}
        print(f"Payload: {payload}")
        result = launchMethod(request_constructor_str(payload,"PutDataRequest"), "127.0.0.1", 5000)
        result = json.loads(result)
        if result['result'] == "OK":
            QMessageBox.information(None, "Accept - Success", "Richiesta Inviata con successo")


    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.MtrLabel.setText(user[0])
        self.ui.NameLastnameLabel.setText(f"{user[1]}, {user[2]}")
        self.ui.DateLabel.setText(f"{formato_data()}")

    def openDialogInvioRichiestaDateEsami(self):
        self.dialog = QDialog()
        self.ui_dialog = Ui_Invio_Richiesta_Date_Esami()

        self.ui_dialog.setupUi(self.dialog)
        self.ui_dialog.CorsoLaureaLabel.setText(f"{self.user[6][0]} - {self.user[6][1]}")
        corsi = json.loads(launchMethod(request_constructor_str(None, "GetCorsi"), "127.0.0.1", 5000))
        corsi = corsi['result']
        for c in corsi:
            if str(c[4]) == str(self.user[6][0]):
                newstr = f"[{c[0]}] {c[2]} - {c[1]} CFU"
                self.ui_dialog.comboBox.addItem(newstr)

        self.ui_dialog.InviaRichiestaButton.clicked.connect(self.inviaRichiesta)

        self.dialog.exec_()





def run(user):
    window = StudentsHomeLogic(user)
    window.show()


if __name__ == "__main__":
    run('["0124002584", "Vittorio", "Picone", "vittorio.picone001@studenti.uniparthenope.it", "1914752590"]')
