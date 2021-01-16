import os
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import Design
from Burrows_Wheeler_transformation import burrows_wheeler_transformation
from Huffman import HuffNode
from Read_file import read_txt_file


class ExampleApp(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    file: str
    choosed: int
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_file.clicked.connect(self.get_file_f)
        self.com.clicked.connect(self.compress)
        self.huff.toggled.connect(self.com_type)
        self.huff_tr.toggled.connect(self.com_type)
        self.shan.toggled.connect(self.com_type)
        self.shan_tr.toggled.connect(self.com_type)
        self.lz78.toggled.connect(self.com_type)
        self.lzw.toggled.connect(self.com_type)

    def get_file_f(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Text files (*.txt)", options=options)
        name = os.path.basename(self.file)
        self.file_name.setText(name)

    def com_type(self):
        type = self.sender()
        if type.isChecked():
            if type.objectName() == 'huff': self.choosed = 1
            elif type.objectName() == 'huff_tr': self.choosed = 2
            elif type.objectName() == 'shan': self.choosed = 3
            elif type.objectName() == 'shan_tr': self.choosed = 4
            elif type.objectName() == 'lz78': self.choosed = 5
            elif type.objectName() == 'lzw': self.choosed = 6
            else: self.choosed = -1


    def compress(self):
        if (self.choosed ==  1):
            h = HuffNode()
            h.compress(self.file)

        elif(self.choosed == 2):
            text = read_txt_file(self.file)
            text1 = burrows_wheeler_transformation(text)
            print(text1)
            h = HuffNode()
            h.compress_from_text(text1, self.file)




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()