import sqlite3
import sys

from PyQt6 import uic, QtWidgets


class AddWidget(QtWidgets.QWidget):
    def __init__(self, core):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.core = core
        self.setWindowTitle("~ /Add coffee")

        self.applyBtn.clicked.connect(self.apply)

    def apply(self):
        if (len((name := self.name.text())) > 0 and len((roast := self.roast.text())) > 0 and len(
                (type := self.type.text())) > 0 and len((taste := self.taste.text())) > 0 and len(
            (cost := self.cost.text())) > 0 and len((value := self.value.text())) > 0):
            self.core.add_coffee(name, roast, type, taste, cost, value)
            self.destroy()


class EditWidget(QtWidgets.QWidget):
    def __init__(self, values, core):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
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


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.base = sqlite3.connect("coffee.db")
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
