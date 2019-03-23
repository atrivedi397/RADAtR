"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel."""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget)


class TimeTableOptions:
    def __init__(self, base=None, function=None, initial_index=0):
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 4  # this must be update if new options are added
        self.preOccupiedIndexes = initial_index
        print('Pre occupied index: ', self.preOccupiedIndexes)
        self.functionReference = function

        # creating a widget to contain a list of options related to time table
        self.timeTableOptionsWidget = QWidget(base)
        self.timeTableOptionsLayout = QVBoxLayout(self.timeTableOptionsWidget)

        # heading for Time-Table List
        self.timeTableHead = QLabel('Time Table:', self.timeTableOptionsWidget)

        # creating options list for time table module
        self.timeTableList = QListWidget(self.timeTableOptionsWidget)

        # List items
        self.timeTableList.insertItem(0, 'Creation')
        self.timeTableList.insertItem(1, 'Viewing')
        self.timeTableList.insertItem(2, 'Editing')
        self.timeTableList.insertItem(3, 'Deletion')
        self.timeTableList.currentRowChanged.connect(self.timetable_option_changed)

        # stacking up all widgets in vertical layout
        self.timeTableOptionsLayout.addWidget(self.timeTableHead)
        self.timeTableOptionsLayout.addWidget(self.timeTableList)
        self.timeTableOptionsLayout.setContentsMargins(0, 3, 0, 3)

    """-------------------------------- Function Definitions ------------------------------"""
    def timetable_option_changed(self, changed_to_index):
        self.functionReference(self.preOccupiedIndexes + changed_to_index)
