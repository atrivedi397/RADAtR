import sys
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWidgets import *


class AddingFunctionality(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MainWindow()

    def MainWindow(self):
        self.setFixedSize(600, 340)
        self.setGeometry(300, 90, 600, 400)
        self.setWindowTitle(" UPDATION OF TEACHER'S DATABASE")

        LabelMainWindow = QLabel("PLEASE  ENTER  THE  DETAILS  OF  THE  TEACHERS", self)
        LabelMainWindow.move(120, 2)
        LabelMainWindow.setStyleSheet("font-weight: bold;"
                                      "font-family: Times New Roman ;"
                                      " color: black ; "
                                      "font-size: 10pt")
        add = QPushButton("ADD",self)
        add.move(200,290)

        # namefield

        nameField = QLabel("NAME",self)
        nameField.move(70,70)
        self.TextnameField = QTextEdit(self)
        self.TextnameField.move(250,60)
        self.TextnameField.setFixedWidth(200)
        self.TextnameField.setFixedHeight(30)

        AddNew = QPushButton("+", self)
        AddNew.move(458, 68)
        AddNew.setFixedHeight(20)
        AddNew.setFixedWidth(20)
        AddNew.clicked.connect(self.texteditclear)

        #code
        Code = QLabel("CODE", self)
        Code.move(70, 110)
        self.TextCode = QTextEdit(self)
        self.TextCode.move(250, 110)
        self.TextCode.setFixedWidth(200)
        self.TextCode.setFixedHeight(30)

        AddNew3 = QPushButton("+", self)
        AddNew3.move(458, 115)
        AddNew3.setFixedHeight(20)
        AddNew3.setFixedWidth(20)
        AddNew3.clicked.connect(self.textedituidclear)


        # number of semesters
        SemNos = QLabel("NUMBER OF SEMESTERS", self)
        SemNos.move(70, 160)
        self.TextSemNos = QTextEdit(self)
        self.TextSemNos.move(250, 160)
        self.TextSemNos.setFixedWidth(200)
        self.TextSemNos.setFixedHeight(30)

        AddNew5 = QPushButton("+", self)
        AddNew5.move(458, 165)
        AddNew5.setFixedHeight(20)
        AddNew5.setFixedWidth(20)
        AddNew5.clicked.connect(self.textSemNos)

        # start timing
        StartTiming = QLabel("MINIMUM LECTURES", self)
        StartTiming.move(70, 210)
        self.TextStartTiming = QTextEdit(self)
        self.TextStartTiming.move(250, 210)
        self.TextStartTiming.setFixedWidth(200)
        self.TextStartTiming.setFixedHeight(30)

        AddNew5 = QPushButton("+", self)
        AddNew5.move(458, 215)
        AddNew5.setFixedHeight(20)
        AddNew5.setFixedWidth(20)
        AddNew5.clicked.connect(self.textStartTiming)

    def texteditclear(self):
        # write the code to add the text of the text edit to the database
        self.TextnameField.clear()

    def textedituidclear(self):
        # write the code to add the text of the text edit to the database
        self.TextCode.clear()

    def Comboboxdesigclear(self):
        self.teacher_designation.setCurrentIndex(-1)

    def textSemNos(self):
        self.TextSemNos.clear()

    def textStartTiming(self):
        self.TextStartTiming.clear()


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()