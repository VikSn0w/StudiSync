import json
import os
import re

from PyQt5.QtWidgets import QMessageBox, QDialog, QHBoxLayout, QLabel, QPushButton
# from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import request_constructor_str, loadJSONFromFile
from gui.students.students_dialog_prenotazioni import Ui_student_dialog_prenotazioni


class StudentsDialogPrenotazioneLogic(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_student_dialog_prenotazioni()
        self.ui.setupUi(self)


def run():
    dialog = StudentsDialogPrenotazioneLogic()
    dialog.exec_()


if __name__ == "__main__":
    run()
