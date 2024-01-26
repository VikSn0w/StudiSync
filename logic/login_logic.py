import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from pyqt5_plugins.examplebutton import QtWidgets

from SelMultiplexClient import launchMethod
from common.communication import customHash, request_constructor_str
from gui.login_gui import Ui_Login
from logic import students_home_logic

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
            QMessageBox.critical(None, "Login - Error", "Email, Password or User type incorrect.\nCheck your info and retry.")
        else:
            self.openMainWindow(result)
    def openMainWindow(self,user):
        print("open")
        students_home_logic.run(user)
        self.close()

def run():
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()