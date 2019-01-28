import sys
from PyQt5.QtWidgets import *


class AddingFunctionality(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MainWindow()

    def MainWindow(self):
        self.setFixedSize(600, 400)
        self.setGeometry(300, 90, 600, 400)
        self.setWindowTitle(" Add Subject")

        LabelMainWindow = QLabel("PLEASE  ENTER  THE  DETAILS  OF  THE  SUBJECT  YOU  WANT  TO  ADD", self)
        LabelMainWindow.move(85, 2)
        LabelMainWindow.setStyleSheet("font-weight: bold;font-family: Times New Roman ; color: black ; font-size: 10pt")
        DisclaimLabel = QLabel("*all the fields are mandatory", self)
        DisclaimLabel.move(85, 380)
        DisclaimLabel.setStyleSheet("font-weight : bold; font- family :Times New Roman ;color : red")

        OkPushButton = QPushButton("OKAY", self)
        OkPushButton.move(200, 300)

        CancelPushButton = QPushButton("CANCEL", self)
        CancelPushButton.move(300, 300)

        # DisplayPushButton = QPushButton("DISPLAY", self)
        # DisplayPushButton.move(380, 300)

        global x
        x = 190
        self.CourseName()
        self.Semester()
        self.Subjects()
        self.AdditionOfAdd()
        # self.Test()

    def CourseName(self):
        LabelCourseName = QLabel("Course Name", self)
        LabelCourseName.move(60, 70)
        LabelCourseName.setStyleSheet("font-family:italics")
        ComboCourseName = QComboBox(self)
        ComboCourseName.move(320, 70)
        ComboCourseName.addItems(["MCA", "MSC - IT", "MA - HINDI", "MSC-MATHS"])
        ComboCourseName.setFixedHeight(30)
        ComboCourseName.setFixedWidth(200)
        # ComboCourseName.styleSheet("font-weight : bold; font- family :Times New Roman ;color : red")

    def Semester(self):
        LabelSemester = QLabel("Semester", self)
        LabelSemester.move(60, 130)
        LabelSemester.setStyleSheet("font-family:italics")
        ComboSemester = QComboBox(self)
        ComboSemester.move(320, 130)
        ComboSemester.addItems(["1", "2", "3", "4", "5", "6", "7", "8"])

    def Subjects(self):
        LabelSubjects = QLabel("Subjects", self)
        LabelSubjects.move(60, 190)
        LabelSubjects.setStyleSheet("font-family:italics")
        LabelTextEdit = QTextEdit(self)
        LabelTextEdit.setFixedHeight(30)
        LabelTextEdit.setFixedWidth(200)
        LabelTextEdit.move(320, x)
        LabelTextEdit.setStyleSheet("font - weight : bold; font - family :Times New Roman; color : black")
        self.x = x + 100

    def AdditionOfAdd(self):
        AddNew = QPushButton("+", self)
        AddNew.move(530, 195)
        AddNew.setFixedHeight(20)
        AddNew.setFixedWidth(20)
        AddNew.clicked.connect(self.Test)

    def Test(self):
        hello = QPushButton("hello", self)


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
