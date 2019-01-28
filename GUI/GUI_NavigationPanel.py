from PyQt5.QtWidgets import *


class NavigationPanel:
    def __init__(self, base=None):

        # navigation panel
        self.navPanel = QWidget(base)
        self.navPanel.setFixedWidth(175)

        # navigation panel layout
        self.navLayout = QVBoxLayout(self.navPanel)

        # for Time-Table List
        self.timeTableList = QListWidget(self.navPanel)
        # self.timeTableList.setFixedWidth(200)

        # List items
        self.timeTableList.insertItem(0, 'Creation')
        self.timeTableList.insertItem(1, 'Viewing')
        self.timeTableList.insertItem(2, 'Editing')
        self.timeTableList.insertItem(3, 'Deletion')

        # heading for Time-Table List
        self.timeTableHead = QLabel('Time Table:', self.navPanel)

        # stacking up all widgets in vertical layout
        self.navLayout.addWidget(self.timeTableHead)
        self.navLayout.addWidget(self.timeTableList)
        self.navLayout.setContentsMargins(0, 3, 0, 3)
        self.navLayout.setSpacing(1)
        self.navPanel.setLayout(self.navLayout)
