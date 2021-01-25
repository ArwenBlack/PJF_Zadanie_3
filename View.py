import os
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool, pyqtSlot
import Design
import View_data
from All_statistic_coding_decompression import Statistic_coding_decompression
from DataBase import *
from Huffman import HuffNode
from Lempel_Ziv_Welch import LZW
from Lib_com_decom import *
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


class Main_window(QtWidgets.QMainWindow, Design.Ui_MainWindow):
    file: str
    choosed: int
    params: []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_file.clicked.connect(self.get_file_f)
        self.com.clicked.connect(self.compress)
        self.decom.clicked.connect(self.decompress)
        self.zlib.clicked.connect(self.com_type)
        self.gzib.clicked.connect(self.com_type)
        self.bz2.clicked.connect(self.com_type)
        self.lzma.clicked.connect(self.com_type)
        self.huff.toggled.connect(self.com_type)
        self.shan.toggled.connect(self.com_type)
        self.lz78.toggled.connect(self.com_type)
        self.lzw.toggled.connect(self.com_type)
        self.data_analyze.clicked.connect(self.data)

        self.threadpool = QThreadPool()

    def data(self):
        self.w = View_data.Main_window()
        self.w.show()

    def get_file_f(self):
        options = QFileDialog.Options()
        self.file, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                   "All Files (*);;Text files (*.txt)", options=options)
        name = os.path.basename(self.file)
        self.file_name.setText(name)

    def com_type(self):
        type = self.sender()
        if type.isChecked():
            if type.objectName() == 'zlib':
                self.choosed = 1
            elif type.objectName() == 'gzib':
                self.choosed = 2
            elif type.objectName() == 'bz2':
                self.choosed = 3
            elif type.objectName() == 'lzma':
                self.choosed = 4
            elif type.objectName() == 'huff':
                self.choosed = 5
            elif type.objectName() == 'shan':
                self.choosed = 6
            elif type.objectName() == 'lz78':
                self.choosed = 7
            elif type.objectName() == 'lzw':
                self.choosed = 8
            else:
                self.choosed = -1

    def zlib_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        f = zlib_best_com(self.file)
        end = time.time()
        self.params[0] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[0] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def zlib_decom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        zlib_best_com(self.file)
        end = time.time()
        f_time = end - start
        self.params[0] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Deompression done')

    def gzib_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        f = gzip_com(self.file)
        end = time.time()
        self.params[1] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[1] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def gzib_decom(self):
        self.info.setText('Deompressing...')
        start = time.time()
        gzip_decom(self.file)
        end = time.time()
        f_time = end - start
        self.params[1] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Decompression done')

    def bz2_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        f = bz2_com(self.file)
        end = time.time()
        self.params[2] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[2] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def bz2_decom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        bz2_decom(self.file)
        end = time.time()
        f_time = end - start
        self.params[2] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Decompression done')

    def lzma_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        f = lzma_com(self.file)
        end = time.time()
        self.params[3] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[3] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def lzma_decom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        lzma_decom(self.file)
        end = time.time()
        f_time = end - start
        self.params[3] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Decompression done')

    def huff_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        h = HuffNode()
        f = h.compress(self.file)
        end = time.time()
        self.params[4] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[4] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def huff_dcom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        h = Statistic_coding_decompression()
        h.decompression(self.file, 'huff')
        end = time.time()
        f_time = end - start
        self.params[4] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Dempression done')

    def shan_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        s = Shannon(self.file)
        f = s.compress()
        end = time.time()
        self.params[5] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[5] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def shan_dcom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        s = Statistic_coding_decompression()
        s.decompression(self.file, 'shan')
        end = time.time()
        f_time = end - start
        self.params[5] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Dempression done')

    def lz78_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        lz78 = LZ_78(256)
        f = lz78.compress(self.file)
        end = time.time()
        self.params[6] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[6] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def lz78_dcom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        lz78 = LZ_78(256)
        lz78.decompress(self.file)
        end = time.time()
        f_time = end - start
        self.params[6] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Dempression done')

    def lzw_com(self):
        self.info.setText('Compressing...')
        start = time.time()
        lzw = LZW(self.file)
        f = lzw.compress()
        end = time.time()
        self.params[7] = os.path.getsize(f)
        insert_size(os.path.basename(self.file), *self.params)
        f_time = end - start
        self.params[7] = f_time
        insert_time(1, os.path.basename(self.file), *self.params)
        self.info.setText('Compression done')

    def lzw_dcom(self):
        self.info.setText('Decompressing...')
        start = time.time()
        lzw = LZW()
        lzw.decompress(self.file)
        end = time.time()
        f_time = end - start
        self.params[7] = f_time
        insert_time(0, os.path.basename(self.file), *self.params)
        self.info.setText('Dempression done')

    def compress(self):
        size = os.path.getsize(self.file)
        insert(os.path.basename(self.file), size)
        self.params = [None for i in range(8)]
        if self.choosed == 1:
            runnable = Runnable(self.zlib_com)
            self.threadpool.start(runnable)

        if self.choosed == 2:
            runnable = Runnable(self.gzib_com)
            self.threadpool.start(runnable)

        if self.choosed == 3:
            runnable = Runnable(self.bz2_com)
            self.threadpool.start(runnable)

        if self.choosed == 4:
            runnable = Runnable(self.lzma_com)
            self.threadpool.start(runnable)

        if self.choosed == 5:
            runnable = Runnable(self.huff_com)
            self.threadpool.start(runnable)


        elif self.choosed == 6:
            runnable = Runnable(self.shan_com)
            self.threadpool.start(runnable)



        elif self.choosed == 7:
            runnable = Runnable(self.lz78_com)
            self.threadpool.start(runnable)

        elif self.choosed == 8:
            runnable = Runnable(self.lzw_com)
            self.threadpool.start(runnable)

    def decompress(self):
        self.params = [None for i in range(8)]
        if self.choosed == 1:
            runnable = Runnable(self.zlib_decom())
            self.threadpool.start(runnable)
        elif self.choosed == 2:
            runnable = Runnable(self.gzib_decom())
            self.threadpool.start(runnable)
        elif self.choosed == 3:
            runnable = Runnable(self.bz2_decom())
            self.threadpool.start(runnable)
        elif self.choosed == 4:
            runnable = Runnable(self.lzma_decom())
            self.threadpool.start(runnable)
        elif self.choosed == 5:
            runnable = Runnable(self.huff_dcom)
            self.threadpool.start(runnable)

        elif self.choosed == 6:
            runnable = Runnable(self.shan_dcom)
            self.threadpool.start(runnable)

        elif self.choosed == 7:
            runnable = Runnable(self.lz78_dcom)
            self.threadpool.start(runnable)

        elif self.choosed == 8:
            runnable = Runnable(self.lzw_dcom)
            self.threadpool.start(runnable)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main_window()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
