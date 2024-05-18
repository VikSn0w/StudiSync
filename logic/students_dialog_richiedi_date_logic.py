import json
import sys
import os
import re


from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QHBoxLayout, QLabel, QVBoxLayout, \
    QPushButton
# from pyqt5_plugins.examplebutton import QtWidgets
from common.communication import find_rows

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str, formato_data
from gui.students_dialog_invio_richiesta_date_esami_gui import Ui_Invio_Richiesta_Date_Esami


class StudentsDialogRichiestaDateLogic(QDialog):

    def __init__(self,user):
        super().__init__()
        self.user = user
        self.ui = Ui_Invio_Richiesta_Date_Esami()
        self.ui.setupUi(self)
        self.ui.CorsoLaureaLabel.setText(f"{self.user[6][0]} - {self.user[6][1]}")
        corsi = json.loads(launchMethod(request_constructor_str(None, "GetCorsi"), "127.0.0.1", 5000))
        corsi = corsi['result']
        for c in corsi:
            if str(c[4]) == str(self.user[6][0]):
                newstr = f"[{c[0]}] {c[2]} - {c[1]} CFU"
                self.ui.comboBox.addItem(newstr)
        self.ui.InviaRichiestaButton.clicked.connect(self.inviaRichiesta)
        self.ui.AggiornaStoricoButton.clicked.connect(self.aggiornaStorico)
        self.data = None
        self.aggiornaStorico()




    def aggiornaStorico(self):
        payload = {"Matricola": self.user[0]}
        rows = json.loads(launchMethod(request_constructor_str(payload, "GetRichiesteDateEsamiByMatricola"), "127.0.0.1", 5000))

        #print(rows)
        if rows["result"] == "false":
            QMessageBox.information(None, "Attenzione",
                                    f"Nessuna richiesta disponibile")
            self.data = None
        else:
            if self.data == None:
                for r in rows["result"]:
                    self.createRow(r)
                self.data = rows
            elif self.data != rows:
                self.data = rows
                for r in rows["result"]:
                    self.createRow(r)

    def inviaRichiesta(self):
        selected = self.ui.comboBox.currentText()
        pattern = r'\[(.*?)\]'
        selected = re.search(pattern, selected)
        selected = selected.group(1)
        payload = {"EsameRichiesto": selected, "MatricolaRichiedente": self.user[0]}
        print(f"Payload: {payload}")
        result = launchMethod(request_constructor_str(payload, "PutDataRichiestaDate"), "127.0.0.1", 5000)
        result = json.loads(result)
        if result['result'] == "OK":
            QMessageBox.information(None, "Accept - Success", "Richiesta Inviata con successo")
        self.clearTableView()
        self.aggiornaStorico()

    def createRow(self, data):
        layout = QHBoxLayout()


        layout.addWidget(QLabel(data[0]))
        layout.addWidget(QLabel(data[1]))

        newButton_mostradate = QPushButton("Mostra date")
        newButton_mostradate.clicked.connect(lambda: self.showDialogDates(data[3]))

        if data[2] == "?":
            label = QLabel("In attesa")
            label.setStyleSheet('color: GoldenRod')
            layout.addWidget(label)
            newButton_mostradate.setEnabled(False)
        elif data[2] == "0":
            label = QLabel("Declinata")
            label.setStyleSheet('color: red')
            layout.addWidget(label)
            newButton_mostradate.setEnabled(False)
        elif data[2] == "1":
            label = QLabel("Accetta")
            label.setStyleSheet('color: green')
            layout.addWidget(label)
            newButton_mostradate.setEnabled(True)

        layout.addWidget(newButton_mostradate)

        # Set the layout of the widget
        self.ui.TableView.addLayout(layout)

    def showDialogDates(self, data):
        QMessageBox.information(None, "Placeholder della dialogbox", f"JSON Date ricevuto {data}")

    def clearTableView(self):
        # Remove all layouts from TableView
        while self.ui.TableView.count():
            item = self.ui.TableView.takeAt(0)
            if item:
                widget = item.widget()
                if widget:
                    widget.deleteLater()
                else:
                    layout = item.layout()
                    if layout:
                        # Recursively clear layout's items
                        self.clearLayout(layout)

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            else:
                self.clearLayout(item.layout())


def run():
    dialog = StudentsDialogRichiestaDateLogic()
    dialog.exec_()


if __name__ == "__main__":
    run()
