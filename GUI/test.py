import sys
from PyQt5.QtWidgets import *


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
        self.upper_Title_Widget.setGeometry(0, 0, 880, 30)
        # self.upper_Title_Widget.setStyleSheet(" border:1px solid rgb(0, 140, 255);")

        self.upper_Widget = QWidget(self.container)
        self.upper_Widget.setGeometry(0, 30, 880, 90)
        # self.upper_Widget.setStyleSheet(" border:1px solid rgb(0, 140, 255);")

        self.middle_left_Widget = QWidget(self.container)
        self.middle_left_Widget.setGeometry(0, 120, 440, 300)
        # self.middle_left_Widget.setStyleSheet(" border:1px solid rgb(255, 45, 255);")

        self.middle_middle_Widget = QWidget(self.container)
        self.middle_middle_Widget.setGeometry(440, 120, 30, 300)
        # self.middle_middle_Widget.setStyleSheet(" border:1px solid rgb(0, 45, 255);")


        self.middle_right_Widget = QWidget(self.container)
        self.middle_right_Widget.setGeometry(440, 120, 440, 300)
        # self.middle_right_Widget.setStyleSheet(" border:1px solid rgb(255, 170, 0 );")

        self.lower_Widget = QWidget(self.container)
        self.lower_Widget.setGeometry(0, 420, 880, 40)
        self.lower_Widget.setStyleSheet(" border:1px solid rgb(0, 200, 45);")

        self.last_Line_widget = QWidget(self.container)
        self.last_Line_widget.setGeometry(0, 460, 880, 20)
        self.last_Line_widget.setStyleSheet(" border:1px solid rgb(0, 2, 45);")

def main():
    application = QApplication(sys.argv)
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()

