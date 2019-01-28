from PyQt5.QtWidgets import *
import sys


class Some:
    def __init__(self):
        self.widget = QWidget()

        self.teachers = ["None", "Shared", "Manoj Kumar", "Narendra Kumar", "Santosh Kumar Dwivedi", "Vipin Saxena", "Deepa Raj", "Shalini Chandra"]

        self.layout = QVBoxLayout(self.widget)
        self.comboBoxes = []

        for widget in range(len(self.teachers)):
            someWid = self.test_function2(widget)
            # someWid.currentIndexChanged.connect(lambda: self.test_function(widget))
            self.comboBoxes.append(someWid)

        self.widget.setLayout(self.layout)

    def test_function(self, index):
        value = self.comboBoxes[index].currentText()
        print(f'Combo Box index is {index} and its value is {value}')

    def test_function2(self, i):
        CB = QComboBox()
        CB.addItems(self.teachers)
        CB.currentIndexChanged.connect(lambda: self.test_function(i))
        self.layout.addWidget(CB)
        return CB


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    obj = Some()
    obj.widget.show()
    sys.exit(app.exec_())
