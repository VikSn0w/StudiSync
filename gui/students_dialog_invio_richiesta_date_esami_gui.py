# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'students_dialog_invio_richiesta_date_esami_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Invio_Richiesta_Date_Esami(object):
    def setupUi(self, Invio_Richiesta_Date_Esami):
        Invio_Richiesta_Date_Esami.setObjectName("Invio_Richiesta_Date_Esami")
        Invio_Richiesta_Date_Esami.resize(534, 278)
        self.verticalLayout = QtWidgets.QVBoxLayout(Invio_Richiesta_Date_Esami)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Invio_Richiesta_Date_Esami)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.CorsoLaureaLabel = QtWidgets.QLabel(Invio_Richiesta_Date_Esami)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CorsoLaureaLabel.sizePolicy().hasHeightForWidth())
        self.CorsoLaureaLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.CorsoLaureaLabel.setFont(font)
        self.CorsoLaureaLabel.setObjectName("CorsoLaureaLabel")
        self.horizontalLayout_2.addWidget(self.CorsoLaureaLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Invio_Richiesta_Date_Esami)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Invio_Richiesta_Date_Esami)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.InviaRichiestaButton = QtWidgets.QPushButton(Invio_Richiesta_Date_Esami)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InviaRichiestaButton.setFont(font)
        self.InviaRichiestaButton.setObjectName("InviaRichiestaButton")
        self.verticalLayout.addWidget(self.InviaRichiestaButton)

        self.retranslateUi(Invio_Richiesta_Date_Esami)
        QtCore.QMetaObject.connectSlotsByName(Invio_Richiesta_Date_Esami)

    def retranslateUi(self, Invio_Richiesta_Date_Esami):
        _translate = QtCore.QCoreApplication.translate
        Invio_Richiesta_Date_Esami.setWindowTitle(_translate("Invio_Richiesta_Date_Esami", "StudiSync - Students Richiesta Date Esami"))
        self.label_2.setText(_translate("Invio_Richiesta_Date_Esami", "Esami relativi al corso di laurea:"))
        self.CorsoLaureaLabel.setText(_translate("Invio_Richiesta_Date_Esami", "0124 - Informatica"))
        self.label.setText(_translate("Invio_Richiesta_Date_Esami", "Seleziona Corso:"))
        self.InviaRichiestaButton.setText(_translate("Invio_Richiesta_Date_Esami", "Invia Richiesta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Invio_Richiesta_Date_Esami = QtWidgets.QDialog()
    ui = Ui_Invio_Richiesta_Date_Esami()
    ui.setupUi(Invio_Richiesta_Date_Esami)
    Invio_Richiesta_Date_Esami.show()
    sys.exit(app.exec_())