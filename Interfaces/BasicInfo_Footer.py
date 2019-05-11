"""
Represent a section (placed inside 'SchoolBasicInfo' Widget) that contains
all stack-screened widgets on top of one another and a buttons sub-section.
 These widgets will be displayed/controlled by the 'next' or 'back' buttons.
"""
from Global.Styles.Colors import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QPushButton
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoFooter(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main layout of the widget
        self.mainLayout = QHBoxLayout(self)

        # this widget contains 3 parts in the order (prompts, back button, next button)
        self.promptArea = QWidget(self)
        self.backButton = QPushButton('< Back')
        self.nextButton = QPushButton('Next >')

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.promptArea, 2)
        self.mainLayout.addWidget(self.backButton)
        self.mainLayout.addWidget(self.nextButton)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
