import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str
from gui.login_gui import Ui_Login


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.LoginButton.clicked.connect(self.checkLogin)

    def checkLogin(self):
        password = str(customHash(self.ui.PasswordField.text()))
        username = self.ui.EmailField.text()
        combobox = self.ui.ComboBoxSelect.currentText()
        result = None

        if combobox == "Students":
            toSend = {"Matricola":username, "Password": password}
            result = launchMethod(request_constructor_str(toSend,"StudentsLogin"),"127.0.0.1", 1024)

        elif combobox == "Office":
            toSend = {"Email": username, "Password": password}
            result = launchMethod(request_constructor_str(toSend, "OfficeLogin"), "127.0.0.1", 1024)

        if result == "false":
            QMessageBox.critical(None, "Login - Error", "")

    def openMainWindow(self):
        print("open")
        '''self.main_window = MetaphaseWindow()
        self.close()
        self.main_window.show()
        self.main_window.ui.nameLabel.setText(self.ui.usernameTextField.text())'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
