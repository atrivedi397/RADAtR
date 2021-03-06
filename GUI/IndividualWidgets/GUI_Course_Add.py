from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QFormLayout,
    QPushButton, QFrame
)
from PyQt5.QtGui import QFont


class AddCourse(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # layouts for the window
        self.rootVerticalLayout = QVBoxLayout(self)

        # creating style to apply on heading
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(24)

        self.message = ''                   # used to show any warning or message upon the click of 'Add' button

        # ----------- widgets of the window ---------------
        # header part (contains heading and main prompt)
        self.headerPart = QWidget(self)
        self.headerPartLayout = QVBoxLayout(self.headerPart)
        heading = QLabel("Add a Course", self.headerPart)
        heading.setFont(self.font)
        main_prompt = QLabel("Enter the details of the course to be added.", self.headerPart)
        # adding widget to layout
        self.headerPartLayout.addWidget(heading)
        self.headerPartLayout.addWidget(main_prompt)

        # content part (contains label and input fields)
        self.contentPart = QWidget(self)
        self.nestedFormLayout = QFormLayout(self.contentPart)

        self.courseNameField = QLineEdit()                # for 'course name' input
        self.courseNameField.setFixedWidth(300)
        self.semesterField = QLineEdit()                      # for 'number of semesters' input
        self.semesterField.setFixedWidth(300)
        self.subjectsPerSemester = QLineEdit()           # for 'number of subjects/semester' input
        self.subjectsPerSemester.setFixedWidth(50)
        self.startTimingField = QLineEdit()                   # for 'course start timing' input
        self.startTimingField.setFixedWidth(100)

        # adding widgets into the form layout
        self.nestedFormLayout.addRow(QLabel("Name of the course"), self.courseNameField)
        self.nestedFormLayout.addRow(QLabel("Total semesters in course"), self.semesterField)
        self.nestedFormLayout.addRow(QLabel("Subjects per semester"), self.subjectsPerSemester)
        self.nestedFormLayout.addRow(QLabel("Starting Time (24-hours format)"), self.startTimingField)

        # footer part (contains message area, 'cancel' and 'add' buttons)
        self.footerPart = QWidget(self)
        self.footerPartLayout = QHBoxLayout(self.footerPart)

        # widgets of footer part
        self.prompt = QLabel(self.message, self.footerPart)
        self.cancelButton = QPushButton('Cancel', self.footerPart)
        self.addButton = QPushButton('Add', self.footerPart)
        # adding widgets into the footer-part layout
        self.footerPartLayout.addWidget(self.prompt, 2)
        self.footerPartLayout.addWidget(self.cancelButton)
        self.footerPartLayout.addWidget(self.addButton)

        # creating a horizontal line
        self.horizontalLine = QFrame(self)
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        # stacking all the widgets in the main layout
        self.rootVerticalLayout.addWidget(self.headerPart)
        self.rootVerticalLayout.addWidget(self.contentPart)
        self.rootVerticalLayout.addStretch(5)
        self.rootVerticalLayout.addWidget(self.horizontalLine)
        self.rootVerticalLayout.addWidget(self.footerPart)
        self.rootVerticalLayout.setContentsMargins(80, 10, 0, 0)
