from random import choice, randint
from sys import argv, exit

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.setupUi()
        self.x = -1
        self.y = -1
        self.k = 0
        self.setMouseTracking(True)

    def setupUi(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))

        self.pushButton.clicked.connect(self.drw_ev)

    def drw_ev(self):
        self.x = randint(0, 500)
        self.y = randint(0, 500)
        self.label.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        qp.setBrush(QColor('Yellow'))
        a = randint(1, 100)
        qp.drawEllipse(self.x, self.y, a, a)

        qp.setBrush(QColor('white'))
        qp.drawEllipse(self.x + 2, self.y + 2, a - 4, a - 4)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
