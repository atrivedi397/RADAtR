import sys
from PyQt5.QtWidgets import (
    QWidget, QApplication,
    QVBoxLayout, QFormLayout, QHBoxLayout,
    QLabel, QFrame, QPushButton,
    QLineEdit, QComboBox, QCheckBox
)


class InitialConfigurations(QWidget):
    def __init__(self, base=None):
        super().__init__(base)

        # units are in pixels
        self.windowLeftMargin = 200
        self.windowTopMargin = 0
        self.windowWidth = 800
        self.windowHeight = 600

        self.setWindowTitle('Basic Information')

        # window geometries and positions on the screen
        self.setGeometry(
            self.windowLeftMargin, self.windowTopMargin,
            self.windowWidth, self.windowHeight
        )

        # structure of the window
        """rootWidget (follows vertical layout):
                i) prompt of window,
                ii) form area widget (form layout)
        """

        # root/outermost layout of the window
        self.windowLayout = QVBoxLayout(self)

        # prompt of the window (1st element of root widget)
        self.prompt = QLabel('Provide the basic information of the institute.', self)

        # form widget for inputs (2nd element of root widget)
        self.formWidget = QWidget(self)
        self.formWidgetLayout = QFormLayout(self.formWidget)

        # form's input widgets
        self.instituteName = QLabel('Name of Institute')
        self.instituteNameInputField = QLineEdit()              # institute name input

        self.instituteBranch = QLabel('Branch/Region')
        self.instituteBranchInputField = QLineEdit()            # institute branch input

        # list of all major Boards in India
        self.boardNames = [
            'Central Board of Secondary Education',
            'Indian Certificate of Secondary Education/Indian School Certificate',
            'State Board'
        ]
        self.affiliatedBoard = QLabel('Board affiliated to')
        self.affiliatedBoardInputField = QComboBox(self)
        self.affiliatedBoardInputField.addItems(self.boardNames)

        # list of education levels
        self.educationLevels = [
            'Up to 5th class (Primary)',
            'Up to 8th class',
            'Up to 10th class (High School)',
            'Up to 12th class (Intermediate)'
        ]
        self.instituteEducationLevel = QLabel('Education Level offers')
        self.instituteEducationLevelInputField = QComboBox(self)
        self.instituteEducationLevelInputField.addItems(self.educationLevels)

        # possible stream combination (must be exported from a dedicated file/DB)
        self.streams = [
            'Science (Physics, Chemistry, Maths) with Computers',
            'Science (Physics, Chemistry, Maths) without Computers',
            'Science (Physics, Chemistry, Biology) with Computers',
            'Science (Physics, Chemistry, Biology) without Computers',
            'Commerce'
        ]

        # container/area for containing all checkboxes of each stream combinations
        self.streamsInputArea = QWidget(self.formWidget)
        self.streamsInputAreaLayout = QVBoxLayout(self.streamsInputArea)
        self.streamOptions = QLabel('Streams offered')
        for each_stream in self.streams:
            self.generate_stream_options_for(each_stream)

        # horizontal line (used for separating input fields from buttons)
        self.horizontalLine = QFrame(self)
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        # putting input fields and labels inside form layout
        self.formWidgetLayout.addRow(self.instituteName, self.instituteNameInputField)
        self.formWidgetLayout.addRow(self.instituteBranch, self.instituteBranchInputField)
        self.formWidgetLayout.addRow(self.affiliatedBoard, self.affiliatedBoardInputField)
        self.formWidgetLayout.addRow(self.instituteEducationLevel, self.instituteEducationLevelInputField)
        self.formWidgetLayout.addRow(self.streamOptions, self.streamsInputArea)

        # margins for form area
        left_form_margin = 50
        top_form_margin = 20
        right_form_margin = 130
        bottom_form_margin = 0
        self.formWidgetLayout.setContentsMargins(left_form_margin, top_form_margin, right_form_margin, bottom_form_margin)

        # putting all widgets inside root widget at desired place
        self.windowLayout.addWidget(self.prompt)
        self.windowLayout.addWidget(self.formWidget)
        self.windowLayout.addStretch(1)
        self.setLayout(self.windowLayout)

    # function which generates the stream options checkboxes
    def generate_stream_options_for(self, stream):
        stream_option_checkbox = QCheckBox(stream)
        self.streamsInputAreaLayout.addWidget(stream_option_checkbox)


def main():
    window = QApplication(sys.argv)
    window.setStyle('Fusion')
    initial_config_window = InitialConfigurations()
    initial_config_window.show()
    sys.exit(window.exec_())


if __name__ == '__main__':
    main()
