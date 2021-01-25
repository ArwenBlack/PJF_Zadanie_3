# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 490, 191, 23))
        self.pushButton.setObjectName("pushButton")
        self.plots_view = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.plots_view.setGeometry(QtCore.QRect(60, 100, 911, 361))
        self.plots_view.setObjectName("plots_view")
        self.compression_rate = QtWidgets.QPushButton(self.centralwidget)
        self.compression_rate.setGeometry(QtCore.QRect(70, 20, 171, 23))
        self.compression_rate.setObjectName("compression_rate")
        self.com_size_or_size = QtWidgets.QPushButton(self.centralwidget)
        self.com_size_or_size.setGeometry(QtCore.QRect(260, 20, 181, 23))
        self.com_size_or_size.setObjectName("com_size_or_size")
        self.com_time_orginal_size = QtWidgets.QPushButton(self.centralwidget)
        self.com_time_orginal_size.setGeometry(QtCore.QRect(460, 20, 171, 23))
        self.com_time_orginal_size.setObjectName("com_time_orginal_size")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(650, 20, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.files = QtWidgets.QSpinBox(self.centralwidget)
        self.files.setGeometry(QtCore.QRect(290, 490, 111, 22))
        self.files.setMinimum(1)
        self.files.setMaximum(500)
        self.files.setSingleStep(1)
        self.files.setObjectName("files")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(440, 490, 101, 22))
        self.spinBox.setMinimum(10000)
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setSingleStep(10000)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(600, 490, 91, 22))
        self.spinBox_2.setMinimum(20000)
        self.spinBox_2.setMaximum(2000000000)
        self.spinBox_2.setSingleStep(10000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 470, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(440, 470, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(600, 470, 71, 16))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Generate random data"))
        self.compression_rate.setText(_translate("MainWindow", "Compression rate"))
        self.com_size_or_size.setText(_translate("MainWindow", "Compression size to orginal size"))
        self.com_time_orginal_size.setText(_translate("MainWindow", "Compression time to orginal size"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "Files number"))
        self.label_2.setText(_translate("MainWindow", "Minimum size"))
        self.label_3.setText(_translate("MainWindow", "Maximum size"))
from PyQt5 import QtWebEngineWidgets
