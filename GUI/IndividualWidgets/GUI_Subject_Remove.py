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

        LabelMainWindow = QLabel("PLEASE  ENTER  THE  DETAILS  OF  THE  SUBJECT  YOU  WANT  TO  DELETE", self)
        LabelMainWindow.move(60, 2)
        LabelMainWindow.setStyleSheet("font-weight: bold;font-family: Times New Roman ; color: black ; font-size: 10pt")
        DisclaimLabel = QLabel("*all the fields are mandatory", self)
        DisclaimLabel.move(45, 380)
        DisclaimLabel.setStyleSheet("font-weight : bold; font- family :Times New Roman ;color : red")

        DeletePushButton = QPushButton("DELETE", self)
        DeletePushButton.move(200, 300)

        CancelPushButton = QPushButton("CANCEL", self)
        CancelPushButton.move(300, 300)

        # DisplayPushButton = QPushButton("DISPLAY", self)
        # DisplayPushButton.move(380, 300)

        self.CourseName()
        self.Semester()
        self.Subjects()

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
        CheckSubjects = QCheckBox("CBNST",self)
        CheckSubjects.move(320, 190)
        CheckSubjects.setStyleSheet("font-weight : bold; font- family :Times New Roman ;color : black")


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
