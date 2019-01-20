from PyQt5.QtWidgets import *
import sys


class Some:
    def __init__(self):
        self.widget = QWidget()

        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]

        self.layout = QVBoxLayout(self.widget)
        self.comboBoxes = [QComboBox() for i in range(5)]

        for widget in range(len(self.comboBoxes)):
            self.comboBoxes[widget].addItems(self.teachers)
            self.comboBoxes[widget].currentIndexChanged.connect(lambda: self.test_function(widget, self.comboBoxes[widget].currentText()))
            self.layout.addWidget(self.comboBoxes[widget])

        self.widget.setLayout(self.layout)

    def test_function(self, index, value):
        print(f'Combo Box index is {index} and its value is {value}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    obj = Some()
    obj.widget.show()
    sys.exit(app.exec_())
