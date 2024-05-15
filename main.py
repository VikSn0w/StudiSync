import os
import platform
import subprocess
import sys
from multiprocessing import Process

from PyQt5.QtWidgets import QApplication

from logic.login_logic import LoginLogic
from logic.students_home_logic import StudentsHomeLogic
from logic.segreteria_home_logic import SegreteriaHomeLogic
from combined_multiplex_concurrent_server import server_main


def main():
    app = QApplication(sys.argv)

    login_window = LoginLogic()
    students_window = StudentsHomeLogic(login_window.user)
    segreteria_window = SegreteriaHomeLogic(login_window.user)
    login_window.show_students_home.connect(lambda: students_window.showWindow(login_window.user))
    login_window.show_office_home.connect(lambda: segreteria_window.showWindow(login_window.user))

    login_window.show()

    app.exec_()

if __name__ == "__main__":
    server = Process(target=server_main, args=('127.0.0.1', 5000))
    server.start()
    main()
    server.kill()



