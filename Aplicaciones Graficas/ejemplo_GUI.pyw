import sys
from PyQt6 import uic, QtGui, QtCore
from PyQt6.QtWidgets import QMainWindow, QApplication

class ejemplo_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(350, 100, 300, 300)
        self.setWindowTitle('Primer Ejemplo de GUI con PyQt.')
        salir = QtGui.QPushButton('Salir', self)
        salir.setGeometry(100, 100, 100, 100)
        salir.clicked.connect(self.close)

app = QApplication(sys.argv)
mi_app = ejemplo_GUI()
mi_app.show()
sys.exit(app.exec_())

