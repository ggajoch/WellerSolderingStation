# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1094, 427)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.connectSerialButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectSerialButton.sizePolicy().hasHeightForWidth())
        self.connectSerialButton.setSizePolicy(sizePolicy)
        self.connectSerialButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.connectSerialButton.setObjectName(_fromUtf8("connectSerialButton"))
        self.gridLayout.addWidget(self.connectSerialButton, 2, 3, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 8, 1, 1)
        self.offsetSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(70)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offsetSpinBox.sizePolicy().hasHeightForWidth())
        self.offsetSpinBox.setSizePolicy(sizePolicy)
        self.offsetSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.offsetSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.offsetSpinBox.setObjectName(_fromUtf8("offsetSpinBox"))
        self.gridLayout.addWidget(self.offsetSpinBox, 1, 9, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setMinimumSize(QtCore.QSize(40, 0))
        self.label_4.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 8, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 3, 6, 1, 1)
        self.KiSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.KiSpinBox.setObjectName(_fromUtf8("KiSpinBox"))
        self.gridLayout.addWidget(self.KiSpinBox, 2, 7, 1, 1)
        self.gainSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.gainSpinBox.setObjectName(_fromUtf8("gainSpinBox"))
        self.gridLayout.addWidget(self.gainSpinBox, 2, 9, 1, 1)
        self.KpSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.KpSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.KpSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.KpSpinBox.setObjectName(_fromUtf8("KpSpinBox"))
        self.gridLayout.addWidget(self.KpSpinBox, 1, 7, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 6, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(25, 0))
        self.label_6.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1)
        self.KdSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.KdSpinBox.setObjectName(_fromUtf8("KdSpinBox"))
        self.gridLayout.addWidget(self.KdSpinBox, 3, 7, 1, 1)
        self.setpointSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.setpointSpinBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.setpointSpinBox.setMaximum(999.99)
        self.setpointSpinBox.setSingleStep(5.0)
        self.setpointSpinBox.setObjectName(_fromUtf8("setpointSpinBox"))
        self.gridLayout.addWidget(self.setpointSpinBox, 1, 5, 1, 1)
        self.disconnectButton = QtGui.QPushButton(self.centralwidget)
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.gridLayout.addWidget(self.disconnectButton, 3, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 10, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(70, 0))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 10, 1, 1)
        self.deviceTextEdit = QtGui.QLineEdit(self.centralwidget)
        self.deviceTextEdit.setObjectName(_fromUtf8("deviceTextEdit"))
        self.gridLayout.addWidget(self.deviceTextEdit, 1, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(55, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 4, 1, 1)
        self.maxPowerSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.maxPowerSpinBox.setMaximum(100.0)
        self.maxPowerSpinBox.setObjectName(_fromUtf8("maxPowerSpinBox"))
        self.gridLayout.addWidget(self.maxPowerSpinBox, 2, 5, 1, 1)
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 12, 1, 1)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 1, 12, 1, 1)
        self.standTemperatureSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.standTemperatureSpinBox.setMaximum(999)
        self.standTemperatureSpinBox.setSingleStep(5)
        self.standTemperatureSpinBox.setObjectName(_fromUtf8("standTemperatureSpinBox"))
        self.gridLayout.addWidget(self.standTemperatureSpinBox, 2, 13, 1, 1)
        self.sleepTemperatureSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.sleepTemperatureSpinBox.setMaximum(999)
        self.sleepTemperatureSpinBox.setSingleStep(5)
        self.sleepTemperatureSpinBox.setObjectName(_fromUtf8("sleepTemperatureSpinBox"))
        self.gridLayout.addWidget(self.sleepTemperatureSpinBox, 1, 13, 1, 1)
        self.brightnessSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightnessSpinBox.sizePolicy().hasHeightForWidth())
        self.brightnessSpinBox.setSizePolicy(sizePolicy)
        self.brightnessSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.brightnessSpinBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.brightnessSpinBox.setMaximum(100.0)
        self.brightnessSpinBox.setObjectName(_fromUtf8("brightnessSpinBox"))
        self.gridLayout.addWidget(self.brightnessSpinBox, 1, 11, 1, 1)
        self.contrastSpinBox = QtGui.QDoubleSpinBox(self.centralwidget)
        self.contrastSpinBox.setEnabled(True)
        self.contrastSpinBox.setMinimumSize(QtCore.QSize(70, 0))
        self.contrastSpinBox.setMaximum(100.0)
        self.contrastSpinBox.setObjectName(_fromUtf8("contrastSpinBox"))
        self.gridLayout.addWidget(self.contrastSpinBox, 2, 11, 1, 1)
        self.connectSimulatorButton = QtGui.QPushButton(self.centralwidget)
        self.connectSimulatorButton.setObjectName(_fromUtf8("connectSimulatorButton"))
        self.gridLayout.addWidget(self.connectSimulatorButton, 3, 13, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSimulator = QtGui.QAction(MainWindow)
        self.actionSimulator.setObjectName(_fromUtf8("actionSimulator"))
        self.actionDisconnect = QtGui.QAction(MainWindow)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionTip_Calibration = QtGui.QAction(MainWindow)
        self.actionTip_Calibration.setObjectName(_fromUtf8("actionTip_Calibration"))
        self.actionPID_Calibration = QtGui.QAction(MainWindow)
        self.actionPID_Calibration.setObjectName(_fromUtf8("actionPID_Calibration"))
        self.actionSetpoint = QtGui.QAction(MainWindow)
        self.actionSetpoint.setObjectName(_fromUtf8("actionSetpoint"))
        self.actionDisplay = QtGui.QAction(MainWindow)
        self.actionDisplay.setObjectName(_fromUtf8("actionDisplay"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.disconnectButton, self.setpointSpinBox)
        MainWindow.setTabOrder(self.setpointSpinBox, self.KpSpinBox)
        MainWindow.setTabOrder(self.KpSpinBox, self.KiSpinBox)
        MainWindow.setTabOrder(self.KiSpinBox, self.KdSpinBox)
        MainWindow.setTabOrder(self.KdSpinBox, self.offsetSpinBox)
        MainWindow.setTabOrder(self.offsetSpinBox, self.gainSpinBox)
        MainWindow.setTabOrder(self.gainSpinBox, self.widget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.connectSerialButton.setText(_translate("MainWindow", "Connect", None))
        self.label_5.setText(_translate("MainWindow", "Gain:", None))
        self.label_4.setText(_translate("MainWindow", "Offset:", None))
        self.label_8.setText(_translate("MainWindow", "Kd:", None))
        self.label_7.setText(_translate("MainWindow", "Ki:", None))
        self.label_6.setText(_translate("MainWindow", "Kp:", None))
        self.disconnectButton.setText(_translate("MainWindow", "Disconnect", None))
        self.label_2.setText(_translate("MainWindow", "Contrast:", None))
        self.label.setText(_translate("MainWindow", "Brightness:", None))
        self.deviceTextEdit.setPlaceholderText(_translate("MainWindow", "Serial port", None))
        self.label_9.setText(_translate("MainWindow", "Max power:", None))
        self.label_3.setText(_translate("MainWindow", "Setpoint:", None))
        self.label_10.setText(_translate("MainWindow", "Stand temperature:", None))
        self.label_11.setText(_translate("MainWindow", "Sleep temperature:", None))
        self.connectSimulatorButton.setText(_translate("MainWindow", "Simulator", None))
        self.actionSimulator.setText(_translate("MainWindow", "Simulator", None))
        self.actionDisconnect.setText(_translate("MainWindow", "Disconnect", None))
        self.actionTip_Calibration.setText(_translate("MainWindow", "Tip Calibration", None))
        self.actionPID_Calibration.setText(_translate("MainWindow", "PID Calibration", None))
        self.actionSetpoint.setText(_translate("MainWindow", "Temperature", None))
        self.actionDisplay.setText(_translate("MainWindow", "Display", None))

from pyqtgraph import PlotWidget
