# ############  Sacred FIle ###################
# importing all widgets that are to be displayed as output
from GUI.IndividualWidgets.Template_WorkInProgress import *
from GUI.IndividualWidgets.GUI_Course_Add import *
from GUI.GUI_TimeTable_Create import *


class DynamicWidgets:
    def __init__(self, base=None):

        # Output-Widgets container
        self.OutputWidgetsContainer = QWidget(base)
        self.outputContainerLayout = QVBoxLayout(self.OutputWidgetsContainer)
        self.outputStack = QStackedWidget(self.OutputWidgetsContainer)

        """every widget of each module that has to be displayed must be defined here"""
        # time table module
        self.timeTableSubModule = TimeTableWindow(self.OutputWidgetsContainer)

        # miscellaneous category
        self.blankWidget = QWidget(self.OutputWidgetsContainer)
        self.calender = QCalendarWidget(self.OutputWidgetsContainer)
        self.template = WorkInProgress(self.OutputWidgetsContainer)
        self.addCourseWindow = AddCourse(self.OutputWidgetsContainer)

        # stacking up all the above widgets (indexes for following widgets start from 0)
        self.outputStack.addWidget(self.timeTableSubModule.createTimeTableWindow)
        self.outputStack.addWidget(self.blankWidget)
        self.outputStack.addWidget(self.calender)
        self.outputStack.addWidget(self.addCourseWindow)
        self.outputStack.addWidget(self.template.incompleteWorkTemplate)

        self.outputStack.setCurrentIndex(0)  # for testing purpose

        # adding outputStack to the layout of outputContainer
        self.outputContainerLayout.addWidget(self.outputStack)
