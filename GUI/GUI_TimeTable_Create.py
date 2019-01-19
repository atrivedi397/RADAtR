from PyQt5.QtWidgets import *
from Detached.Global.Functions.IndependentFunctions import get_list_of_subject_for
from testFile1 import *


class TimeTableWindow:
    def __init__(self, base=None):
        # dependencies
        self.semesterList = ["-", "1", "2", "3", "4", "5", "6"]

        # This is the 'Create' Window
        self.createTimeTableWindow = QWidget(base)

        # text widgets for the window
        self.windowHeading = QLabel('Create Time Table')               # window Heading Text
        self.windowHeading.setStyleSheet('font-size: 16px;'
                                         'font-weight: bold;'
                                         'margin-top: 2px;'
                                         'margin-bottom: 5px;')

        # input fields of the window
        self.semesterField = QComboBox(self.createTimeTableWindow)      # for semester no. input
        self.semesterField.addItems(self.semesterList)                  # list values must be passed
        self.semesterField.currentIndexChanged.connect(self.test_function)
        self.semesterField.setFixedWidth(60)
        self.batchField = QLineEdit()                                   # for batch input
        self.batchField.setFixedWidth(60)
        self.timingField = QLineEdit()                                  # for timing input (24 hours)
        self.timingField.setFixedWidth(80)
        self.generateButton = QPushButton('Generate')                   # creating 'Generate' button
        self.cancelButton = QPushButton('Cancel')                       # creating 'Cancel' button

        # creating a horizontal line
        self.HLine = QFrame(self.createTimeTableWindow)
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine.setFrameShadow(QFrame.Sunken)

        # layout containing 4 vertical sections (for heading, sem-batch-timing input, mappings and generate-cancel buttons)
        self.fourSections = QVBoxLayout(self.createTimeTableWindow)     # main container for all 4 sub-layouts

        # there's no need to create a sub-layout for heading explicitly. Heading is the first section in its own.
        # sub-layout for semester, batch and timing
        self.secondSection = QHBoxLayout(self.createTimeTableWindow)    # will contain sem, batch, timing input horizontally

        # sub-sub layout1 for semester only
        self.semForm = QFormLayout(self.createTimeTableWindow)          # for sem input, will be nested in 2nd section
        self.semForm.addRow(QLabel('For Semester'), self.semesterField)

        # sub-sub layout2 for batch only
        self.batchForm = QFormLayout(self.createTimeTableWindow)
        self.batchForm.addRow(QLabel('For Batch'), self.batchField)

        # sub-sub layout3 for timing only
        self.timingForm = QFormLayout(self.createTimeTableWindow)
        self.timingForm.addRow(QLabel('Start Timing (in 24 hours'), self.timingField)

        # putting all 3 sub-sub layouts in sub-layout (ie 2nd section)
        self.secondSection.addLayout(self.semForm)
        self.secondSection.addStretch(1)
        self.secondSection.addLayout(self.batchForm)
        self.secondSection.addStretch(1)
        self.secondSection.addLayout(self.timingForm)

        # sub-layout for dynamic contents (ie mapping of subjects and teachers, the 3rd Section)
        self.thirdSection = QVBoxLayout(self.createTimeTableWindow)

        # sub-layout for 'generate' and 'cancel' button (ie 4th Section)
        self.fourthSection = QHBoxLayout(self.createTimeTableWindow)
        self.fourthSection.addStretch(1)
        self.fourthSection.addWidget(self.generateButton)
        self.fourthSection.addWidget(self.cancelButton)

        # putting sub layouts in the main layout (ie fourSections)
        self.fourSections.addWidget(self.windowHeading)                 # heading acts as the first section
        self.fourSections.addLayout(self.secondSection)
        self.fourSections.addStretch(1)
        self.fourSections.addLayout(self.thirdSection, 4)
        self.fourSections.addWidget(self.HLine)                         # putting a horizontal line
        self.fourSections.addLayout(self.fourthSection)

        self.createTimeTableWindow.setLayout(self.fourSections)

    def test_function(self):
        pass
