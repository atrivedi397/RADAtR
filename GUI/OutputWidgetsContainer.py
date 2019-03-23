# ############  Sacred FIle ###################
# importing all widgets that are to be displayed as output
from GUI.IndividualWidgets.Template_WorkInProgress import *
from GUI.IndividualWidgets.GUI_Course_Add import *
from GUI.GUI_TimeTable_Create import *
from GUI.IndividualWidgets.TimeTable_View import *
from GUI.IndividualWidgets.TimeTable_Edit import *
from GUI.IndividualWidgets.TimeTable_Remove import *


class DynamicWidgets:
    def __init__(self, base=None):

        # Output-Widgets container
        self.OutputWidgetsContainer = QWidget(base)
        self.outputContainerLayout = QVBoxLayout(self.OutputWidgetsContainer)
        self.outputStack = QStackedWidget(self.OutputWidgetsContainer)

        """every widget of each module that has to be displayed must be defined here"""
        # time table category widgets declarations
        self.timeTableCreate = TimeTableWindow(self.OutputWidgetsContainer)
        self.timeTableView = ViewTimeTable(self.OutputWidgetsContainer)
        self.timeTableEdit = EditTimeTable(self.OutputWidgetsContainer)
        self.timeTableRemove = RemoveTimeTable(self.OutputWidgetsContainer)

        # miscellaneous category widgets declarations
        self.blankWidget = QWidget(self.OutputWidgetsContainer)
        self.calender = QCalendarWidget(self.OutputWidgetsContainer)
        self.template = WorkInProgress(self.OutputWidgetsContainer)
        self.addCourseWindow = AddCourse(self.OutputWidgetsContainer)

        """ stacking up all the above widgets (indexes for following widgets start from 0) """
        # stacking time table options widget
        self.outputStack.addWidget(self.timeTableCreate.createTimeTableWindow)
        self.outputStack.addWidget(self.timeTableView.timeTableViewWidget)
        self.outputStack.addWidget(self.timeTableEdit.timeTableEditWidget)
        self.outputStack.addWidget(self.timeTableRemove.timeTableRemoveWidget)

        # stacking calender (main module itself, with no sub-modules)
        self.outputStack.addWidget(self.calender)

        # stacking miscellaneous options widget
        self.outputStack.addWidget(self.addCourseWindow)

        # stacking independent widgets
        self.outputStack.addWidget(self.template.incompleteWorkTemplate)
        self.outputStack.addWidget(self.blankWidget)

        # adding outputStack to the layout of outputContainer
        self.outputContainerLayout.addWidget(self.outputStack)
        
    """------------------------------------- Function Definitions ----------------------------------"""
    # following function is called by another widget ( ) located elsewhere
    def change_window(self, window_index):
        self.outputStack.setCurrentIndex(window_index)
