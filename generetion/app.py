import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.exemple)
    def exemple(self):
        print(1)   
app =QApplication([])     
ex = Widget()
ex.show()
app.exec_()