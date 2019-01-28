from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon       # for importing icon
from PyQt5.QtCore import QSize      # for icon size


class LeftModulePanel:
    def __init__(self, base=None):

        # left most (vertical) toggle bar
        self.modulePanel = QWidget(base)
        self.modulePanel.setMaximumWidth(50)                # static value, need not to be changed

        # layout for left bar
        self.leftBarLayout = QVBoxLayout(self.modulePanel)

        # buttons on the left bar
        self.timeTableButton = QPushButton('', self.modulePanel)
        self.timeTableButton.setIcon(QIcon('Icons/timetable.png'))
        self.timeTableButton.setIconSize(QSize(40, 40))

        # stacking all buttons in left bar
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.timeTableButton)
        self.leftBarLayout.addStretch(20)
        # margin order (left, top, right, bottom)
        self.leftBarLayout.setContentsMargins(1, 0, 1, 0)
        self.leftBarLayout.setSpacing(0)
        self.modulePanel.setLayout(self.leftBarLayout)
