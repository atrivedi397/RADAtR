from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon       # for importing icon
from PyQt5.QtCore import QSize      # for icon size


class LeftModulePanel:
    def __init__(self, base=None):

        # left most (vertical) toggle bar
        self.modulePanel = QWidget(base)
        self.modulePanel.setMaximumWidth(50)                # static value, need not to be changed

        # layout for left bar
        self.leftBarLayout = QVBoxLayout(self.modulePanel)

        """----------- buttons on the (left) Modules Panel --------------"""
        # for timeTable module
        self.timeTableButton = QPushButton('', self.modulePanel)
        self.timeTableButton.setIcon(QIcon('Icons/timetable.png'))
        self.timeTableButton.setIconSize(QSize(40, 40))

        # for scheduleExam module
        self.examScheduleButton = QPushButton('', self.modulePanel)
        self.examScheduleButton.setIcon(QIcon('Icons/timetable.png'))
        self.examScheduleButton.setIconSize(QSize(40, 40))

        # for Admission module
        self.admissionButton = QPushButton('', self.modulePanel)
        self.admissionButton.setIcon(QIcon('Icons/timetable.png'))
        self.admissionButton.setIconSize(QSize(40, 40))

        # for calender (home screen)
        self.calenderButton = QPushButton('', self.modulePanel)
        self.calenderButton.setIcon(QIcon('Icons/timetable.png'))
        self.calenderButton.setIconSize(QSize(40, 40))

        # for miscellaneous sub-modules
        self.unitSubModuleButton = QPushButton('', self.modulePanel)
        self.unitSubModuleButton.setIcon(QIcon('Icons/timetable.png'))
        self.unitSubModuleButton.setIconSize(QSize(40, 40))

        # stacking all buttons inside the (left-most) panel
        self.leftBarLayout.addStretch(5)
        self.leftBarLayout.addWidget(self.timeTableButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.examScheduleButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.admissionButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.unitSubModuleButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.calenderButton)
        self.leftBarLayout.addStretch(30)

        # margin order (left, top, right, bottom)
        self.leftBarLayout.setContentsMargins(1, 0, 1, 0)
        self.leftBarLayout.setSpacing(0)
        self.modulePanel.setLayout(self.leftBarLayout)
