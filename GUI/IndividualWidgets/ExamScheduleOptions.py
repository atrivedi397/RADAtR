"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel."""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget)


class ExamScheduleOptions:
    def __init__(self, base=None):
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 4  # this must be update if new options are added

        # creation of the widget
        self.examScheduleOptions = QWidget(base)
        self.examScheduleOptionsLayout = QVBoxLayout(self.examScheduleOptions)

        # heading for Exam-Schedule List
        self.examScheduleHead = QLabel('Exam', self.examScheduleOptions)

        # creating options list for exam-schedule module
        self.examScheduleList = QListWidget(self.examScheduleOptions)

        # List items
        self.examScheduleList.insertItem(0, 'Schedule')
        self.examScheduleList.insertItem(1, 'View')
        self.examScheduleList.insertItem(3, 'Deletion')

        # stacking up all widgets in vertical layout
        self.examScheduleOptionsLayout.addWidget(self.examScheduleHead)
        self.examScheduleOptionsLayout.addWidget(self.examScheduleList)
        self.examScheduleOptionsLayout.setContentsMargins(0, 3, 0, 3)
