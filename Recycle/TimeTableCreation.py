import sys
from PyQt5.QtWidgets import *


class AddingFunctionality(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.MainWindow()

    def MainWindow(self):
        self.setFixedSize(1100, 650)
        # self.setGeometry(300, 300, 1200, 800)
        self.setWindowTitle(" Add Subject")

        """DisclaimLabel = QLabel("*all the fields are mandatory", self)
        DisclaimLabel.move(45, 380)
        DisclaimLabel.setStyleSheet("font-weight : bold; font- family :Times New Roman ;color : red")"""

        self.nav = QListWidget()
        self.nav.setFixedWidth(170)

        self.nav.insertItem(0, 'Create')
        self.nav.insertItem(1, 'Delete')
        self.nav.insertItem(2, 'View')
        self.nav.insertItem(3, 'Edit')

        self.Create = QWidget()
        self.Delete = QWidget()
        self.View = QWidget()
        self.Edit = QWidget()

        self.CreateFunction()
        self.DeleteFunction()
        self.ViewFunction()
        self.EditFunction()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.Create)
        self.Stack.addWidget(self.Delete)
        self.Stack.addWidget(self.View)
        self.Stack.addWidget(self.Edit)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.nav)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.nav.currentRowChanged.connect(self.display)

    def CreateFunction(self):
        layout = QFormLayout()
        layout.addWidget(QLabel("HEY I AM CREATE FUNCTION"))
        self.Create.setLayout(layout)

    def DeleteFunction(self):
        layout = QFormLayout()
        layout.addWidget(QLabel("HEY I AM DELETE FUNCTION"))
        self.Delete.setLayout(layout)

    def ViewFunction(self):
        layout = QFormLayout()
        layout.addWidget(QLabel("HEY I AM VIEW FUNCTION"))

        self.View.setLayout(layout)

    def EditFunction(self):
        layout = QFormLayout()
        layout.addWidget(QLabel("HEY I AM EDIT FUNCTION"))
        self.Edit.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


def main():
    ObjQApplication = QApplication(sys.argv)
    ObjAddingFunctionality = AddingFunctionality()
    ObjAddingFunctionality.show()
    sys.exit(ObjQApplication.exec_())


if __name__ == '__main__':
    main()
