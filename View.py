import os
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
import Design
from All_statistic_coding_decompression import Statistic_coding_decompression
from Burrows_Wheeler_transformation import burrows_wheeler_transformation
from Huffman import HuffNode
from Lempel_Ziv_Welch import LZW
from Read_file import read_txt_file
from Shannon import Shannon
from Lempel_Ziv import LZ_78


class Runnable(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Runnable, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        self.fn(*self.args, **self.kwargs)


class ExampleApp(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    file: str
    choosed: int

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_file.clicked.connect(self.get_file_f)
        self.com.clicked.connect(self.compress)
        self.decom.clicked.connect(self.decompress)
        self.huff.toggled.connect(self.com_type)
        self.huff_tr.toggled.connect(self.com_type)
        self.shan.toggled.connect(self.com_type)
        self.shan_tr.toggled.connect(self.com_type)
        self.lz78.toggled.connect(self.com_type)
        self.lzw.toggled.connect(self.com_type)

        self.threadpool = QThreadPool()

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
            if type.objectName() == 'huff':
                self.choosed = 1
            elif type.objectName() == 'huff_tr':
                self.choosed = 2
            elif type.objectName() == 'shan':
                self.choosed = 3
            elif type.objectName() == 'shan_tr':
                self.choosed = 4
            elif type.objectName() == 'lz78':
                self.choosed = 5
            elif type.objectName() == 'lzw':
                self.choosed = 6
            else:
                self.choosed = -1

    def huff_com(self):
        self.info.setText('Compressing...')
        h = HuffNode()
        h.compress(self.file)
        self.info.setText('Compression done')

    def huff_dcom(self):
        self.info.setText('Decompressing...')
        h = Statistic_coding_decompression()
        h.decompression(self.file, 'huff')
        self.info.setText('Dempression done')

    def shan_com(self):
        self.info.setText('Compressing...')
        s = Shannon(self.file)
        s.compress()
        self.info.setText('Compression done')

    def shan_dcom(self):
        self.info.setText('Decompressing...')
        s = Statistic_coding_decompression()
        s.decompression(self.file, 'shan')
        self.info.setText('Dempression done')

    def lz78_com(self):
        self.info.setText('Compressing...')
        lz78 = LZ_78(256)
        lz78.compress(self.file)
        self.info.setText('Compression done')

    def lz78_dcom(self):
        self.info.setText('Decompressing...')
        lz78 = LZ_78(256)
        lz78.decompress(self.file)
        self.info.setText('Dempression done')

    def lzw_com(self):
        self.info.setText('Compressing...')
        lzw = LZW(self.file)
        lzw.compress()
        self.info.setText('Compression done')

    def lzw_dcom(self):
        self.info.setText('Decompressing...')
        lzw = LZW()
        lzw.decompress(self.file)
        self.info.setText('Dempression done')

    def compress(self):
        if self.choosed == 1:
            runnable = Runnable(self.huff_com)
            self.threadpool.start(runnable)

        elif self.choosed == 2:
            text = read_txt_file(self.file)
            text1 = burrows_wheeler_transformation(text)
            h = HuffNode()
            h.compress_from_text(text1, self.file)

        elif self.choosed == 3:
            runnable = Runnable(self.shan_com)
            self.threadpool.start(runnable)

        elif self.choosed == 5:
            runnable = Runnable(self.lz78_com)
            self.threadpool.start(runnable)

        elif self.choosed == 6:
            runnable = Runnable(self.lzw_com)
            self.threadpool.start(runnable)

    def decompress(self):
        if self.choosed == 1:
            runnable = Runnable(self.huff_dcom)
            self.threadpool.start(runnable)

        # elif self.choosed == 2:
        #     text = read_txt_file(self.file)
        #     text1 = burrows_wheeler_transformation(text)
        #     h = HuffNode()
        #     h.compress_from_text(text1, self.file)
        #
        elif self.choosed == 3:
            runnable = Runnable(self.shan_dcom)
            self.threadpool.start(runnable)

        elif self.choosed == 5:
            runnable = Runnable(self.lz78_dcom)
            self.threadpool.start(runnable)

        elif self.choosed == 6:
            runnable = Runnable(self.lzw_dcom)
            self.threadpool.start(runnable)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
