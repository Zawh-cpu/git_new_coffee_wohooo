import sqlite3
import sys

from PyQt6 import QtWidgets, QtCore


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 170)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 47, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 47, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 47, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 47, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 47, 20))
        self.label_6.setObjectName("label_6")
        self.applyBtn = QtWidgets.QPushButton(Form)
        self.applyBtn.setGeometry(QtCore.QRect(10, 140, 380, 23))
        self.applyBtn.setObjectName("applyBtn")
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(60, 10, 321, 20))
        self.name.setObjectName("name")
        self.roast = QtWidgets.QLineEdit(Form)
        self.roast.setGeometry(QtCore.QRect(60, 30, 321, 20))
        self.roast.setObjectName("roast")
        self.type = QtWidgets.QLineEdit(Form)
        self.type.setGeometry(QtCore.QRect(60, 50, 321, 20))
        self.type.setObjectName("type")
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setGeometry(QtCore.QRect(60, 70, 321, 20))
        self.taste.setObjectName("taste")
        self.cost = QtWidgets.QLineEdit(Form)
        self.cost.setGeometry(QtCore.QRect(60, 90, 321, 20))
        self.cost.setObjectName("cost")
        self.value = QtWidgets.QLineEdit(Form)
        self.value.setGeometry(QtCore.QRect(60, 110, 321, 20))
        self.value.setObjectName("value")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "roast"))
        self.label_3.setText(_translate("Form", "type"))
        self.label_4.setText(_translate("Form", "taste"))
        self.label_5.setText(_translate("Form", "cost"))
        self.label_6.setText(_translate("Form", "value"))
        self.applyBtn.setText(_translate("Form", "APPLY"))


class AddWidget(Ui_Form, QtWidgets.QWidget):
    def __init__(self, core):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.core = core
        self.setWindowTitle("~ /Add coffee")

        self.applyBtn.clicked.connect(self.apply)

    def apply(self):
        if (len((name := self.name.text())) > 0 and len((roast := self.roast.text())) > 0 and len(
                (type := self.type.text())) > 0 and len((taste := self.taste.text())) > 0 and len(
            (cost := self.cost.text())) > 0 and len((value := self.value.text())) > 0):
            self.core.add_coffee(name, roast, type, taste, cost, value)
            self.destroy()


class EditWidget(Ui_Form, QtWidgets.QWidget):
    def __init__(self, values, core):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.core = core
        self.id = values[0]
        self.setWindowTitle(f"~ /Edit coffee --id {self.id}")

        self.name.setText(values[1])
        self.roast.setText(values[2])
        self.type.setText(values[3])
        self.taste.setText(values[4])
        self.cost.setText(values[5])
        self.value.setText(values[6])

        self.applyBtn.clicked.connect(self.apply)

    def apply(self):
        if (len((name := self.name.text())) > 0 and len((roast := self.roast.text())) > 0 and len(
                (type := self.type.text())) > 0 and len((taste := self.taste.text())) > 0 and len(
            (cost := self.cost.text())) > 0 and len((value := self.value.text())) > 0):
            self.core.edit_coffee(self.id, name, roast, type, taste, cost, value)
            self.destroy()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(0, 20, 600, 380))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 50, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 0, 70, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 0, 70, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ADD"))
        self.pushButton_2.setText(_translate("MainWindow", "CHANGE"))
        self.pushButton_3.setText(_translate("MainWindow", "DELETE"))


class MyWidget(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.base = sqlite3.connect("data/coffee.db")
        self.crsr = self.base.cursor()

        self.search()
        self.pushButton.clicked.connect(self.open_add_widget)
        self.pushButton_2.clicked.connect(self.open_edit_widget)
        self.pushButton_3.clicked.connect(self.delete_coffee)

    def add_coffee(self, name, roast, type, taste, cost, value):
        self.crsr.execute(
            f"INSERT INTO coffee ('name', 'roast', 'type', 'taste', 'cost', 'value') VALUES ('{name}', '{roast}', '{type}', '{taste}', '{cost}', '{value}')")
        self.base.commit()
        self.search()

    def edit_coffee(self, id, name, roast, type, taste, cost, value):
        self.crsr.execute(
            f"UPDATE coffee SET name = '{name}', roast = '{roast}', type = '{type}', taste = '{taste}', cost = '{cost}', value = '{value}' WHERE id LIKE {id}")
        self.base.commit()
        self.search()

    def delete_coffee(self):
        if len(self.table.selectedItems()) > 0:
            self.table.selectRow(self.table.selectedItems()[0].row())
            id = self.table.selectedItems()[0].text()

            self.crsr.execute(f"DELETE FROM coffee WHERE id LIKE {id}")
            self.base.commit()
            self.search()

    def open_add_widget(self):
        self.adwidget = AddWidget(self)
        self.adwidget.show()

    def open_edit_widget(self):
        if len(self.table.selectedItems()) > 0:
            self.table.selectRow(self.table.selectedItems()[0].row())
            self.edwidget = EditWidget([_.text() for _ in self.table.selectedItems()], self)
            self.edwidget.show()

    def search(self):
        res = self.crsr.execute(f"SELECT * FROM coffee").fetchall()
        if len(res) > 0:
            self.table.setColumnCount(len(res[0]))
            self.table.setRowCount(len(res))

            for _ in range(len(res)):
                for _2 in range(len(res[0])):
                    self.table.setItem(_, _2, QtWidgets.QTableWidgetItem(str(res[_][_2])))

    def update(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
