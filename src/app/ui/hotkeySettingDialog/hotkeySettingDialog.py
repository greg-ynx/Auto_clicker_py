# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hotkeySettingDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hotkeySetting_Dialog(object):
    def setupUi(self, hotkeySetting_Dialog):
        hotkeySetting_Dialog.setObjectName("hotkeySetting_Dialog")
        hotkeySetting_Dialog.resize(320, 240)
        hotkeySetting_Dialog.setMinimumSize(QtCore.QSize(320, 240))
        hotkeySetting_Dialog.setMaximumSize(QtCore.QSize(320, 240))
        self.hotkeySetting_buttonBox = QtWidgets.QDialogButtonBox(hotkeySetting_Dialog)
        self.hotkeySetting_buttonBox.setGeometry(QtCore.QRect(10, 200, 301, 32))
        self.hotkeySetting_buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.hotkeySetting_buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.hotkeySetting_buttonBox.setObjectName("hotkeySetting_buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(hotkeySetting_Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 301, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hotkeySetting_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hotkeySetting_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.hotkeySetting_horizontalLayout.setObjectName("hotkeySetting_horizontalLayout")
        self.hotkeySetting_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hotkeySetting_button.setMinimumSize(QtCore.QSize(150, 0))
        self.hotkeySetting_button.setMaximumSize(QtCore.QSize(150, 50))
        self.hotkeySetting_button.setObjectName("hotkeySetting_button")
        self.hotkeySetting_horizontalLayout.addWidget(self.hotkeySetting_button)
        self.hotkeySetting_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.hotkeySetting_lineEdit.setEnabled(True)
        self.hotkeySetting_lineEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.hotkeySetting_lineEdit.setMaximumSize(QtCore.QSize(150, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(193, 193, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.hotkeySetting_lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.hotkeySetting_lineEdit.setFont(font)
        self.hotkeySetting_lineEdit.setAutoFillBackground(False)
        self.hotkeySetting_lineEdit.setText("F6")
        self.hotkeySetting_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.hotkeySetting_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.hotkeySetting_lineEdit.setReadOnly(True)
        self.hotkeySetting_lineEdit.setObjectName("hotkeySetting_lineEdit")
        self.hotkeySetting_horizontalLayout.addWidget(self.hotkeySetting_lineEdit)

        self.retranslateUi(hotkeySetting_Dialog)
        self.hotkeySetting_buttonBox.accepted.connect(hotkeySetting_Dialog.accept) # type: ignore
        self.hotkeySetting_buttonBox.rejected.connect(hotkeySetting_Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(hotkeySetting_Dialog)

    def retranslateUi(self, hotkeySetting_Dialog):
        _translate = QtCore.QCoreApplication.translate
        hotkeySetting_Dialog.setWindowTitle(_translate("hotkeySetting_Dialog", "Dialog"))
        self.hotkeySetting_button.setText(_translate("hotkeySetting_Dialog", "Start / Stop"))
