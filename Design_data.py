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
        MainWindow.resize(1028, 606)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.random_data = QtWidgets.QPushButton(self.centralwidget)
        self.random_data.setGeometry(QtCore.QRect(60, 510, 191, 23))
        self.random_data.setObjectName("random_data")
        self.plots_view = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.plots_view.setGeometry(QtCore.QRect(60, 120, 911, 361))
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
        self.size_rate_user_files = QtWidgets.QPushButton(self.centralwidget)
        self.size_rate_user_files.setGeometry(QtCore.QRect(650, 20, 211, 23))
        self.size_rate_user_files.setObjectName("size_rate_user_files")
        self.files = QtWidgets.QSpinBox(self.centralwidget)
        self.files.setGeometry(QtCore.QRect(280, 510, 111, 22))
        self.files.setMinimum(1)
        self.files.setMaximum(500)
        self.files.setSingleStep(1)
        self.files.setObjectName("files")
        self.min_file_size = QtWidgets.QSpinBox(self.centralwidget)
        self.min_file_size.setGeometry(QtCore.QRect(420, 510, 101, 22))
        self.min_file_size.setMinimum(10000)
        self.min_file_size.setMaximum(1000000000)
        self.min_file_size.setSingleStep(10000)
        self.min_file_size.setObjectName("min_file_size")
        self.max_file_size = QtWidgets.QSpinBox(self.centralwidget)
        self.max_file_size.setGeometry(QtCore.QRect(550, 510, 91, 22))
        self.max_file_size.setMinimum(20000)
        self.max_file_size.setMaximum(2000000000)
        self.max_file_size.setSingleStep(10000)
        self.max_file_size.setObjectName("max_file_size")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 490, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 490, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 490, 71, 16))
        self.label_3.setObjectName("label_3")
        self.generate_progress = QtWidgets.QProgressBar(self.centralwidget)
        self.generate_progress.setGeometry(QtCore.QRect(670, 510, 201, 23))
        self.generate_progress.setProperty("value", 0)
        self.generate_progress.setObjectName("generate_progress")
        self.finished = QtWidgets.QLabel(self.centralwidget)
        self.finished.setGeometry(QtCore.QRect(880, 510, 131, 21))
        self.finished.setText("")
        self.finished.setScaledContents(True)
        self.finished.setObjectName("finished")
        self.com_time_file = QtWidgets.QPushButton(self.centralwidget)
        self.com_time_file.setGeometry(QtCore.QRect(70, 60, 171, 23))
        self.com_time_file.setObjectName("com_time_file")
        self.choose_file = QtWidgets.QComboBox(self.centralwidget)
        self.choose_file.setGeometry(QtCore.QRect(70, 90, 91, 22))
        self.choose_file.setMaxVisibleItems(30)
        self.choose_file.setObjectName("choose_file")
        self.choose_file.hide()
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(170, 90, 75, 23))
        self.ok.setObjectName("ok")
        self.ok.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 22))
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
        self.random_data.setText(_translate("MainWindow", "Generate random data"))
        self.compression_rate.setText(_translate("MainWindow", "Compression rate"))
        self.com_size_or_size.setText(_translate("MainWindow", "Compression size to orginal size"))
        self.com_time_orginal_size.setText(_translate("MainWindow", "Compression time to orginal size"))
        self.size_rate_user_files.setText(_translate("MainWindow", "Compression rate for not random data"))
        self.label.setText(_translate("MainWindow", "Files number"))
        self.label_2.setText(_translate("MainWindow", "Minimum size"))
        self.label_3.setText(_translate("MainWindow", "Maximum size"))
        self.com_time_file.setText(_translate("MainWindow", "Compression time of file"))
        self.ok.setText(_translate("MainWindow", "OK"))
from PyQt5 import QtWebEngineWidgets
