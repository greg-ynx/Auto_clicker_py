import sys
from PyQt5 import QtWidgets
from src.app.UI.UIMainWindow.UIMainWindow import UIMainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = UIMainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
