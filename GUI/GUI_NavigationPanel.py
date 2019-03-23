""" This file contains list of sub-module-list """
from GUI.IndividualWidgets.ExamScheduleOptions import *
from GUI.IndividualWidgets.TimeTableOptions import *
from GUI.IndividualWidgets.MiscellaneousOptions import *
from PyQt5.QtWidgets import QStackedWidget


class NavigationPanel:
    def __init__(self, base=None, function=None):
        # this reference points to the 'change_window' function of 'OutputWidgetsContainer.py'
        self.functionReference = function
        self.indexOccupied = 0

        # navigation panel
        self.navPanel = QWidget(base)
        self.navPanel.setHidden(True)
        self.navPanel.setFixedWidth(175)

        # navigation panel layout
        self.navLayout = QVBoxLayout(self.navPanel)

        # navigation panel (widgets) stack list
        self.submoduleStack = QStackedWidget(self.navPanel)

        """------------ Adding sub module options in above stack -------------"""
        self.testTimeTable = TimeTableOptions(self.navPanel, self.functionReference, self.indexOccupied)
        self.indexOccupied += self.testTimeTable.totalOptions
        self.examScheduleSubModule = ExamScheduleOptions(self.navPanel)

        # stacking (TimeTableOption and ExamScheduleSubModule)
        self.submoduleStack.addWidget(self.testTimeTable.timeTableOptionsWidget)
        self.submoduleStack.addWidget(self.examScheduleSubModule.examScheduleOptions)

        self.navLayout.addWidget(self.submoduleStack)
        self.navLayout.setContentsMargins(0, 3, 0, 3)
        self.navLayout.setSpacing(1)

