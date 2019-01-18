from PyQt5.QtWidgets import *


class TimeTableWindow:
    def __init__(self, base=None):
        # dependencies
        self.teachers = ["Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]
        self.subjects = ["MCA-401: Database Management System",
                         "MCA-402: Compiler Design",
                         "MCA-403: Data Communication & Computer Networks",
                         "MCA-404: Modeling and Simulation"]

        self.semesterList = ["1", "2", "3", "4", "5", "6"]

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
        self.semesterField.currentIndexChanged.connect(self.subject_mappings)
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

        # form layout for all fields (pair of label and field)
        self.semRow = QFormLayout(self.createTimeTableWindow)
        self.semRow.addRow(QLabel("For Semester"), self.semesterField)
        self.semRow.addRow(QLabel("For Batch"), self.batchField)
        self.semRow.addRow(QLabel('Batch start-timing (in 24-hours format)'),
                           self.timingField)
        self.semRow.addWidget(self.horizontalLine)

        # putting main heading in the first row
        self.firstRow = QHBoxLayout(self.createTimeTableWindow)
        self.firstRow.addWidget(self.windowHeading)
        self.firstRow.addStretch(1)

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

    def subject_mappings(self):
        self.dynamicMappingList.addWidget(QLabel('Assign the following subjects with respective lecturer'))
        self.dynamicMappingList.addStretch(1)

        # temporary lists
        teacher_comboboxes = []
        subject_stack = []

        if len(self.subjects) >= len(self.teachers):
            index = len(self.teachers)
        else:
            index = len(self.subjects)

        # creating list of lists
        for t in range(len(self.teachers)):
            teacher_options = QComboBox()
            teacher_options.setFixedWidth(400)
            teacher_options.addItems(self.teachers)
            teacher_comboboxes.append(teacher_options)

        for i in range(index):
            subject = QLabel(self.subjects[i])
            subject_stack.append(subject)
            self.dynamicMappingList.addWidget(subject_stack[i])
            self.dynamicMappingList.addWidget(teacher_comboboxes[i])

        self.generateButton.setDisabled(False)

    def close_window(self):
        # external code to empty the (dynamic layout)
        while self.dynamicMappingList.count() > 0:
            item = self.dynamicMappingList.takeAt(0)
            if not item:
                continue

            widget = item.widget()
            if widget:
                widget.close()

        # closing the open window
        self.createTimeTableWindow.close()
