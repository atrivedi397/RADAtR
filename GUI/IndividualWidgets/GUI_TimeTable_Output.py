import sys
from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import add_time_to
from Detached.Classes.TimeTable import *


class Timetable(QMainWindow):

    def __init__(self, parent=None, slots_list=None):
        super().__init__(parent)
        self.title = 'Time Table'
        self.days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.baseTime = '1000'
        self.slotDuration = '60'
        self.slots = []
        self.listOfSlots = slots_list

        # creating an object of 'TimeTable' class to generate time table
        self.time_table = TimeTable()

        self.setWindowTitle(self.title)
        self.setFixedSize(938, 480)

        # central Widget
        self.containerWidget = QWidget(self)
        self.containerWidget.setFixedSize(934, 476)

        # Add box layout
        self.layout = QVBoxLayout(self.containerWidget)
        self.tableWidget = QTableWidget(self.containerWidget)

        # rows creation and its properties
        self.tableWidget.setRowCount(totalWorkingDays)
        for row_no in range(totalWorkingDays):
            self.tableWidget.setRowHeight(row_no, 80)

        # columns creation and its properties
        self.tableWidget.setColumnCount(maximumSlots + 1)
        for column_no in range(maximumSlots + 1):
            if column_no == lunch_slot_no - 1:
                self.tableWidget.setColumnWidth(column_no, 50)
            else:
                self.tableWidget.setColumnWidth(column_no, 130)

        self.tableWidget.setVerticalHeaderLabels(self.days_list)
        self.get_next_slot(maximumSlots+1)
        self.tableWidget.setHorizontalHeaderLabels(self.slots)

        # creating buttons area
        self.buttons_layout = QHBoxLayout(self.containerWidget)

        # creating ('Next', 'Finalize' and 'Cancel') buttons
        next_button = QPushButton('Next')
        next_button.clicked.connect(lambda: self.assign_mappings())
        finalize_button = QPushButton('Finalize')
        cancel_button = QPushButton('Cancel')

        # adding buttons in a line (horizontally)
        self.buttons_layout.addStretch(2)  # creates empty space on the left side
        self.buttons_layout.addWidget(next_button)
        self.buttons_layout.addWidget(finalize_button)
        self.buttons_layout.addWidget(cancel_button)

        # add table to box layout and add box layout to widget
        self.layout.addWidget(self.tableWidget)
        self.layout.addLayout(self.buttons_layout)
        self.containerWidget.setLayout(self.layout)

    def get_next_slot(self, for_n_slots):
        for i in range(for_n_slots):
            # representation for 'Recess' Column
            if i == lunch_slot_no - 1:                      # as lunch_slot_no isn't index
                next_slot_time = add_time_to(self.baseTime, self.slotDuration)
                self.baseTime = next_slot_time
                self.slots.append('')
            else:
                # storing slot starting time
                start = self.baseTime

                # calculating end time for the current slot
                end = add_time_to(self.baseTime, self.slotDuration)
                self.baseTime = end

                # creating label for slots
                column_label = start + '-' + end
                self.slots.append(column_label)

    def assign_mappings(self):
        mapping_list = self.time_table.place(self.listOfSlots)
        print(type(mapping_list))


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    Objtimetable = Timetable()
    Objtimetable.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
