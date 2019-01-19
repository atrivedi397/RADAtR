from GUI.GUI_TimeTable_Create_MapWindow import *


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

        # creating a horizontal line 1 (for being below the semester, batch, timings inputs)
        self.HLine = QFrame(self.createTimeTableWindow)
        self.HLine.setFrameShape(QFrame.HLine)
        self.HLine.setFrameShadow(QFrame.Sunken)

        """To show horizontal lines at 2 places, we need to have 2 different horizontal lines"""
        # creating a horizontal line 2 (for being above the 'generate' and 'cancel' button)
        self.HLine2 = QFrame(self.createTimeTableWindow)
        self.HLine2.setFrameShape(QFrame.HLine)
        self.HLine2.setFrameShadow(QFrame.Sunken)
        self.HLine.hide()                                               # hiding unless mapping list is generated

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
        self.timingForm.addRow(QLabel('Start Timing (in 24 hours)'), self.timingField)

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
        self.fourSections.addLayout(self.thirdSection, 5)
        self.fourSections.addStretch(1)
        self.fourSections.addWidget(self.HLine2)                         # putting a horizontal line
        self.fourSections.addLayout(self.fourthSection)
        self.fourSections.setContentsMargins(40, 10, 20, 10)

        self.createTimeTableWindow.setLayout(self.fourSections)

    def test_function(self):
        # creating class to show mapping options
        external_class = MapWindow(self.createTimeTableWindow)
        self.thirdSection.addWidget(self.HLine)                         # to separate 2nd and 3rd sections
        self.HLine.show()
        self.thirdSection.addWidget(external_class.mapSubWindow)        # displaying mapping options in 3rd Section
        self.thirdSection.addStretch(2)                                 # so that the remaining space is at bottom only
        self.thirdSection.setContentsMargins(0, 20, 0, 0)
        external_class.mapping_options(self.semesterField.currentIndex())
