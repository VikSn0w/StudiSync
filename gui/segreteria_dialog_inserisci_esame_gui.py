# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segreteria_dialog_inserisci_esame_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_segreteria_dialog_inserisci_esame(object):
    def setupUi(self, segreteria_dialog_inserisci_esame):
        segreteria_dialog_inserisci_esame.setObjectName("segreteria_dialog_inserisci_esame")
        segreteria_dialog_inserisci_esame.resize(394, 379)
        self.gridLayout = QtWidgets.QGridLayout(segreteria_dialog_inserisci_esame)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 26, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        self.InsertEsameButton = QtWidgets.QPushButton(segreteria_dialog_inserisci_esame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InsertEsameButton.setFont(font)
        self.InsertEsameButton.setObjectName("InsertEsameButton")
        self.gridLayout.addWidget(self.InsertEsameButton, 5, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(segreteria_dialog_inserisci_esame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.NomeProfessoreField = QtWidgets.QLineEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NomeProfessoreField.setFont(font)
        self.NomeProfessoreField.setText("")
        self.NomeProfessoreField.setObjectName("NomeProfessoreField")
        self.verticalLayout_2.addWidget(self.NomeProfessoreField)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(segreteria_dialog_inserisci_esame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comboBoxLaurea = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxLaurea.setObjectName("comboBoxLaurea")
        self.verticalLayout_3.addWidget(self.comboBoxLaurea)
        self.gridLayout.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(segreteria_dialog_inserisci_esame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NomeEsameField = QtWidgets.QLineEdit(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.NomeEsameField.setFont(font)
        self.NomeEsameField.setText("")
        self.NomeEsameField.setObjectName("NomeEsameField")
        self.verticalLayout.addWidget(self.NomeEsameField)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(segreteria_dialog_inserisci_esame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.CFUSpinBox = QtWidgets.QSpinBox(self.groupBox_4)
        self.CFUSpinBox.setMinimum(1)
        self.CFUSpinBox.setObjectName("CFUSpinBox")
        self.verticalLayout_5.addWidget(self.CFUSpinBox)
        self.gridLayout.addWidget(self.groupBox_4, 4, 0, 1, 1)

        self.retranslateUi(segreteria_dialog_inserisci_esame)
        QtCore.QMetaObject.connectSlotsByName(segreteria_dialog_inserisci_esame)

    def retranslateUi(self, segreteria_dialog_inserisci_esame):
        _translate = QtCore.QCoreApplication.translate
        segreteria_dialog_inserisci_esame.setWindowTitle(_translate("segreteria_dialog_inserisci_esame", "StudiSync - Segreteria Inserisci Esame"))
        self.InsertEsameButton.setText(_translate("segreteria_dialog_inserisci_esame", "Inserisci Esami"))
        self.groupBox_2.setTitle(_translate("segreteria_dialog_inserisci_esame", "Nome Professore"))
        self.groupBox_3.setTitle(_translate("segreteria_dialog_inserisci_esame", "Corso di Laurea"))
        self.groupBox.setTitle(_translate("segreteria_dialog_inserisci_esame", "Nome Esame"))
        self.groupBox_4.setTitle(_translate("segreteria_dialog_inserisci_esame", "CFU"))
