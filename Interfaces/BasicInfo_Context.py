"""
Represent a section (placed inside 'SchoolBasicInfo' Widget) that contains
all stack-screened widgets on top of one another and a buttons sub-section.
 These widgets will be displayed/controlled by the 'next' or 'back' buttons.
"""
from Interfaces.BasicInfo_Context_StackContainer import BasicInfoContextStackContainer
from Interfaces.BasicInfo_Footer import BasicInfoFooter
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoContextSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)

        """
        structure of this widget:
         _____________________________________
        |                                                      |
        |                                                      |
        |        All the widgets which are    |
        |         stacked together and          |
        |   controlled by footer section     |
        |           (Stacked Section)               |
         _____________________________________
        |               (Footer Section)             |
         ______________________________________
        
        """

        # section that will contain all the other widgets
        self.stackedSection = BasicInfoContextStackContainer(self)
        self.footerSection = BasicInfoFooter(self)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.stackedSection, 3)
        self.mainLayout.addWidget(self.footerSection)
        self.mainLayout.setContentsMargins(0, 0, 10, 10)
        self.setLayout(self.mainLayout)
