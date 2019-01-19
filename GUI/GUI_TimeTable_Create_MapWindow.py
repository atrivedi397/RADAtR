from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import get_list_of_subject_for


class MapWindow:
    def __init__(self, parent=None):
        # dependencies
        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]

        # main widget containing dynamic contents
        self.mapSubWindow = QWidget(parent)

        # main layout (for dynamic contents)
        self.mappingSection = QHBoxLayout(self.mapSubWindow)

        # sub-layout1 (for subject-teacher 1 to 1 mapping)
        self.mapArea = QVBoxLayout(self.mapSubWindow)               # to be shown on the left

        # sub-layout2 (for subject-teacher 1 to n mapping)
        self.sharedMapArea = QVBoxLayout(self.mapSubWindow)         # to be shown on the right

        # putting the sub-layouts horizontally
        self.mappingSection.addLayout(self.mapArea)
        self.mappingSection.addLayout(self.sharedMapArea)

    def mapping_options(self, for_semester):
        prompt = QLabel('Assign the following subjects with respective lecturer')
        prompt.setContentsMargins(0, 0, 0, 20)
        self.mapArea.addWidget(prompt)
        # temporary lists
        teacher_combo_boxes = []                            # multiple comboBoxes are required to show dropDowns for each teacher
        subject_stack = []

        course = "MCA"                                      # This value is dependent on the Admin attribute
        semester = for_semester                             # getting semester number

        # getting list of subjects for the desired course and semester
        subject_list = get_list_of_subject_for(course, semester)

        # creating list of comboBoxes with having same dropDown items
        for t in range(len(subject_list)):                  # Teacher comboBox will be created for each subject
            teacher_options = QComboBox()
            # teacher_options.setFixedWidth(400)
            teacher_options.addItems(self.teachers)         # same list of teacher is added as each comboBox items
            teacher_combo_boxes.append(teacher_options)     # each dropDown is added to the list

        for i in range(len(subject_list)):
            subject = QLabel(subject_list[i])
            subject_stack.append(subject)
            self.mapArea.addWidget(subject_stack[i])
            self.mapArea.addWidget(teacher_combo_boxes[i])

        # self.base.generateButton.setDisabled(False)

    # function to close/hide dynamic content (teacher and subject lists)
    def close_map_window(self):
        # external code to empty the (dynamic layout)
        while self.mapArea.count() > 0:
            item = self.mapArea.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # closing the opened window
        self.mapSubWindow.close()
