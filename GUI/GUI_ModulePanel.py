from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon       # for importing icon
from PyQt5.QtCore import QSize      # for icon size


class LeftModulePanel:
    def __init__(self, base=None, controlling_widget=None):
        self.widgetReference = controlling_widget
        self.lastActiveModuleIndex = None

        # left most (vertical) toggle bar
        self.modulePanel = QWidget(base)
        self.modulePanel.setMaximumWidth(50)                # static value, need not to be changed

        # tooltip styling
        self.modulePanel.setStyleSheet('QToolTip{'
                                       'color: white;'
                                       'background-color: black;'
                                       'border: 0px}')

        # layout for left bar
        self.leftBarLayout = QVBoxLayout(self.modulePanel)

        """----------- buttons on the (left) Modules Panel --------------"""
        # for timeTable module (Indexed at 0)
        self.timeTableButton = QPushButton('', self.modulePanel)
        self.timeTableButton.clicked.connect(lambda: self.show_module_options(0))
        self.timeTableButton.setIcon(QIcon('Icons/passage-of-time.svg'))
        self.timeTableButton.setIconSize(QSize(40, 40))
        self.timeTableButton.setToolTip('Time Table Management')

        # for scheduleExam module (Indexed at 1)
        self.examScheduleButton = QPushButton('', self.modulePanel)
        self.examScheduleButton.clicked.connect(lambda: self.show_module_options(1))
        self.examScheduleButton.setIcon(QIcon('Icons/a.svg'))
        self.examScheduleButton.setIconSize(QSize(40, 40))
        self.examScheduleButton.setToolTip('Exam Scheduling')

        # for Admission module (Indexed at 2)
        self.admissionButton = QPushButton('', self.modulePanel)
        self.admissionButton.setIcon(QIcon('Icons/study.svg'))
        self.admissionButton.setIconSize(QSize(40, 40))
        self.admissionButton.setToolTip('Admission Processing')

        # for calender or home screen (Indexed at 3)
        self.calenderButton = QPushButton('', self.modulePanel)
        self.calenderButton.setIcon(QIcon('Icons/calendar.svg'))
        self.calenderButton.setIconSize(QSize(40, 40))
        self.calenderButton.setToolTip('Show Calendar')

        # for miscellaneous sub-modules (Indexed at 4)
        self.unitSubModuleButton = QPushButton('', self.modulePanel)
        self.unitSubModuleButton.clicked.connect(lambda: self.show_module_options(2))
        self.unitSubModuleButton.setIcon(QIcon('Icons/test.svg'))
        self.unitSubModuleButton.setIconSize(QSize(40, 40))
        self.unitSubModuleButton.setToolTip('Other Administrative Tasks')

        # stacking all buttons inside the (left-most) panel
        self.leftBarLayout.addStretch(5)
        self.leftBarLayout.addWidget(self.timeTableButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.examScheduleButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.admissionButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.unitSubModuleButton)
        self.leftBarLayout.addStretch(1)
        self.leftBarLayout.addWidget(self.calenderButton)
        self.leftBarLayout.addStretch(30)

        # margin order (left, top, right, bottom)
        self.leftBarLayout.setContentsMargins(1, 0, 1, 0)
        self.leftBarLayout.setSpacing(0)
        self.modulePanel.setLayout(self.leftBarLayout)

    """-------------------------- Function Definitions -----------------------------"""
    # function to show/hide sub-modules list
    def toggle_nav(self):
        status = self.widgetReference.navPanel.isHidden()
        if status is False:
            self.widgetReference.navPanel.hide()
        else:
            self.widgetReference.navPanel.show()

    def show_module_options(self, module_index):
        # if same module button is pressed twice in sequence, toggle_list
        if module_index == self.lastActiveModuleIndex:
            self.toggle_nav()
        else:   # change to new sub-module list
            self.widgetReference.submoduleStack.setCurrentIndex(module_index)
            self.widgetReference.navPanel.setHidden(False)
            self.lastActiveModuleIndex = module_index
