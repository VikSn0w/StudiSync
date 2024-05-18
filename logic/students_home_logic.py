from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog

from common.communication import customHash, request_constructor_str, formato_data,request_constructor_obj
from gui.students_home_gui import Ui_Students_Home
from logic.students_dialog_richiedi_date_logic import StudentsDialogRichiestaDateLogic


class StudentsHomeLogic(QMainWindow):
    user = None

    def __init__(self, user):
        self.user = user
        super().__init__()
        self.ui = Ui_Students_Home()
        self.ui.setupUi(self)
        self.ui.InvioRichiestaButton.clicked.connect(self.showDialogRichiediDate)


    def showWindow(self, user):
        self.show()
        self.user = user
        self.ui.MtrLabel.setText(user[0])
        self.ui.NameLastnameLabel.setText(f"{user[1]}, {user[2]}")
        self.ui.DateLabel.setText(f"{formato_data()}")

    def showDialogRichiediDate(self):
        dialog = StudentsDialogRichiestaDateLogic(self.user)
        dialog.exec_()


def run(user):
    window = StudentsHomeLogic(user)
    window.show()


if __name__ == "__main__":
    run('["0124002584", "Vittorio", "Picone", "vittorio.picone001@studenti.uniparthenope.it", "1914752590"]')
