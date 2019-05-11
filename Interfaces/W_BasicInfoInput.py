"""
Represent a widget (to be placed inside 'BasicInfo_Context_StackContainer' Widget) that act like a container
and contains all stack-screened widgets on top of one another. All the windows (widgets)
that are to be displayed must be imported and instantiated here only.
"""
import sys
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QCheckBox, QComboBox
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoInputForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # variable dependencies
        # list of all major Boards in India
        self.boardList = [
            '-- Select --',
            'Central Board of Secondary Education',
            'Indian Certificate of Secondary Education/Indian School Certificate',
            'State Board'
        ]

        # list of education levels
        self.educationLevels = [
            '-- Select --',
            'Up to 5th class (Primary)',
            'Up to 8th class',
            'Up to 10th class (High School)',
            'Up to 12th class (Intermediate)'
        ]

        # possible stream combination (must be exported from a dedicated file/DB)
        self.streams = [
            'Science (Physics, Chemistry, Maths) with Computers',
            'Science (Physics, Chemistry, Maths) without Computers',
            'Science (Physics, Chemistry, Biology) with Computers',
            'Science (Physics, Chemistry, Biology) without Computers',
            'Commerce'
        ]

        # main layout of the widget
        self.mainLayout = QFormLayout(self)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # input fields widgets
        # text widgets for the window
        self.headingPrompt = QLabel('Please provide basic information about the school.')
        self.schoolNameLabel = QLabel('School Name')
        self.schoolAddressLabel = QLabel('School Address')
        self.boardLabel = QLabel('Board Affiliated to')
        self.educationLevelLabel = QLabel('Offers classes')
        self.streamLabel = QLabel('Streams available')
        self.workingDaysLabel = QLabel('Operates on')

        """" input fields of the window """
        # for school name input
        self.schoolNameField = QLineEdit()                         # input field 1
        self.schoolNameField.setFixedWidth(450)

        # for school address (3 liner) input
        self.schoolAddressFieldPart1 = QLineEdit()            # input field 2 (line 1)
        self.schoolAddressFieldPart1.setFixedWidth(450)
        self.schoolAddressFieldPart2 = QLineEdit()            # Line 2 (part 2)
        self.schoolAddressFieldPart2.setFixedWidth(450)
        self.schoolAddressFieldPart3 = QLineEdit()            # Line 3 (part 3)
        self.schoolAddressFieldPart3.setFixedWidth(450)

        # for board name selection
        self.boardField = QComboBox(self)                         # input field 3
        self.boardField.addItems(self.boardList)                # the passed list values must be fetch from DB
        self.boardField.currentIndexChanged.connect(self.test_calling)
        self.boardField.setFixedWidth(450)

        # for education level selection
        self.educationLevelField = QComboBox(self)          # input field 4
        self.educationLevelField.addItems(self.educationLevels)  # the passed list values must be fetch from DB
        self.educationLevelField.currentIndexChanged.connect(self.test_calling)
        self.educationLevelField.setFixedWidth(450)

        # for stream selection
        # container/area for containing all checkboxes of each stream combinations
        self.streamsInputArea = QWidget(self)                   # input field 5
        self.streamsInputAreaLayout = QVBoxLayout(self.streamsInputArea)
        # generating checkboxes...
        for each_stream in self.streams:
            self.generate_stream_options_for(each_stream)

        # ########
        # form asking about assets of the school (ie classrooms and teachers)
        self.assetFormArea = QWidget(self)
        self.assetFormAreaLayout = QFormLayout(self.assetFormArea)
        self.classCountLabel = QLabel('No. of classrooms')
        self.classCountField = QLineEdit()  # input field 6
        self.classCountField.setFixedWidth(70)
        self.teacherCountLabel = QLabel('No. of teachers')
        self.teacherCountField = QLineEdit()  # input field 6
        self.teacherCountField.setFixedWidth(70)
        self.assetFormAreaLayout.addRow(self.classCountLabel, self.classCountField)
        self.assetFormAreaLayout.addRow(self.teacherCountLabel, self.teacherCountField)

        # widget for timing form
        self.timingInputArea = QWidget(self)
        self.timingInputAreaLayout = QFormLayout(self.timingInputArea)
        self.shiftLabel = QLabel('Total Shifts')
        self.shiftField = QLineEdit()  # input field 6
        self.shiftField.setFixedWidth(70)
        self.schoolHoursLabel = QLabel('School hours')

        # widget for storing 2 input fields (for start timing and end timing)
        self.startEndFields = QWidget(self.timingInputArea)
        self.startEndFieldsLayout = QHBoxLayout(self.startEndFields)
        self.schoolStartTimeField = QLineEdit()  # input field 6
        self.schoolStartTimeField.setFixedWidth(70)
        self.schoolEndTimeField = QLineEdit()  # input field 6
        self.schoolEndTimeField.setFixedWidth(70)
        self.startEndFieldsLayout.addWidget(self.schoolStartTimeField)
        self.startEndFieldsLayout.addWidget(QLabel(' to '))
        self.startEndFieldsLayout.addWidget(self.schoolEndTimeField)
        self.startEndFieldsLayout.addStretch(1)

        # adding widgets to timing form layout
        self.timingInputAreaLayout.addRow(self.shiftLabel, self.shiftField)
        self.timingInputAreaLayout.addRow(self.schoolHoursLabel, self.startEndFields)

        # adding both widget into main layout
        self.mainLayout.addRow(self.schoolNameLabel, self.schoolNameField)
        self.mainLayout.addRow(self.schoolAddressLabel, self.schoolAddressFieldPart1)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart2)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart3)
        self.mainLayout.addRow(self.boardLabel, self.boardField)
        self.mainLayout.addRow(self.educationLevelLabel, self.educationLevelField)
        self.mainLayout.addRow(self.streamLabel, self.streamsInputArea)
        self.mainLayout.addRow(self.assetFormArea, self.timingInputArea)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)

    # function which generates the stream options checkboxes
    def generate_stream_options_for(self, stream):
        stream_option_checkbox = QCheckBox(stream)
        self.streamsInputAreaLayout.addWidget(stream_option_checkbox)

    # dummy function just for testing
    def test_calling(self):
        print('Function called.')


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    basic_info_window_object = BasicInfoInputForm()
    basic_info_window_object.show()
    sys.exit(application.exec_())
