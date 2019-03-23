from Detached.Classes.Teacher import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QVBoxLayout, QHBoxLayout, QFormLayout, QFrame
)


class AddTeacher(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # information variables (must fetch values from database)
        self.departmentList = ['Department of Computer Science', 'Department of Applied Physics']
        self.courseList = ['MCA', 'M.Tech', 'M.Sc I.T.']
        self.designationList = ['Professor', 'Assistant Professor', 'Associate Professor']
        self.message = ''                               # used to show warnings/status upon clicking 'Add' button

        # creating style to apply on heading
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(24)

        # layout of this widget
        self.rootVerticalLayout = QVBoxLayout(self)

        # 3 part of this widget (i.e. Header, Body and Footer)
        # header part:
        self.headerPart = QWidget(self)
        self.headerPartLayout = QVBoxLayout(self.headerPart)

        # widgets inside header part
        self.heading = QLabel('Add Teacher To A Course', self.headerPart)
        self.heading.setFont(self.font)
        self.headingPrompt = QLabel('Please provide following information about the teacher', self.headerPart)
        self.headerPartLayout.addWidget(self.heading)
        self.headerPartLayout.addWidget(self.headingPrompt)

        # body part:
        self.bodyPart = QWidget(self)
        self.bodyPartLayout = QFormLayout(self.bodyPart)

        # widgets inside bodyPart
        self.nameField = QLineEdit()                                           # for teacher's name input
        self.nameField.setFixedWidth(300)
        self.departmentField = QComboBox(self.bodyPart)
        self.departmentField.addItems(self.departmentList)   # name of department which the teacher belongs to
        self.departmentField.setFixedWidth(300)
        self.courseField = QComboBox(self.bodyPart)
        self.courseField.addItems(self.courseList)                    # for name of course which the teacher belongs to
        self.courseField.setFixedWidth(300)
        self.designationField = QComboBox(self.bodyPart)
        self.designationField.addItems(self.designationList)   # for type of designation what the teacher belongs to
        self.designationField.setFixedWidth(200)
        self.maxLecturesField = QLineEdit()
        self.maxLecturesField.setFixedWidth(100)
        self.minLecturesField = QLineEdit()
        self.minLecturesField.setFixedWidth(100)

        # form like alignment/layout for above widget
        self.bodyPartLayout.addRow('Name of the Teacher', self.nameField)
        self.bodyPartLayout.addRow('Teacher\'s Department', self.departmentField)
        self.bodyPartLayout.addRow('Course belongs to', self.courseField)
        self.bodyPartLayout.addRow('Teacher\'s Designation', self.designationField)
        self.bodyPartLayout.addRow('Teacher\'s Max Lectures', self.maxLecturesField)
        self.bodyPartLayout.addRow('Teacher\'s Min Lectures', self.minLecturesField)

        # Footer part:
        self.footerPart = QWidget(self)
        self.footerPartLayout = QHBoxLayout(self.footerPart)

        # widgets inside footer part
        self.footerPrompt = QLabel(self.message, self.footerPart)
        self.cancelButton = QPushButton('Cancel', self.footerPart)
        self.addButton = QPushButton('Add', self.footerPart)
        # self.addButton.clicked.connect(self.add_teacher)                  # uncomment this line to add teacher to DB
        self.footerPartLayout.addWidget(self.footerPrompt, 2)
        self.footerPartLayout.addWidget(self.cancelButton)
        self.footerPartLayout.addWidget(self.addButton)

        # creating a horizontal line
        self.horizontalLine = QFrame(self)
        self.horizontalLine.setFrameShape(QFrame.HLine)
        self.horizontalLine.setFrameShadow(QFrame.Sunken)

        # stacking all the widgets in the main layout
        self.rootVerticalLayout.addWidget(self.headerPart)
        self.rootVerticalLayout.addWidget(self.bodyPart)
        self.rootVerticalLayout.addStretch(5)
        self.rootVerticalLayout.addWidget(self.horizontalLine)
        self.rootVerticalLayout.addWidget(self.footerPart)
        self.rootVerticalLayout.setContentsMargins(80, 10, 0, 0)

    def add_teacher(self):
        name = self.nameField.text()
        department = self.departmentField.currentText()
        designation = self.designationField.currentText()
        course = self.courseField.currentText()
        min_lectures = self.minLecturesField.text()
        max_lectures = self.maxLecturesField.text()

        # creating a Teacher class instance
        teacher = Teacher(name, department, designation, max_lectures, min_lectures, None, course)
        teacher.add_teacher()                           # storing teacher details in database

        # resetting the values of each widget
        self.nameField.clear()
        self.departmentField.setCurrentIndex(0)
        self.designationField.setCurrentIndex(0)
        self.courseField.setCurrentIndex(0)
        self.TextminLectures.clear()
        self.TextmaxLectures.clear()
