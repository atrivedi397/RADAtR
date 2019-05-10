"""
Represent a window (Widget) for inputting all basic information about the school.
This window is meant for admins only and is displayed only after the admin login.
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget,  QHBoxLayout
)


# represents whole window
class SchoolBasicInfoWindow(QWidget):
    def __int__(self, parent=None):
        super().__init__(parent)

        print('hi')

        # title of the main window
        window_title = 'School Basic Information'
        self.setWindowTitle(window_title)

        # values are in pixels
        self.windowTopMargin = 10
        self.windowLeftMargin = 10
        self.windowHeight = 600
        self.windowWidth = 1280

        # initializing size and the location on screen for the window
        self.setGeometry(self.windowTopMargin, self.windowLeftMargin, self.windowWidth, self.windowHeight)

        # main layout of the widget
        self.mainLayout = QHBoxLayout(self)

        """the structure of the window is like follow:
             __________________________________________________
            |                       |                                                |
            |  navigation    |              context                     |
            |   section        |              section                      |
            |                       |                                                |
            ___________________________________________________
            
        """

        # navigation section widget (to be placed on the left side)
        self.navigationSection = QWidget(self)

        # context section widget (to be placed on the right side)
        self.contextSection = QWidget(self)

        # adding above sections (i.e. navigation and context) to the main layout
        self.mainLayout.addWidget(self.navigationSection)
        self.mainLayout.addWidget(self.contextSection)
        self.setLayout(self.mainLayout)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    basic_info_window_object = SchoolBasicInfoWindow()
    basic_info_window_object.show()
    sys.exit(application.exec_())
