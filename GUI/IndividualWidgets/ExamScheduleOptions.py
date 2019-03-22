"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel.
    This file is not being used anywhere because of the unexpected error (class isn't accepting any arguments)"""
from PyQt5.QtWidgets import *


class ExamScheduleOptions(QWidget):
    def __int__(self, parent=None):
        super.__init__(parent)
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 4                               # this must be update if new options are added

        # layout
        self.examScheduleOptionsLayout = QVBoxLayout(self)

        # heading for Exam-Schedule List
        self.examScheduleHead = QLabel('Exam', self)

        # creating options list for exam-schedule module
        self.examScheduleList = QListWidget(self)

        # List items
        self.examScheduleList.insertItem(0, 'Schedule')
        self.examScheduleList.insertItem(1, 'View')
        self.examScheduleList.insertItem(3, 'Deletion')

        # stacking up all widgets in vertical layout
        self.examScheduleOptionsLayout.addWidget(self.examScheduleHead)
        self.examScheduleOptionsLayout.addWidget(self.examScheduleList)
        self.examScheduleOptionsLayout.setContentsMargins(0, 3, 0, 3)
