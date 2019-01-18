from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import get_list_of_subject_for


class TimeTableWindow:
    def __init__(self, base=None):
        # dependencies
        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]
        self.semesterList = ["-", "1", "2", "3", "4", "5", "6"]
        self.windowAlreadyOpen = False

        # This is the 'Create' Window
        self.createTimeTableWindow = QWidget(base)

        # text widgets for the window
        self.windowHeading = QLabel('Create Time Table')               # window Heading Text
        self.windowHeading.setStyleSheet('font-size: 16px;'
                                         'font-weight: bold;'
                                         'margin-top: 2px;'
                                         'margin-bottom: 5px;')

        # input fields of the window
        self.semesterField = QComboBox(self.createTimeTableWindow)
        self.semesterField.addItems(self.semesterList)                 # list values must be passed
        self.semesterField.currentIndexChanged.connect(self.test_function)
        self.semesterField.setFixedWidth(60)
        self.batchField = QLineEdit()
        self.batchField.setFixedWidth(60)
        self.timingField = QLineEdit()
        self.timingField.setFixedWidth(80)

        # layout for rows
        self.rows = QVBoxLayout(self.createTimeTableWindow)

        # properties of the horizontal line
        self.horizontalLine = QFrame(self.createTimeTableWindow)
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        # putting main heading in the first row
        self.firstRow = QHBoxLayout(self.createTimeTableWindow)
        self.firstRow.addWidget(self.windowHeading)

        # form layout for all fields (pair of label and field)
        self.semRow = QFormLayout(self.createTimeTableWindow)
        self.semRow.addRow(QLabel("For Semester"), self.semesterField)
        self.semRow.addRow(QLabel("For Batch"), self.batchField)
        self.semRow.addRow(QLabel('Batch start-timing (in 24-hours format)'),
                           self.timingField)

        # 'Generate' and 'Cancel' buttons
        self.finalButton = QHBoxLayout(self.createTimeTableWindow)
        self.generateButton = QPushButton('Generate')
        self.generateButton.setDisabled(True)
        self.cancelButton = QPushButton('Cancel')
        self.cancelButton.clicked.connect(self.close_window)
        self.finalButton.addStretch(5)
        self.finalButton.addWidget(self.generateButton)
        self.finalButton.addWidget(self.cancelButton)

        # dynamic content
        self.dynamicMappingList = QVBoxLayout(self.createTimeTableWindow)

        # adding layouts and widgets into rows
        self.rows.addLayout(self.firstRow)
        self.rows.addLayout(self.semRow)
        self.rows.addLayout(self.dynamicMappingList, 2)
        self.rows.addStretch(1)
        self.rows.addWidget(self.horizontalLine)
        self.rows.addLayout(self.finalButton)
        self.createTimeTableWindow.setLayout(self.rows)
        self.createTimeTableWindow.setContentsMargins(40, 0, 0, 0)

    def test_function(self):
        if self.windowAlreadyOpen:
            self.close_window()
            self.createTimeTableWindow.show()
            self.subject_mappings()
        else:
            self.subject_mappings()

    def subject_mappings(self):
        self.windowAlreadyOpen = True

        self.dynamicMappingList.addWidget(QLabel('Assign the following subjects with respective lecturer'))
        self.dynamicMappingList.addStretch(1)

        # temporary lists
        teacher_combo_boxes = []                            # multiple comboBoxes are required to show dropDowns for each teacher
        subject_stack = []
        
        course = "MCA"                                      # This value is dependent on the Admin attribute
        semester = self.semesterField.currentIndex()        # getting semester number
        
        # getting list of subjects for the desired course and semester
        subject_list = get_list_of_subject_for(course, semester)

        # creating list of comboBoxes with having same dropDown items
        for t in range(len(subject_list)):                  # Teacher comboBox will be created for each subject
            teacher_options = QComboBox()
            teacher_options.setFixedWidth(400)
            teacher_options.addItems(self.teachers)         # same list of teacher is added as each comboBox items
            teacher_combo_boxes.append(teacher_options)     # each dropDown is added to the list

        for i in range(len(subject_list)):
            subject = QLabel(subject_list[i])
            subject_stack.append(subject)
            self.dynamicMappingList.addWidget(subject_stack[i])
            self.dynamicMappingList.addWidget(teacher_combo_boxes[i])

        self.generateButton.setDisabled(False)

    # function to close/hide dynamic content (teacher and subject lists)
    def close_window(self):
        # external code to empty the (dynamic layout)
        while self.dynamicMappingList.count() > 0:
            item = self.dynamicMappingList.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # closing the opened window
        self.createTimeTableWindow.close()
        self.windowAlreadyOpen = False
