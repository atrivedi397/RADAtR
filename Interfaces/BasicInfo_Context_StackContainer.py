"""
Represent a section (placed inside 'BasicInfo_Context' Widget) that act like a container
and contains all stack-screened widgets on top of one another. All the windows (widgets)
that are to be displayed must be imported and instantiated here only.
"""
from Interfaces.W_BasicInfoInput import BasicInfoInputForm
from PyQt5.QtGui import QFont, QPalette
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget
)


# represents navigation section inside 'School Basic Information' window
class BasicInfoContextStackContainer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main layout of the widget
        self.mainLayout = QVBoxLayout(self)
        # self.setStyleSheet('border: 1px solid white;')

        """
        structure of this widget:
         _____________________________________
        |                                                      |
        |                                                      |
        |        All the widgets which are    |
        |               stacked together           |
        |                                                      |
         _____________________________________

        """

        # container for all the other widgets which are to be stacked
        self.widgetStackContainer = QStackedWidget(self)

        # instantiating all the required widgets
        self.basicInfoForm = BasicInfoInputForm(self)

        # stacking widgets
        self.widgetStackContainer.addWidget(self.basicInfoForm)
        self.widgetStackContainer.setCurrentIndex(0)

        # font family, size and color
        self.navTextFont = QFont()
        self.navTextFont.setBold(False)
        self.navTextFont.setPointSize(13)  # in pixels
        self.setFont(self.navTextFont)

        # adding both widget into main layout
        self.mainLayout.addWidget(self.widgetStackContainer)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainLayout)
