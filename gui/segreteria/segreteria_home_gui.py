# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'segreteria_home_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Segreteria_Home(object):
    def setupUi(self, Segreteria_Home):
        Segreteria_Home.setObjectName("Segreteria_Home")
        Segreteria_Home.resize(564, 361)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        Segreteria_Home.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Segreteria_Home)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.NameLastnameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.NameLastnameLabel.setFont(font)
        self.NameLastnameLabel.setObjectName("NameLastnameLabel")
        self.horizontalLayout.addWidget(self.NameLastnameLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.DateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.DateLabel.setFont(font)
        self.DateLabel.setObjectName("DateLabel")
        self.horizontalLayout.addWidget(self.DateLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.MtrLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.MtrLabel.setFont(font)
        self.MtrLabel.setObjectName("MtrLabel")
        self.horizontalLayout.addWidget(self.MtrLabel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.InserimentoEsamiButton = QtWidgets.QPushButton(self.centralwidget)
        self.InserimentoEsamiButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.InserimentoEsamiButton.setFont(font)
        self.InserimentoEsamiButton.setObjectName("InserimentoEsamiButton")
        self.gridLayout_2.addWidget(self.InserimentoEsamiButton, 0, 0, 1, 1)
        self.InserimentoLaureaButton = QtWidgets.QPushButton(self.centralwidget)
        self.InserimentoLaureaButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.InserimentoLaureaButton.setFont(font)
        self.InserimentoLaureaButton.setObjectName("InserimentoLaureaButton")
        self.gridLayout_2.addWidget(self.InserimentoLaureaButton, 0, 1, 1, 1)
        self.InoltraRichiestaButton = QtWidgets.QPushButton(self.centralwidget)
        self.InoltraRichiestaButton.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.InoltraRichiestaButton.setFont(font)
        self.InoltraRichiestaButton.setObjectName("InoltraRichiestaButton")
        self.gridLayout_2.addWidget(self.InoltraRichiestaButton, 2, 1, 1, 1)
        self.DateDiposnibiliEsami = QtWidgets.QPushButton(self.centralwidget)
        self.DateDiposnibiliEsami.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.DateDiposnibiliEsami.setFont(font)
        self.DateDiposnibiliEsami.setObjectName("DateDiposnibiliEsami")
        self.gridLayout_2.addWidget(self.DateDiposnibiliEsami, 2, 0, 1, 1)
        self.AggiungiAppello = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        self.AggiungiAppello.setFont(font)
        self.AggiungiAppello.setObjectName("AggiungiAppello")
        self.gridLayout_2.addWidget(self.AggiungiAppello, 3, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem3)
        Segreteria_Home.setCentralWidget(self.centralwidget)
        self.actionCIso = QtWidgets.QAction(Segreteria_Home)
        self.actionCIso.setObjectName("actionCIso")
        self.actionCiao = QtWidgets.QAction(Segreteria_Home)
        self.actionCiao.setObjectName("actionCiao")

        self.retranslateUi(Segreteria_Home)
        QtCore.QMetaObject.connectSlotsByName(Segreteria_Home)

    def retranslateUi(self, Segreteria_Home):
        _translate = QtCore.QCoreApplication.translate
        Segreteria_Home.setWindowTitle(_translate("Segreteria_Home", "StudiSync - Segreteria Home"))
        self.label_6.setText(_translate("Segreteria_Home", "Ciao"))
        self.NameLastnameLabel.setText(_translate("Segreteria_Home", "Nome, Cognome"))
        self.DateLabel.setText(_translate("Segreteria_Home", "Lunedì 13/05/2024 20:40"))
        self.label_7.setText(_translate("Segreteria_Home", "ID"))
        self.MtrLabel.setText(_translate("Segreteria_Home", "1"))
        self.InserimentoEsamiButton.setText(_translate("Segreteria_Home", "Crea nuovo corso"))
        self.InserimentoLaureaButton.setText(_translate("Segreteria_Home", "Crea nuova laurea"))
        self.InoltraRichiestaButton.setText(_translate("Segreteria_Home", "Prenotazioni appelli studenti"))
        self.DateDiposnibiliEsami.setText(_translate("Segreteria_Home", "Richieste studenti"))
        self.AggiungiAppello.setText(_translate("Segreteria_Home", "Aggiungi Appello"))
        self.actionCIso.setText(_translate("Segreteria_Home", "CIso"))
        self.actionCiao.setText(_translate("Segreteria_Home", "Ciao"))
