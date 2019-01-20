import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AddingFunctionality(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 700, 300)
        self.title = 'correction'
        self.initUI()
        self.createCombo()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(300, 300, 700, 300)


    def createCombo(self):
            global k
            k = 50
        #for i in range (4):
            self.comboTeachers = QComboBox(self)
            self.teachers = ["PROFF . SANJAY KUMAR DIWEDI",
                             "PROFF . VIPIN SAXENA",
                             "DR.  DEEPA RAJ",
                             "DR . MANOJ KUMAR",
                             "DR. SHALINI CHANDRA"]

            self.comboTeachers.addItems(self.teachers)

            # self.comboTeachers.move(200, 50)
            self.comboTeachers.move(200, k)
            """for i in self.teachers:
                print(i, self.teachers.index(i))"""
            k+=10
            self.comboTeachers.activated.connect(self.handleActivated)

    def handleActivated(self, index):
        print(self.comboTeachers.currentIndex(), self.comboTeachers.itemText(index))



def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
