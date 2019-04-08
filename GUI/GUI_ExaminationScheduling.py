import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties

        self.setFixedSize(900, 520)
        self.setWindowTitle('Main Window')

        """----------------------WIDGETS USED-------------------------------------------"""
        # central widget (main parent widget)
        self.container = QWidget(self)
        self.container.setGeometry(10, 20, 880, 480)
        # self.container.setStyleSheet(" border:1px solid rgb(0, 0, 25);")

        self.upper_Title_Widget = QWidget(self.container)
        self.upper_Title_Widget.setGeometry(0, 0, 880, 50)
        # self.upper_Title_Widget.setStyleSheet(" border:1px solid rgb(0, 140, 255);")

        self.upper_Widget = QWidget(self.container)
        self.upper_Widget.setGeometry(0, 50, 880, 90)
        # self.upper_Widget.setStyleSheet(" border:1px solid rgb(0, 140, 255);")

        self.middle_middle_Widget = QWidget(self.container)
        self.middle_middle_Widget.setGeometry(440, 150, 30, 250)
        # self.middle_middle_Widget.setStyleSheet(" border:1px solid rgb(0, 45, 255);")

        self.middle_left_Widget = QWidget(self.container)
        self.middle_left_Widget.setGeometry(100, 120, 440, 300)
        # self.middle_left_Widget.setStyleSheet(" border:1px solid rgb(255, 45, 255);")

        self.middle_right_Widget = QWidget(self.container)
        self.middle_right_Widget.setGeometry(570, 120, 440, 300)
        # self.middle_right_Widget.setStyleSheet(" border:1px solid rgb(255, 170, 0 );")

        self.lower_Widget = QWidget(self.container)
        self.lower_Widget.setGeometry(0, 440, 880, 40)
        # self.lower_Widget.setStyleSheet(" border:1px solid rgb(0, 200, 45);")

        self.last_Line_widget = QWidget(self.container)
        self.last_Line_widget.setGeometry(0, 420, 880, 20)
        # self.last_Line_widget.setStyleSheet(" border:1px solid rgb(0, 2, 45);")

        """------------------------INITIAL VALUES OF OBJECTS USED ----------------------"""
        self.listOfCombo = []

        # comboLayout contains the label " CHOOSE THE COURSE " and the combo box of the courses
        self.comboBoxesList = ["MCA", "M Sc. IT", "MA(ENGLISH)", "MCA(EVENING)"]

        # contains the list of all the semesters selected by the user
        self.semestersSelected = []
        self.checkBoxes = []  # contains the text to be written on checkboxes i.e. the semester number
        self.checkBoxesList = []  # contains the list of checkboxes(object)"""

        """"----------------------- calling of functions ---------------------------------"""
        self.button_creation()
        self.semester_checkbox_creation()
        self.course_radiobutton_creation()
        self.textbox_creation()
        self.title_label()
        self.addHline()
        self.add_last_hline()

    """this function creates the checkboxes for the user to select the semester"""

    def title_label(self):
        self.TitleLayout = QVBoxLayout(self.upper_Title_Widget)
        self.SemesterLabel = QLabel(" EXAMINATION SCHEDULING ", self.upper_Title_Widget)
        self.SemesterLabel.setStyleSheet("font: 10pt Comic Sans MS")
        self.VLine = QFrame(self.upper_Title_Widget)
        self.VLine.setFrameShape(QFrame.HLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.TitleLayout.addWidget(self.SemesterLabel)
        self.TitleLayout.addWidget(self.VLine)

    def addHline(self):
        self.lineLayout = QVBoxLayout(self.middle_middle_Widget)
        self.VLine = QFrame(self.middle_middle_Widget)
        self.VLine.setFrameShape(QFrame.VLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.lineLayout.addWidget(self.VLine)

    def add_last_hline(self):
        self.last_lineLayout = QVBoxLayout(self.last_Line_widget)
        self.VLine = QFrame(self.last_Line_widget)
        self.VLine.setFrameShape(QFrame.HLine)
        self.VLine.setFrameShadow(QFrame.Sunken)
        self.last_lineLayout.addWidget(self.VLine)

    def textbox_creation(self):
        self.TexteditLayout = QHBoxLayout(self.upper_Widget)
        self.SlotLabel = QLabel("Enter The Number Of Slots", self.container)
        self.SlotTextbox = QLineEdit(self.upper_Widget)
        self.SlotTextbox.setFixedWidth(100)
        self.SlotTextbox.setFixedHeight(25)

        self.workingdaysLabel = QLabel("Enter The Working Days", self.container)
        self.workingdaysTextbox = QLineEdit(self.container)
        self.workingdaysTextbox.setFixedWidth(100)
        self.workingdaysTextbox.setFixedHeight(25)

        self.BatchLabel = QLabel("Enter The Number Of Batch", self.container)
        self.BatchTextbox = QLineEdit(self.container)
        self.BatchTextbox.setFixedWidth(100)
        self.BatchTextbox.setFixedHeight(25)

        self.TexteditLayout.addWidget(self.SlotLabel)
        self.TexteditLayout.addWidget(self.SlotTextbox)

        self.TexteditLayout.addStretch(1)
        self.TexteditLayout.addWidget(self.workingdaysLabel)
        self.TexteditLayout.addWidget(self.workingdaysTextbox)

        self.TexteditLayout.addStretch(1)
        self.TexteditLayout.addWidget(self.BatchLabel)
        self.TexteditLayout.addWidget(self.BatchTextbox)

    def semester_checkbox_creation(self):
        self.SemesterLayout = QVBoxLayout(self.middle_left_Widget)
        # container layout contains the " CHOOSE THE SEMESTERS " label and the semester checkboxes

        self.SemesterLabel = QLabel(" CHOOSE THE SEMESTERS ", self.middle_left_Widget)
        self.SemesterLabel.setFixedSize(400, 50)
        self.SemesterLayout.addWidget(self.SemesterLabel)

        for semesters in range(6):
            # print (semesters+1)
            self.checkBoxes.append(str(semesters + 1))

        for semesters in self.checkBoxes:
            # print(semesters)
            self.returnFunctionCombo = self.check_box_creation(semesters)
            self.checkBoxesList.append(self.returnFunctionCombo)
            # print(self.checkBoxesList)
            self.SemesterLayout.addWidget(self.returnFunctionCombo)

    """ the function contains the common properties of every checkboxes 
        i contains the text of all the checkboxes that is provided by the semester_check function"""

    def check_box_creation(self, i):
        # print(i)
        self.multipleCheckboxes = QCheckBox(i, self.container)
        # self.multipleCheckboxes.stateChanged.connect(self.click_box)
        return self.multipleCheckboxes

    """ this functions create the combo buttons to select the course"""

    def course_radiobutton_creation(self):
        self.radioButton = []
        self.radioButtonList = []
        self.radioButton = QVBoxLayout(self.middle_right_Widget)
        # container layout contains the " CHOOSE THE SEMESTERS " label and the semester checkboxes

        self.SemesterLabel = QLabel(" CHOOSE THE COURSE ", self.middle_right_Widget)
        self.SemesterLabel.setFixedSize(400, 50)
        self.radioButton.addWidget(self.SemesterLabel)
        self.courseList = ["MCA", "M Sc. IT", "M TECH.", "MBA", "MA(ENGLISH)", "MCA(EVENING)"]

        for semesters in self.courseList:
            # print(semesters)
            self.radiobutton_creation_func_called = self.radio_button_instance_creation(semesters)
            self.radioButtonList.append(self.radiobutton_creation_func_called)
            # print(self.radioButtonList)
            self.radioButton.addWidget(self.radiobutton_creation_func_called)

    """ the function contains the common properties of every checkboxes 
        i contains the text of all the checkboxes that is provided by the semester_check function"""

    def radio_button_instance_creation(self, i):
        # print(i)
        self.multipleCheckboxes = QRadioButton(i, self.container)
        # self.multipleCheckboxes.stateChanged.connect(self.click_box)
        return self.multipleCheckboxes

    def button_creation(self):
        self.buttonLayout = QHBoxLayout(self.lower_Widget)
        self.Submit = QPushButton("SUBMIT", self.lower_Widget)
        self.Submit.setFixedSize(100, 30)
        self.Submit.clicked.connect(self.click_box)
        self.Cancel = QPushButton("CANCEL", self.lower_Widget)
        self.Cancel.setFixedSize(100, 30)
        self.Cancel.clicked.connect(exit)
        self.Reset = QPushButton("RESET", self.lower_Widget)
        self.Reset.setFixedSize(100, 30)
        # self.Reset.clicked.connect()

        self.buttonLayout.addWidget(self.Submit)
        self.buttonLayout.addWidget(self.Cancel)
        self.buttonLayout.addWidget(self.Reset)

    def click_box(self):

        for i in range(6):
            if self.checkBoxesList[i].isChecked():
                # print(self.checkBoxesList[i].text())
                # print("checked")
                self.semestersSelected.append(self.checkBoxesList[i].text())

            else:
                pass
                # print(self.checkBoxesList[i].text())
                # print('Unchecked')
        print(self.semestersSelected)

        for j in range(6):
            if self.radioButtonList[j].isChecked():
                # print(self.checkBoxesList[i].text())
                # print("checked")
                #self.semestersSelected.append(self.radioButtonList[j].text())
                print(self.radioButtonList[j].text())

            else:
                pass
                # print(self.checkBoxesList[i].text())
                # print('Unchecked')

        exit()



    def undo_changes(self):
        pass


def main():
    application = QApplication(sys.argv)
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
