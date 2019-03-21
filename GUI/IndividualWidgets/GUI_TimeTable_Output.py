import sys
from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import add_time_to, last_name_only
from Detached.Classes.TimeTable import *


class TimeTableDisplayWindow(QMainWindow):

    def __init__(self, parent=None, slots_list=None, course=None, semester=None, batch_no='1', batch_timing=starting_time):
        super().__init__(parent)
        self.title = 'Time Table'
        self.course = course
        self.semester = semester
        self.session = '2018-2019'                      # static value for now, must be updated
        self.batchNo = batch_no
        self.baseTime = batch_timing
        self.slotDuration = '60'
        self.slots = []
        self.listOfSlots = slots_list
        self.timeTableGenerated = 0
        self.timeTableMaxGenerationLimit = 5

        # batch timing validations
        if self.baseTime == '':
            self.baseTime = str(starting_time)
        else:
            self.baseTime = str(batch_timing)

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
        self.infoRow = QHBoxLayout(self.containerWidget)
        self.tableWidget = QTableWidget(self.containerWidget)
        
        # first row layout which shows Course, Batch, Year and Semester info
        course_label = 'Course: ' + self.course
        self.course_info = QLabel(course_label)
        
        semester_label = 'Semester: ' + str(self.semester)
        self.semester_info = QLabel(semester_label)
        
        batch_label = 'Batch: ' + self.batchNo
        self.batch_info = QLabel(batch_label)
        
        session_label = 'Year: ' + self.session
        self.session_info = QLabel(session_label)

        # stacking up all of the above widget horizontally
        self.infoRow.addWidget(self.course_info)
        self.infoRow.addWidget(self.semester_info)
        self.infoRow.addWidget(self.batch_info)
        self.infoRow.addWidget(self.session_info)

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

        self.tableWidget.setVerticalHeaderLabels(days_list)
        self.get_next_slot(maximumSlots+1)
        self.tableWidget.setHorizontalHeaderLabels(self.slots)

        # creating buttons area
        self.buttons_layout = QHBoxLayout(self.containerWidget)

        # creating ('Print', 'Previous', 'Next', 'Finalize' and 'Cancel') buttons
        print_button = QPushButton('Print')
        previous_button = QPushButton('Previous')
        previous_button.clicked.connect(self.show_previous_time_table)
        self.next_button = QPushButton('Next')
        self.next_button.clicked.connect(lambda: self.assign_mappings())
        finalize_button = QPushButton('Finalize')
        finalize_button.clicked.connect(self.finalize_time_table)
        cancel_button = QPushButton('Cancel')

        # adding buttons in a line (horizontally)
        self.buttons_layout.addStretch()  # creates empty space on the left side
        self.buttons_layout.addWidget(print_button)
        self.buttons_layout.addWidget(previous_button)
        self.buttons_layout.addWidget(self.next_button)
        self.buttons_layout.addWidget(finalize_button)
        self.buttons_layout.addWidget(cancel_button)

        # adding table widget and 'info_row' layout to box layout and add box layout to widget
        self.layout.addLayout(self.infoRow)
        self.layout.addWidget(self.tableWidget)
        self.layout.addLayout(self.buttons_layout)
        self.containerWidget.setLayout(self.layout)
        self.assign_mappings()

    # function which gets time-duration
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
                column_label = start[0:2] + ':' + start[2:4] + '-' + end[0:2] + ':' + end[2:4]
                self.slots.append(column_label)

    # function to assign 'Subject-teacher' mapping to each slot of each week.
    def assign_mappings(self):
        if self.timeTableGenerated < self.timeTableMaxGenerationLimit:
            mapping_list = self.time_table.place(self.listOfSlots)

            day_number = 0
            lunch = 'LUNCH'

            # plotting lectures in different slots
            for day in mapping_list:
                slot_number = 0
                for lecture in day:
                    for teacher, subject in lecture.items():
                        # putting a single letter of 'LUNCH' in each day for lunch slot.
                        if slot_number == lunch_slot_no - 1:
                            self.tableWidget.setItem(day_number, slot_number, QTableWidgetItem(lunch[day_number]))
                            slot_number += 1
                        # putting a subject lecture
                        else:
                            # no labels for the slots for which no teachers are available
                            # (dictionary value is {'not': '-' }
                            if teacher == 'not':
                                slot_label = ''
                                slot_number += 1
                            else:
                                slot_label = subject[0] + '\n' + teacher
                                trimmed_label = self.trim_label(slot_label, 2)

                                # shortening teacher's name
                                trimmed_label = trimmed_label + '\n' + last_name_only(teacher)

                                self.tableWidget.setItem(day_number, slot_number, QTableWidgetItem(trimmed_label))
                                slot_number += 1
                day_number += 1
            self.timeTableGenerated += 1
        else:
            self.next_button.setEnabled(False)

    # function to display previously generated time table templates
    def show_previous_time_table(self):
        pass

    # function that is to be performed on clicking 'Finalize' button
    def finalize_time_table(self):
        self.time_table.store_time_table_in_db()
        """it must close itself and return a value to the 'TimeTableOutputWindow file.
            This returned value will trigger closing function resulting in home screen display"""

    # function to trim down lecture label if it is too long
    def trim_label(self, original_label, words_limit):
        word_count = 0
        invalid_word_count = 0
        words_in_label = original_label.split()             # finding the total number of words in whole label string

        # counting the (appropriate) words
        invalid_name_words = ['of', 'in', 'and', 'the', '&', 'based', 'on', 'at']
        for word in words_in_label:
            for invalid_word in invalid_name_words:
                if word == invalid_word:
                    invalid_word_count += 1
                else:
                    word_count += 1

        if word_count > words_limit:
            # shortened list of words
            name_list = words_in_label[0: words_limit + invalid_word_count]

            # removing any invalid word which comes at the end
            for invalid_word in invalid_name_words:
                if name_list[-1] == invalid_word:                   # if last word is invalid word
                    invalid_word_count -= 1
                    break

            # joining the words together to form a string/label
            short_label = ' '.join(words_in_label[0: words_limit + invalid_word_count])
            return short_label


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    Objtimetable = TimeTableDisplayWindow()
    Objtimetable.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
