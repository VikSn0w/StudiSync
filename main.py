import sys

from PyQt5.QtWidgets import QApplication

from logic.login_logic import LoginLogic
from logic.students_home_logic import StudentsHomeLogic
from logic.segreteria_home_logic import SegreteriaHomeLogic

def main():
    app = QApplication(sys.argv)

    login_window = LoginLogic()
    students_window = StudentsHomeLogic(login_window.user)
    segreteria_window = SegreteriaHomeLogic(login_window.user)
    login_window.show_students_home.connect(lambda: students_window.showWindow(login_window.user))
    login_window.show_office_home.connect(lambda: segreteria_window.showWindow(login_window.user))

    login_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()