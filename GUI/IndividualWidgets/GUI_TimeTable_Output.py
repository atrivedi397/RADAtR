import sys
from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import add_time_to
from Detached.Classes.TimeTable import *
from testFile1 import test_list


class TimeTableDisplayWindow(QMainWindow):

    def __init__(self, parent=None, slots_list=None, course=None, semester=None, batch_no='1', batch_timing=starting_time):
        super().__init__(parent)
        self.title = 'Time Table'
        self.course = course
        self.semester = semester
        self.days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.batchNo = batch_no
        self.baseTime = starting_time
        self.slotDuration = '60'
        self.slots = []
        self.listOfSlots = slots_list
        self.timeTableGenerated = 0

        # batch timing validations
        if self.baseTime == '':
            self.baseTime = str(starting_time)
        else:
            self.baseTime = batch_timing

        # batch number validation
        if self.batchNo == '':
            self.batchNo = '1'
        else:
            self.batchNo = batch_no

        # creating an object of 'TimeTable' class to generate time table
        self.time_table = TimeTable(self.course, self.semester, self.batchNo, self.baseTime)

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
        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(lambda: self.assign_mappings())
        finalize_button = QPushButton('Finalize')
        finalize_button.clicked.connect(self.finalize_time_table)
        cancel_button = QPushButton('Cancel')

        # adding buttons in a line (horizontally)
        self.buttons_layout.addStretch(2)  # creates empty space on the left side
        self.buttons_layout.addWidget(self.next_button)
        self.buttons_layout.addWidget(finalize_button)
        self.buttons_layout.addWidget(cancel_button)

        # add table to box layout and add box layout to widget
        self.layout.addWidget(self.tableWidget)
        self.layout.addLayout(self.buttons_layout)
        self.containerWidget.setLayout(self.layout)
        self.assign_mappings()

    def get_next_slot(self, for_n_slots):
        for i in range(for_n_slots):
            # representation for 'Recess' Column
            if i == lunch_slot_no - 1:                      # as lunch_slot_no isn't index
                next_slot_time = add_time_to(self.baseTime, self.slotDuration)
                self.baseTime = next_slot_time
                self.slots.append('')                       # print no label for lunch slots
            else:
                # storing slot starting time
                start = self.baseTime
                start = str(start)

                # batch timing validations
                if start == '':
                    start = str(starting_time)

                # calculating end time for the current slot
                end = add_time_to(start, self.slotDuration)
                self.baseTime = end

                # creating label for slots
                column_label = start + '-' + end
                self.slots.append(column_label)

    def assign_mappings(self):
        if self.timeTableGenerated < 5 - 1:
            mapping_list = self.time_table.place(self.listOfSlots)

            day_number = 0
            lunch = 'LUNCH'

            # plotting lectures in different slots
            for day in mapping_list:
                slot_number = 0
                for lecture in day:
                    for teacher, subject in lecture.items():
                        if slot_number == lunch_slot_no - 1:
                            self.tableWidget.setItem(day_number, slot_number, QTableWidgetItem(lunch[day_number]))
                            slot_number += 1
                        else:
                            slot_label = subject[0] + '\n' + teacher
                            self.tableWidget.setItem(day_number, slot_number, QTableWidgetItem(slot_label))
                            slot_number += 1
                day_number += 1
            self.timeTableGenerated += 1
        else:
            self.next_button.setEnabled(False)

    # function that is to be performed on clicking 'Finalize' button
    def finalize_time_table(self):
        self.time_table.store_time_table_in_db()


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    Objtimetable = TimeTableDisplayWindow()
    Objtimetable.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
