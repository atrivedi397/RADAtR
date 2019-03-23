# ############  Sacred FIle ###################
# importing all widgets that are to be displayed as output
from GUI.IndividualWidgets.Template_WorkInProgress import *
from GUI.IndividualWidgets.GUI_Course_Add import *
from GUI.GUI_TimeTable_Create import *
from GUI.IndividualWidgets.TimeTable_View import ViewTimeTable
from GUI.IndividualWidgets.TimeTable_Edit import EditTimeTable
from GUI.IndividualWidgets.TimeTable_Remove import RemoveTimeTable
from GUI.IndividualWidgets.ExamSchedule_Create import CreateExamSchedule
from GUI.IndividualWidgets.ExamSchedule_View import ViewExamSchedule
from GUI.IndividualWidgets.ExamSchedule_Delete import DeleteExamSchedule
from GUI.IndividualWidgets.Misc_AddSubject import AddSubjects
from GUI.IndividualWidgets.GUI_Teacher_Add import AddTeacher


class DynamicWidgets:
    def __init__(self, base=None):

        # Output-Widgets container
        self.OutputWidgetsContainer = QWidget(base)
        self.outputContainerLayout = QVBoxLayout(self.OutputWidgetsContainer)
        self.outputStack = QStackedWidget(self.OutputWidgetsContainer)

        """every widget of each module that has to be displayed must be defined here"""
        # time table category widgets declarations (order doesn't matter)
        self.timeTableCreate = TimeTableWindow(self.OutputWidgetsContainer)
        self.timeTableView = ViewTimeTable(self.OutputWidgetsContainer)
        self.timeTableEdit = EditTimeTable(self.OutputWidgetsContainer)
        self.timeTableRemove = RemoveTimeTable(self.OutputWidgetsContainer)

        # exam schedule category widgets declarations (order doesn't matter)
        self.examScheduleCreate = CreateExamSchedule(self.OutputWidgetsContainer)
        self.examScheduleView = ViewExamSchedule(self.OutputWidgetsContainer)
        self.examScheduleDelete = DeleteExamSchedule(self.OutputWidgetsContainer)

        # miscellaneous category widgets declarations (order doesn't matter)
        self.blankWidget = QWidget(self.OutputWidgetsContainer)
        self.calender = QCalendarWidget(self.OutputWidgetsContainer)
        self.template = WorkInProgress(self.OutputWidgetsContainer)
        self.addCourseWindow = AddCourse(self.OutputWidgetsContainer)
        self.addSubjectWindow = AddSubjects(self.OutputWidgetsContainer)
        self.addTeacherWindow = AddTeacher(self.OutputWidgetsContainer)

        """ stacking up all the above widgets (indexes for following widgets start from 0) """
        """ Sequences of the following widgets are important """
        # stacking time table options widget
        self.outputStack.addWidget(self.timeTableCreate.createTimeTableWindow)
        self.outputStack.addWidget(self.timeTableView.timeTableViewWidget)
        self.outputStack.addWidget(self.timeTableEdit.timeTableEditWidget)
        self.outputStack.addWidget(self.timeTableRemove.timeTableRemoveWidget)

        # stacking exam schedule options widget
        self.outputStack.addWidget(self.examScheduleCreate.createExamScheduleWidget)
        self.outputStack.addWidget(self.examScheduleView.viewExamScheduleWidget)
        self.outputStack.addWidget(self.examScheduleDelete.deleteExamScheduleWidget)

        # stacking miscellaneous options widget
        self.outputStack.addWidget(self.addCourseWindow)
        self.outputStack.addWidget(self.addTeacherWindow)
        self.outputStack.addWidget(self.addSubjectWindow)

        # stacking calender (main module itself, with no sub-modules)
        self.outputStack.addWidget(self.calender)

        # stacking independent widgets (not called by any user)
        self.outputStack.addWidget(self.template.incompleteWorkTemplate)
        self.outputStack.addWidget(self.blankWidget)
        self.outputStack.setCurrentIndex(12)                                # set blank/empty widget at startup

        # adding outputStack to the layout of outputContainer
        self.outputContainerLayout.addWidget(self.outputStack)
        
    """------------------------------------- Function Definitions ----------------------------------"""
    # following function is called by another widget ( ) located elsewhere
    def change_window(self, window_index):
        self.outputStack.setCurrentIndex(window_index)
