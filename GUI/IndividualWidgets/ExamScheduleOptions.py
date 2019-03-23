"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel."""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget)


class ExamScheduleOptions:
    def __init__(self, base=None, function=None, index_used=0):
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 3  # this must be update if new options are added
        self.preOccupiedIndexes = index_used
        self.functionReference = function

        # creation of the widget
        self.examScheduleOptions = QWidget(base)
        self.examScheduleOptionsLayout = QVBoxLayout(self.examScheduleOptions)

        # heading for Exam-Schedule List
        self.examScheduleHead = QLabel('Exam Schedule', self.examScheduleOptions)

        # creating options list for exam-schedule module
        self.examScheduleList = QListWidget(self.examScheduleOptions)

        # List items
        self.examScheduleList.insertItem(0, 'Creation')
        self.examScheduleList.insertItem(1, 'View')
        self.examScheduleList.insertItem(2, 'Deletion')
        self.examScheduleList.currentRowChanged.connect(self.exam_schedule_option_changed)

        # stacking up all widgets in vertical layout
        self.examScheduleOptionsLayout.addWidget(self.examScheduleHead)
        self.examScheduleOptionsLayout.addWidget(self.examScheduleList)
        self.examScheduleOptionsLayout.setContentsMargins(0, 3, 0, 3)

    """-------------------------------- Function Definitions ------------------------------"""
    def exam_schedule_option_changed(self, changed_to_index):
        self.functionReference(self.preOccupiedIndexes + changed_to_index)
