import sys
from Detached.Classes.Teacher import *
from PyQt5.QtWidgets import *


class AddingFunctionality(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(600, 400)
        self.setGeometry(300, 90, 600, 400)
        self.setWindowTitle(" UPDATE OF TEACHER'S DATABASE")

        LabelMainWindow = QLabel("PLEASE  ENTER  THE  DETAILS  OF  THE  TEACHERS", self)
        LabelMainWindow.move(120, 2)
        LabelMainWindow.setStyleSheet("font-weight: bold;"
                                      "font-family: Times New Roman ;"
                                      " color: black ; "
                                      "font-size: 10pt")
        add = QPushButton("ADD",self)
        add.move(200,350)
        add.clicked.connect(self.add_teacher)

        # namefield

        self.nameLabel = QLabel("NAME",self)
        self.nameLabel.move(70,70)
        self.nameField = QLineEdit(self)
        self.nameField.move(250,60)
        self.nameField.setFixedWidth(200)
        self.nameField.setFixedHeight(30)

        # DEPARTMENT
        subField = QLabel("DEPARTMENT", self)
        subField.move(70, 110)
        self.department = ["DCS", "Msc.-IT", "HINDI", "MATHS", "BA"]
        self.teacher_options = QComboBox(self)
        self.teacher_options.addItems(self.department)
        self.teacher_options.move(250,110)
        self.teacher_options.setFixedWidth(200)

        # Designation
        nameField = QLabel("DESIGNATION", self)
        nameField.move(70, 190)
        self.designation = ["PROFESSOR", "ASSISTANT PROFESSOR", "ASSOCIATE PROFESSOR"]
        self.teacher_designation = QComboBox(self)
        self.teacher_designation.addItems(self.designation)
        self.teacher_designation.move(250, 190)
        self.teacher_designation.setFixedWidth(200)

        # maximum lectures
        maxLectures = QLabel("MAXIMUM LECTURES", self)
        maxLectures.move(70, 230)
        self.TextmaxLectures = QLineEdit(self)
        self.TextmaxLectures.move(250, 230)
        self.TextmaxLectures.setFixedWidth(200)
        self.TextmaxLectures.setFixedHeight(30)

        # min lectures
        minLectures = QLabel("MINIMUM LECTURES", self)
        minLectures.move(70, 270)
        self.TextminLectures = QLineEdit(self)
        self.TextminLectures.move(250, 270)
        self.TextminLectures.setFixedWidth(200)
        self.TextminLectures.setFixedHeight(30)

    def add_teacher(self):
        name = self.nameField.text()
        department = self.teacher_options.currentText()
        designation = self.teacher_designation.currentText()
        min_lect = self.TextminLectures.text()
        max_lect = self.TextmaxLectures.text()

        teacher = Teacher(name, department, designation, max_lect, min_lect)
        teacher.add_teacher()

        self.nameField.clear()
        self.teacher_options.setCurrentIndex(0)
        self.teacher_designation.setCurrentIndex(0)
        self.TextminLectures.clear()
        self.TextmaxLectures.clear()


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjQApplication.setStyle('Fusion')
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
