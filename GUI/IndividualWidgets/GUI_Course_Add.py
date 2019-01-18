import sys
from PyQt5.QtWidgets import *


class AddCourse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # window properties
        self.setFixedSize(600, 400)
        self.setWindowTitle("Add Course")

        # layouts for the window
        self.mainVLayout = QVBoxLayout(self)
        self.nestedHLayout = QHBoxLayout(self)
        self.nestedFormLayout = QFormLayout(self)

        # ----------- widgets of the window ---------------
        main_prompt = QLabel("Enter the details of the course to be added.")

        self.nameField = QLineEdit()                # for 'name' input
        self.nameField.setFixedWidth(300)
        self.codeField = QLineEdit()
        self.codeField.setFixedWidth(100)
        self.semesterField = QComboBox()
        self.semesterField.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])
        self.semesterField.setFixedWidth(50)
        self.startTimingField = QLineEdit()
        self.startTimingField.setFixedWidth(100)

        # adding widgets into the form layout
        self.nestedFormLayout.addRow(QLabel("Name of the course"), self.nameField)
        self.nestedFormLayout.addRow(QLabel("Code for the course"), self.codeField)
        self.nestedFormLayout.addRow(QLabel("Total Semesters"), self.semesterField)
        self.nestedFormLayout.addRow(QLabel("Starting Time (24-hours format)"), self.startTimingField)

        # adding form into horizontal layout (so it could be in center)
        self.nestedHLayout.addStretch(1)                                # for space on the left
        self.nestedHLayout.addLayout(self.nestedFormLayout)             # displaying form in the center
        self.nestedHLayout.addStretch(1)                                # for space on the right

        # stacking all the widgets in the main layout
        self.mainVLayout.addWidget(main_prompt)
        self.mainVLayout.addStretch(1)
        self.mainVLayout.addLayout(self.nestedHLayout)
        self.mainVLayout.addStretch(2)
        self.setLayout(self.mainVLayout)


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    add_course_object = AddCourse()
    add_course_object.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
