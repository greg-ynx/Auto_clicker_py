import sys

from PyQt5 import QtWidgets
from src.app.ui.MainWindow.main_window import Ui_main_window


def main():
    print('main')
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
