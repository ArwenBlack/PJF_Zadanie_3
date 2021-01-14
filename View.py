import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.button_for_file = QPushButton("Get_file")
        self.contents = QTextEdit()
        self.title = "Kompresja"
        self.initUI()
        self.setFixedHeight(600)
        self.setFixedWidth(1000)

    def initUI(self):
        self.setWindowTitle(self.title)

        vlayout = QVBoxLayout(self)
        hlayout = QHBoxLayout(self)
        hlayout.addWidget(self.button_for_file)
        hlayout.addWidget(self.contents)
        vlayout.addLayout(hlayout)

        self.button_for_file.clicked.connect(self.get_file)

    def get_file(self):
        print()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Text files (*.txt)", options=options)
        f = open(fileName, 'r')
        with f:
            data = f.read()
            self.contents.setText(data)




app = QApplication(sys.argv)
view = App()
view.show()
app.exec_()
