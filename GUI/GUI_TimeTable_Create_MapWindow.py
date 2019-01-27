from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import get_list_of_subject_for


class MapWindow:
    def __init__(self, parent=None):
        # dependencies
        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Sanjay Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]
        self.teacher_combo_boxes = []                       # multiple comboBoxes are required to show dropDowns for each teacher
        self.callingComboBoxIndex = None
        self.subjectList = None
        self.windowOpened = False

        # main widget containing dynamic contents
        self.mapSubWindow = QWidget(parent)

        # main layout (for dynamic contents)
        self.mappingSection = QHBoxLayout(self.mapSubWindow)

        # creating a vertical line
        self.VLine = QFrame(self.mapSubWindow)
        self.VLine.setFrameShape(QFrame.VLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.VLine.hide()

        # sub-layout1 (for subject-teacher 1 to 1 mapping)
        self.mapArea = QVBoxLayout(self.mapSubWindow)               # to be shown on the left

        # sub-layout2 (for subject-teacher 1 to n mapping)
        self.sharedMapArea = QVBoxLayout(self.mapSubWindow)         # to be shown on the right

        # sub-sub layout1 (nested in above layout)
        self.sharingTeacherLayout = QVBoxLayout(self.mapSubWindow)
        self.sharedMapArea.addLayout(self.sharingTeacherLayout)

        # sub x3 nested horizontal layout (for buttons of share-teacher sub window)
        self.shareButtonsLayout = QHBoxLayout(self.mapSubWindow)

        # putting the sub-layouts horizontally
        self.mappingSection.addLayout(self.mapArea)
        self.mappingSection.addWidget(self.VLine)
        self.mappingSection.addLayout(self.sharedMapArea)

        # self.mapSubWindow.setLayout(self.mappingSection)

    def display_sharing_section(self, index):
        # getting current value of selected combo box
        value = self.teacher_combo_boxes[index].currentText()
        if value == 'Shared':
            # showing vertical line (to separate 2 sub windows)
            self.VLine.show()

            self.windowOpened = True                                            # to indicate that sharing window is open now

            # getting index of the operated combo box
            self.callingComboBoxIndex = index

            # disabling all the combo boxes till the sharing option window is open
            for i in range(len(self.teacher_combo_boxes)):
                self.disable_combo_box(i)

            # to generate the list for teachers which would be sharing a subject
            prompt = QLabel(f'Subject {self.subjectList[index]} will be shared by')
            prompt.setWordWrap(True)
            prompt.setContentsMargins(10, 0, 0, 20)
            self.sharingTeacherLayout.addWidget(prompt)

            # required but temporary
            self.checkBoxes = []

            # appending checkbox for each teacher
            # starting from 2 as the 1st two elements of teacher's list are 'none' and 'shared'
            for i in range(2, len(self.teachers)):
                checkbox = QCheckBox(self.teachers[i])
                self.checkBoxes.append(checkbox)

            # displaying the teachers list (along with their checkboxes)
            for i in range(len(self.checkBoxes)):
                self.sharingTeacherLayout.addWidget(self.checkBoxes[i])

            self.sharingTeacherLayout.addStretch(1)

            # for 'share' and 'cancel' buttons layout
            self.shareButtonsLayout.addStretch(1)
            share_teacher_button = QPushButton('Share')
            self.shareButtonsLayout.addWidget(share_teacher_button)         # must be referenced to set other behaviour

            cancel_share_button = QPushButton('Cancel')
            cancel_share_button.clicked.connect(self.close_sharing_section)
            self.shareButtonsLayout.addWidget(cancel_share_button)
            self.sharingTeacherLayout.addLayout(self.shareButtonsLayout)

    def create_combo_box(self, for_index):
        teacher_options_widget = QComboBox()
        teacher_options_widget.addItems(self.teachers)                      # same list of teacher is added as each comboBox items
        teacher_options_widget.currentIndexChanged.connect(lambda: self.display_sharing_section(for_index))
        return teacher_options_widget

    def mapping_options(self, for_semester):
        prompt = QLabel('Please assign the following subjects with their respective lecturer')
        prompt.setContentsMargins(0, 0, 0, 20)
        self.mapArea.addWidget(prompt)

        course = "MCA"                                      # This value is dependent on the Admin attribute
        semester = for_semester                             # getting semester number

        # getting list of subjects for the desired course and semester
        self.subjectList = get_list_of_subject_for(course, semester)

        self.teacher_combo_boxes = []                       # resetting list to be empty
        # creating list of comboBoxes with having same dropDown items
        for i in range(len(self.subjectList)):
            drop_down = self.create_combo_box(i)
            self.teacher_combo_boxes.append(drop_down)
            self.mapArea.addWidget(QLabel(self.subjectList[i]))
            self.mapArea.addWidget(self.teacher_combo_boxes[i])

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

    def close_sharing_section(self):
        # setting 'None' in lieu of 'Shared' if cancel button is pressed
        if self.windowOpened is True:
            self.teacher_combo_boxes[self.callingComboBoxIndex].setCurrentIndex(0)

            # enabling all the disabled drop-downs)
            for i in range(len(self.teacher_combo_boxes)):
                self.enable_combo_box(i)

        # external code to empty the (dynamic layout)
        self.VLine.hide()

        # removing 'share' and 'cancel' button
        while self.shareButtonsLayout.count() > 0:
            item = self.shareButtonsLayout.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # removing teacher's checkboxes
        while self.sharingTeacherLayout.count() > 0:
            item = self.sharingTeacherLayout.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        self.windowOpened = False

    # for disabling all the drop-downs (for selecting teacher) till sharing window is open
    def disable_combo_box(self, at_index):
        self.teacher_combo_boxes[at_index].setEnabled(False)

    # for enabling all the drop-downs (which were disable due to opening of sharing window)
    def enable_combo_box(self, at_index):
        self.teacher_combo_boxes[at_index].setEnabled(True)
