# -*- coding: utf-8 -*-

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from config.definitions import img_dir
from src.app._Service.ParametersService import ParametersService


class UIMainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setEnabled(True)
        MainWindow.resize(435, 340)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(435, 340))
        MainWindow.setMaximumSize(QtCore.QSize(435, 340))
        MainWindow.setBaseSize(QtCore.QSize(435, 340))

        self.params = ParametersService()

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(os.path.join(img_dir, "icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.main_centralWidget = QtWidgets.QWidget(MainWindow)
        self.main_centralWidget.setObjectName("main_centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.clickInterval_groupBox = QtWidgets.QGroupBox(self.main_centralWidget)
        self.clickInterval_groupBox.setFlat(False)
        self.clickInterval_groupBox.setObjectName("clickInterval_groupBox")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.clickInterval_groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.hours_spinBox = QtWidgets.QSpinBox(self.clickInterval_groupBox)
        self.hours_spinBox.setMaximum(9999)
        self.hours_spinBox.setObjectName("hours_spinBox")
        self.horizontalLayout.addWidget(self.hours_spinBox)

        self.hours_label = QtWidgets.QLabel(self.clickInterval_groupBox)
        self.hours_label.setObjectName("hours_label")
        self.horizontalLayout.addWidget(self.hours_label)

        self.mins_spinBox = QtWidgets.QSpinBox(self.clickInterval_groupBox)
        self.mins_spinBox.setMaximum(9999)
        self.mins_spinBox.setObjectName("mins_spinBox")
        self.horizontalLayout.addWidget(self.mins_spinBox)

        self.mins_label = QtWidgets.QLabel(self.clickInterval_groupBox)
        self.mins_label.setObjectName("mins_label")
        self.horizontalLayout.addWidget(self.mins_label)

        self.secs_spinBox = QtWidgets.QSpinBox(self.clickInterval_groupBox)
        self.secs_spinBox.setMaximum(9999)
        self.secs_spinBox.setObjectName("secs_spinBox")
        self.horizontalLayout.addWidget(self.secs_spinBox)

        self.secs_label = QtWidgets.QLabel(self.clickInterval_groupBox)
        self.secs_label.setObjectName("secs_label")
        self.horizontalLayout.addWidget(self.secs_label)

        self.ms_spinBox = QtWidgets.QSpinBox(self.clickInterval_groupBox)
        self.ms_spinBox.setMinimum(1)
        self.ms_spinBox.setMaximum(9999)
        self.ms_spinBox.setProperty("value", 100)
        self.ms_spinBox.setObjectName("ms_spinBox")
        self.horizontalLayout.addWidget(self.ms_spinBox)

        self.ms_label = QtWidgets.QLabel(self.clickInterval_groupBox)
        self.ms_label.setObjectName("ms_label")
        self.horizontalLayout.addWidget(self.ms_label)

        self.verticalLayout.addWidget(self.clickInterval_groupBox)

        self.optionsRepeat_horizontalLayout = QtWidgets.QHBoxLayout()
        self.optionsRepeat_horizontalLayout.setObjectName("optionsRepeat_horizontalLayout")

        self.clickOptions_groupBox = QtWidgets.QGroupBox(self.main_centralWidget)
        self.clickOptions_groupBox.setObjectName("clickOptions_groupBox")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.clickOptions_groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.mouseButton_horizontalLayout = QtWidgets.QHBoxLayout()
        self.mouseButton_horizontalLayout.setObjectName("mouseButton_horizontalLayout")

        self.mouseButton_label = QtWidgets.QLabel(self.clickOptions_groupBox)
        self.mouseButton_label.setObjectName("mouseButton_label")
        self.mouseButton_horizontalLayout.addWidget(self.mouseButton_label)

        self.mouseButton_comboBox = QtWidgets.QComboBox(self.clickOptions_groupBox)
        self.mouseButton_comboBox.setObjectName("mouseButton_comboBox")
        self.mouseButton_comboBox.addItems(["Left", "Right", "Middle"])
        self.mouseButton_horizontalLayout.addWidget(self.mouseButton_comboBox)

        self.verticalLayout_2.addLayout(self.mouseButton_horizontalLayout)

        self.clickType_horizontalLayout = QtWidgets.QHBoxLayout()
        self.clickType_horizontalLayout.setObjectName("clickType_horizontalLayout")

        self.clickType_label = QtWidgets.QLabel(self.clickOptions_groupBox)
        self.clickType_label.setObjectName("clickType_label")
        self.clickType_horizontalLayout.addWidget(self.clickType_label)

        self.clickType_comboBox = QtWidgets.QComboBox(self.clickOptions_groupBox)
        self.clickType_comboBox.setObjectName("clickType_comboBox")
        self.clickType_comboBox.addItems(["Single", "Double"])
        self.clickType_horizontalLayout.addWidget(self.clickType_comboBox)

        self.verticalLayout_2.addLayout(self.clickType_horizontalLayout)

        self.optionsRepeat_horizontalLayout.addWidget(self.clickOptions_groupBox)

        self.clickRepeat_groupBox = QtWidgets.QGroupBox(self.main_centralWidget)
        self.clickRepeat_groupBox.setObjectName("clickRepeat_groupBox")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.clickRepeat_groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.repeat_horizontalLayout = QtWidgets.QHBoxLayout()
        self.repeat_horizontalLayout.setObjectName("repeat_horizontalLayout")

        self.repeat_radioButton = QtWidgets.QRadioButton(self.clickRepeat_groupBox)
        self.repeat_radioButton.setObjectName("repeat_radioButton")
        self.repeat_horizontalLayout.addWidget(self.repeat_radioButton)

        self.repeat_spinBox = QtWidgets.QSpinBox(self.clickRepeat_groupBox)
        self.repeat_spinBox.setMinimum(1)
        self.repeat_spinBox.setMaximum(999999999)
        self.repeat_horizontalLayout.addWidget(self.repeat_spinBox)

        self.repeat_label = QtWidgets.QLabel(self.clickRepeat_groupBox)
        self.repeat_label.setObjectName("repeat_label")
        self.repeat_horizontalLayout.addWidget(self.repeat_label)

        self.verticalLayout_3.addLayout(self.repeat_horizontalLayout)

        self.repeatUntilStopped_horizontalLayout = QtWidgets.QHBoxLayout()
        self.repeatUntilStopped_horizontalLayout.setObjectName("repeatUntilStopped_horizontalLayout")

        self.repeatUntilStopped_radioButton = QtWidgets.QRadioButton(self.clickRepeat_groupBox)
        self.repeatUntilStopped_radioButton.setChecked(True)
        self.repeatUntilStopped_radioButton.setObjectName("repeatUntilStopped_radioButton")
        self.repeatUntilStopped_horizontalLayout.addWidget(self.repeatUntilStopped_radioButton)

        self.verticalLayout_3.addLayout(self.repeatUntilStopped_horizontalLayout)

        self.optionsRepeat_horizontalLayout.addWidget(self.clickRepeat_groupBox)

        self.verticalLayout.addLayout(self.optionsRepeat_horizontalLayout)

        self.cursorPosition_groupBox = QtWidgets.QGroupBox(self.main_centralWidget)
        self.cursorPosition_groupBox.setObjectName("cursorPosition_groupBox")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cursorPosition_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.currentLocation_radioButton = QtWidgets.QRadioButton(self.cursorPosition_groupBox)
        self.currentLocation_radioButton.setChecked(True)
        self.currentLocation_radioButton.setObjectName("currentLocation_radioButton")

        self.horizontalLayout_2.addWidget(self.currentLocation_radioButton)

        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem)

        self.customLocation_radioButton = QtWidgets.QRadioButton(self.cursorPosition_groupBox)
        self.customLocation_radioButton.setText("")
        self.customLocation_radioButton.setObjectName("customLocation_radioButton")
        self.horizontalLayout_2.addWidget(self.customLocation_radioButton)

        self.X_label = QtWidgets.QLabel(self.cursorPosition_groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.X_label.setFont(font)
        self.X_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.X_label.setObjectName("X_label")
        self.horizontalLayout_2.addWidget(self.X_label)

        self.X_lineEdit = QtWidgets.QLineEdit(self.cursorPosition_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.X_lineEdit.sizePolicy().hasHeightForWidth())
        self.X_lineEdit.setSizePolicy(sizePolicy)
        self.X_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.X_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.X_lineEdit.setText("0")
        self.X_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.X_lineEdit.setReadOnly(True)
        self.X_lineEdit.setObjectName("X_lineEdit")
        self.horizontalLayout_2.addWidget(self.X_lineEdit)

        self.Y_label = QtWidgets.QLabel(self.cursorPosition_groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Y_label.setFont(font)
        self.Y_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Y_label.setObjectName("Y_label")
        self.horizontalLayout_2.addWidget(self.Y_label)

        self.Y_lineEdit = QtWidgets.QLineEdit(self.cursorPosition_groupBox)
        self.Y_lineEdit.setMinimumSize(QtCore.QSize(50, 0))
        self.Y_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.Y_lineEdit.setText("0")
        self.Y_lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Y_lineEdit.setReadOnly(True)
        self.Y_lineEdit.setObjectName("Y_lineEdit")
        self.horizontalLayout_2.addWidget(self.Y_lineEdit)

        self.verticalLayout.addWidget(self.cursorPosition_groupBox)

        self.startStop_gridLayout = QtWidgets.QGridLayout()
        self.startStop_gridLayout.setObjectName("startStop_gridLayout")

        self.start_pushButton = QtWidgets.QPushButton(self.main_centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_pushButton.sizePolicy().hasHeightForWidth())
        self.start_pushButton.setSizePolicy(sizePolicy)
        self.start_pushButton.setMinimumSize(QtCore.QSize(160, 45))
        self.start_pushButton.setObjectName("start_pushButton")
        self.start_pushButton.clicked.connect(self.start)
        self.startStop_gridLayout.addWidget(self.start_pushButton, 0, 0, 1, 1)

        self.stop_pushButton = QtWidgets.QPushButton(self.main_centralWidget)
        self.stop_pushButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_pushButton.sizePolicy().hasHeightForWidth())
        self.stop_pushButton.setSizePolicy(sizePolicy)
        self.stop_pushButton.setMinimumSize(QtCore.QSize(160, 45))
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.startStop_gridLayout.addWidget(self.stop_pushButton, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.startStop_gridLayout)

        self.currentLocation_radioButton.toggled.connect(self.currentLocation_toggled)
        self.customLocation_radioButton.toggled.connect(self.customLocation_toggled)

        self.stop_pushButton.clicked.connect(self.stop)

        MainWindow.setCentralWidget(self.main_centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def seconds_count(self):
        return self.hours_spinBox.value() * 60 ** 2 + \
               self.mins_spinBox.value() * 60 + \
               self.secs_spinBox.value() + \
               self.ms_spinBox.value() * 10 ** (-3)

    def start(self):
        self.start_pushButton.setEnabled(False)
        self.stop_pushButton.setEnabled(True)
        self.setAllEnabled(False)
        self.attribute_params()

    def stop(self):
        self.stop_pushButton.setEnabled(False)
        self.start_pushButton.setEnabled(True)
        self.setAllEnabled(True)

    def currentLocation_toggled(self):
        self.X_lineEdit.setReadOnly(True)
        self.Y_lineEdit.setReadOnly(True)

    def customLocation_toggled(self):
        self.X_lineEdit.setReadOnly(False)
        self.Y_lineEdit.setReadOnly(False)

    def attribute_params(self):
        self.params.click_interval = self.seconds_count()
        self.params.mouse_button = self.mouseButton_comboBox.value()
        self.params.click_type = self.clickType_comboBox.value()
        self.params.repeat_until_stopped = True
        if not self.repeatUntilStopped_radioButton.isChecked():
            self.params.repeat_until_stopped = False
            self.params.times = self.repeat_spinBox.value()
        self.params.cursor_position = True
        if not self.currentLocation_radioButton.isChecked():
            self.params.cursor_position = False
            self.params.cursor_X = self.X_lineEdit.text()
            self.params.cursor_Y = self.Y_lineEdit.text()

    def setAllEnabled(self, state: bool):
        self.hours_spinBox.setEnabled(state)
        self.mins_spinBox.setEnabled(state)
        self.secs_spinBox.setEnabled(state)
        self.ms_spinBox.setEnabled(state)
        self.mouseButton_comboBox.setEnabled(state)
        self.clickType_comboBox.setEnabled(state)
        self.repeat_radioButton.setEnabled(state)
        self.repeat_spinBox.setEnabled(state)
        self.repeatUntilStopped_radioButton.setEnabled(state)
        self.currentLocation_radioButton.setEnabled(state)
        self.customLocation_radioButton.setEnabled(state)
        self.X_lineEdit.setEnabled(state)
        self.Y_lineEdit.setEnabled(state)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto_clicker_py"))
        self.clickInterval_groupBox.setTitle(_translate("MainWindow", "Click interval"))
        self.hours_label.setText(_translate("MainWindow", "hours"))
        self.mins_label.setText(_translate("MainWindow", "mins"))
        self.secs_label.setText(_translate("MainWindow", "secs"))
        self.ms_label.setText(_translate("MainWindow", "milliseconds"))
        self.clickOptions_groupBox.setTitle(_translate("MainWindow", "Click options"))
        self.mouseButton_label.setText(_translate("MainWindow", "Mouse button:"))
        self.clickType_label.setText(_translate("MainWindow", "Click type"))
        self.clickRepeat_groupBox.setTitle(_translate("MainWindow", "Click repeat"))
        self.repeat_radioButton.setText(_translate("MainWindow", "Repeat"))
        self.repeat_label.setText(_translate("MainWindow", "times"))
        self.repeatUntilStopped_radioButton.setText(_translate("MainWindow", "Repeat until stopped"))
        self.cursorPosition_groupBox.setTitle(_translate("MainWindow", "Cursor position"))
        self.currentLocation_radioButton.setText(_translate("MainWindow", "Current location"))
        self.X_label.setText(_translate("MainWindow", "X"))
        self.Y_label.setText(_translate("MainWindow", "Y"))
        self.start_pushButton.setText(_translate("MainWindow", "Start (F6)"))
        self.stop_pushButton.setText(_translate("MainWindow", "Stop (F6)"))
