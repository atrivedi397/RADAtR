import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties

        self.setFixedSize(900, 520)
        self.setWindowTitle('Main Window')

        # central widget (main parent widget)
        self.container = QWidget(self)
        self.container.setGeometry(10, 20, 880, 480)
        self.container.setStyleSheet(" border:1px solid rgb(255, 170, 255);")

        # contains the list of all the semesters selected by the user
        self.semestersSelected = []
        self.checkBoxes = []  # contains the text to be written on checkboxes i.e. the semester number
        self.checkBoxesList = []  # contains the list of checkboxes(object)

        self.FinalLayout = QVBoxLayout(self.container)

        self.slotSemButtonLayout = QVBoxLayout(self.container)

        self.semSubButtonLayout = QVBoxLayout(self.container)
        # semSubButtonLayout is used to place the button and combingLayout vertically
        self.semCourseLayout = QVBoxLayout(self.container)
        # semCourseLayout contains the layout containing containerLayout and comboLayout and place them horizontally
        self.listOfCombo = []

        # comboLayout contains the label " CHOOSE THE COURSE " and the combo box of the courses
        self.comboBoxesList = ["MCA", "M Sc. IT", "MA(ENGLISH)", "MCA(EVENING)"]

        self.semester_check()
        self.course_combo()
        self.submit_cancel()
        self.time_slot()
        self.working_days()
        self.batch()

    """this function creates the checkboxes for the user to select the semester"""

    def semester_check(self):
        self.containerLayout = QHBoxLayout(self.container)
        self.comboLayout = QHBoxLayout(self.container)
        # container layout contains the " CHOOSE THE SEMESTERS " label and the semester checkboxes

        self.SemesterLabel = QLabel(" CHOOSE THE SEMESTERS ", self.container)
        self.containerLayout.addWidget(self.SemesterLabel)

        for semesters in range(6):
            # print (semesters+1)
            self.checkBoxes.append(str(semesters + 1))

        for semesters in self.checkBoxes:
            # print(semesters)
            self.returnFunctionCombo = self.combo_box_creation(semesters)
            self.checkBoxesList.append(self.returnFunctionCombo)
            # print(self.checkBoxesList)
            self.containerLayout.addWidget(self.returnFunctionCombo)

    """ the function contains the common properties of every checkboxes 
    i contains the text of all the checkboxes that is provided by the semester_check function"""

    def combo_box_creation(self, i):
        # print(i)
        self.multipleCheckboxes = QCheckBox(i, self.container)
        # self.multipleCheckboxes.stateChanged.connect(self.click_box)
        return self.multipleCheckboxes

    """ this functions create the combo buttons to select the course"""

    def course_combo(self):

        self.courseLabel = QLabel(" CHOOSE THE COURSE ", self.container)
        self.comboLayout.addWidget(self.containerLayout)
        self.semCourseLayout.addLayout(self.courseLabel)

        self.comboBox = QComboBox(self.container)
        self.comboBox.addItems(self.comboBoxesList)
        self.comboLayout.addWidget(self.comboBox)

        self.semCourseLayout.addLayout(self.comboLayout)

    def submit_cancel(self):
        self.buttonLayout = QHBoxLayout(self.container)
        # buttonLayout contains the two submit and cancel button horizontally
        self.Submit = QPushButton("SUBMIT", self.container)
        self.Submit.clicked.connect(self.click_box)
        self.Cancel = QPushButton("CANCEL", self.container)
        self.Cancel.clicked.connect(exit)

        self.buttonLayout.addWidget(self.Submit)
        self.buttonLayout.addWidget(self.Cancel)

        self.semSubButtonLayout.addLayout(self.semCourseLayout)
        self.semSubButtonLayout.addLayout(self.buttonLayout)

    def click_box(self):
        # displays the current text value of combo box
        self.cur_txt = self.comboBox.currentText()
        # print(self.cur_txt)
        for i in range(6):
            if self.checkBoxesList[i].isChecked():
                # print(self.checkBoxesList[i].text())
                # print("checked")
                self.semestersSelected.append(self.checkBoxesList[i].text())

            else:
                pass
                # print(self.checkBoxesList[i].text())
                # print('Unchecked')
        # print(self.semestersSelected)
        return self.cur_txt, self.semestersSelected

    def time_slot(self):
        self.workingslotbatchLayout = QHBoxLayout(self.container)
        self.slotLabel = QLabel("Enter the number of slots", self.container)
        self.SlotTextbox = QLineEdit(self.container)
        self.SlotTextbox.setFixedWidth(100)
        self.SlotTextbox.setFixedHeight(20)
        self.workingslotbatchLayout.addWidget(self.slotLabel)
        self.workingslotbatchLayout.addWidget(self.SlotTextbox)
        self.workingslotbatchLayout.addStretch(1)

        self.slotSemButtonLayout.addLayout(self.workingslotbatchLayout)
        self.slotSemButtonLayout.addLayout(self.semSubButtonLayout)

    def working_days(self):

        self.workingdaysLabel = QLabel("Enter the working days", self.container)
        self.workingdaysTextbox = QLineEdit(self.container)
        self.workingdaysTextbox.setFixedWidth(100)
        self.workingdaysTextbox.setFixedHeight(20)
        self.workingslotbatchLayout.addWidget(self.workingdaysLabel)
        self.workingslotbatchLayout.addWidget(self.workingdaysTextbox)
        self.workingslotbatchLayout.addStretch(1)

        # self.FinalLayout.addLayout(self.workingslotbatchLayout)
        self.FinalLayout.addLayout(self.slotSemButtonLayout)

    def batch(self):
        self.batchLabel = QLabel("Enter the number of batches", self.container)
        self.batchTextbox = QLineEdit(self.container)
        self.batchTextbox.setFixedWidth(100)
        self.batchTextbox.setFixedHeight(20)
        self.workingslotbatchLayout.addWidget(self.batchLabel)
        self.workingslotbatchLayout.addWidget(self.batchTextbox)
        self.workingslotbatchLayout.addStretch(1)

        self.FinalLayout.addLayout(self.workingslotbatchLayout)
        self.FinalLayout.addLayout(self.slotSemButtonLayout)


def main():
    application = QApplication(sys.argv)
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
