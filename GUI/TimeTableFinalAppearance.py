import sys
from PyQt5.QtWidgets import *
from Detached.Global.Variables.varFile1 import *


class Timetable(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Time Table'
        self.MainWindowProp()

    def MainWindowProp(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 300, 800, 300)

        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(totalWorkingDays)
        self.tableWidget.setColumnCount(maximumSlots)
        self.tableWidget.move(0, 0)
        self.tableWidget.setVerticalHeaderLabels(days_list)
        self.tableWidget.setHorizontalHeaderLabels(time_slot)

        self.tableWidget.setItem(0, 0, QTableWidgetItem(i))
        self.tableWidget.setItem(0, 1, QTableWidgetItem())
        self.tableWidget.setItem(0, 2, QTableWidgetItem())


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    Objtimetable = Timetable()
    Objtimetable.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
