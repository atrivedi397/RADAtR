"""
Represent a widget (to be placed inside 'BasicInfo_Context_StackContainer' Widget) that act like a container
and contains all stack-screened widgets on top of one another. All the windows (widgets)
that are to be displayed must be imported and instantiated here only.
"""
import sys
from PyQt5.QtGui import QColor, QFont, QFontDatabase
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFormLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QCheckBox, QComboBox
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoInputForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # variable dependencies
        self.screenCount = 0                        # used for changing index for stacked widgets
        self.workingDaysCheckboxes = []    # contains all the checkboxes generated for working days
        self.streamCheckboxes = []              # contains all the checkboxes generated for streams
        self.daysSelected = []
        self.streamSelected = []
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
        form_font = QFont("Trebuchet")
        form_font.setPointSize(10)
        self.setFont(form_font)

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.formPalette = self.palette()
        self.formPalette.setColor(self.foregroundRole(), QColor('white'))
        self.setPalette(self.formPalette)

        # input fields widgets
        # text widgets for the window
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
        for index in range(len(self.streams)):
            stream_checkbox = self.generate_stream_options_for(index, self.streams[index])
            self.streamCheckboxes.append(stream_checkbox)

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

        # widget for storing 2 input fields (for start timing and end timing) into single row
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

        # widgets for placing checkboxes for working days
        self.workingDaysCheckboxArea = QWidget(self)
        self.workingDaysCheckboxAreaLayout = QHBoxLayout(self.workingDaysCheckboxArea)
        self.daysList = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        # generating checkboxes...
        for index in range(len(self.daysList)):
            day_checkbox = self.create_working_days_checkbox_for(index, self.daysList[index])
            self.workingDaysCheckboxes.append(day_checkbox)

        # adding all widgets into main layout
        self.mainLayout.addRow(self.schoolNameLabel, self.schoolNameField)
        self.mainLayout.addRow(self.schoolAddressLabel, self.schoolAddressFieldPart1)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart2)
        self.mainLayout.addRow(QLabel(''), self.schoolAddressFieldPart3)
        self.mainLayout.addRow(self.boardLabel, self.boardField)
        self.mainLayout.addRow(self.educationLevelLabel, self.educationLevelField)
        self.mainLayout.addRow(self.streamLabel, self.streamsInputArea)
        self.mainLayout.addRow(self.assetFormArea, self.timingInputArea)
        self.mainLayout.addRow(self.workingDaysLabel, self.workingDaysCheckboxArea)
        self.mainLayout.setContentsMargins(10, 20, 0, 0)
        self.setLayout(self.mainLayout)

    # function which generates the stream options checkboxes
    def generate_stream_options_for(self, checkbox_index, stream_value):
        stream_option_checkbox = QCheckBox(stream_value)
        stream_option_checkbox.toggled.connect(lambda: self.process_stream_checkbox(checkbox_index))
        self.streamsInputAreaLayout.addWidget(stream_option_checkbox)
        return stream_option_checkbox

    # function to create checkboxes for working days
    def create_working_days_checkbox_for(self, checkbox_index, checkbox_value):
        working_day_checkbox = QCheckBox(checkbox_value)
        working_day_checkbox.toggled.connect(lambda: self.process_working_days_checkbox(checkbox_index))
        self.workingDaysCheckboxAreaLayout.addWidget(working_day_checkbox)
        return working_day_checkbox

    # dummy function just for testing
    def test_calling(self):
        print('Function called.')

    # store information into the database
    def initialize_school_configurations(self):
        school_name = self.schoolNameField.text()
        address_line1 = self.schoolAddressFieldPart1.text()
        address_line2 = self.schoolAddressFieldPart2.text()
        address_line3 = self.schoolAddressFieldPart3.text()
        school_address = f'{address_line1} \n {address_line2} \n {address_line3}'
        board_name = self.boardField.currentText()
        education_level = self.educationLevelField.currentText()
        total_classes = self.classCountField.text()
        total_teachers = self.teacherCountField.text()

        print(f'Opted values are as follow:'
              f'School Name: {school_name}'
              f'School Address: {school_address}'
              f'board Name: {board_name}'
              f'Education Level: {education_level}'
              f'Streams available: {self.streamSelected}'
              f'Working Days: {self.daysSelected}'
              f'No. of Classes: {total_classes}'
              f'No. of teacher: {total_teachers}')

    # process working days checkboxes on toggling
    def process_working_days_checkbox(self, checkbox_index):
        if self.workingDaysCheckboxes[checkbox_index].isChecked():
            print(f'Appended {self.daysList[checkbox_index]}')
            self.daysSelected.append(self.daysList[checkbox_index])
        else:
            print(f'Removed {self.daysList[checkbox_index]}')
            self.daysSelected.remove(self.daysList[checkbox_index])

    # process working days checkboxes on toggling
    def process_stream_checkbox(self, checkbox_index):
        if self.streamCheckboxes[checkbox_index].isChecked():
            print(f'Appended {self.streams[checkbox_index]}')
            self.daysSelected.append(self.streams[checkbox_index])
        else:
            print(f'Removed {self.streams[checkbox_index]}')
            self.daysSelected.remove(self.streams[checkbox_index])


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    basic_info_window_object = BasicInfoInputForm()
    basic_info_window_object.show()
    sys.exit(application.exec_())
