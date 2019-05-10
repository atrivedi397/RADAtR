"""
Represent a sub window or a section (placed inside 'SchoolBasicInfo' Widget)
 that contains main options whose sub options will be displayed elsewhere.
This widget will operate the stack-screened widget (i.e 'context' widget).
"""
from Global.Styles.Colors import *
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoNavSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # appearance of the window (changing background as dark)
        self.setAutoFillBackground(True)
        self.navPalette = self.palette()
        self.navPalette.setColor(self.backgroundRole(), pycharm_dark_blue)
        self.navPalette.setColor(self.foregroundRole(), QColor('lightGrey'))
        self.setPalette(self.navPalette)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)

        # options entries
        self.basicInfoText = QLabel('Basic Information')
        self.feeStructureText = QLabel('Fee Structure')

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # font palette (used for changing font color)
        # self.navTextFontPalette = self.basicInfoText.palette()
        # self.navTextFontPalette.setColor(self.basicInfoText.foregroundRole(), QColor('lightGrey'))
        # self.basicInfoText.setPalette(self.navTextFontPalette)

        self.mainLayout.addWidget(self.basicInfoText)
        self.mainLayout.addWidget(self.feeStructureText)
        self.mainLayout.addStretch(1)
        self.mainLayout.setContentsMargins(20, 20, 0, 0)
        self.setLayout(self.mainLayout)
