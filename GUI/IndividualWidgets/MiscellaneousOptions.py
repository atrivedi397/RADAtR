"""This class intents to provide modularity and hence, reducing the code of GUI_NavigationPanel."""
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QListWidget)


class MiscellaneousOptions:
    def __init__(self, base=None, function=None, index=0):
        # used to help in determining the start index for another list, embedded in same stacking list
        self.totalOptions = 5  # this must be update if new options are added
        self.functionReference = function
        self.preOccupiedIndexes = index

        # creation of the widget
        self.miscellaneousOptionsWidget = QWidget(base)
        self.miscellaneousOptionsLayout = QVBoxLayout(self.miscellaneousOptionsWidget)

        # heading for Exam-Schedule List
        self.miscellaneousOptionsHead = QLabel('Miscellaneous', self.miscellaneousOptionsWidget)

        # creating options list for exam-schedule module
        self.miscellaneousOptionsList = QListWidget(self.miscellaneousOptionsWidget)

        # List items
        self.miscellaneousOptionsList.insertItem(0, 'Add Course')
        self.miscellaneousOptionsList.insertItem(1, 'Add Teacher')
        self.miscellaneousOptionsList.insertItem(2, 'Add Subject')
        # self.miscellaneousOptionsList.insertItem(3, 'Remove Course')
        # self.miscellaneousOptionsList.insertItem(4, 'Remove Teacher')
        # self.miscellaneousOptionsList.insertItem(5, 'Add Subject')
        self.miscellaneousOptionsList.currentRowChanged.connect(self.miscellaneous_option_changed)

        # stacking up all widgets in vertical layout
        self.miscellaneousOptionsLayout.addWidget(self.miscellaneousOptionsHead)
        self.miscellaneousOptionsLayout.addWidget(self.miscellaneousOptionsList)
        self.miscellaneousOptionsLayout.setContentsMargins(0, 3, 0, 3)

    """----------------------------- Function Definitions ---------------------------------"""
    def miscellaneous_option_changed(self, changed_to_index):
        self.functionReference(self.preOccupiedIndexes + changed_to_index)
