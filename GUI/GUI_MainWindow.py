import sys
from GUI.GUI_ModulePanel import *
from GUI.GUI_NavigationPanel import *
from GUI.GUI_TimeTable_Create import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # main window properties
        self.setFixedSize(1200, 720)
        self.setWindowTitle('Main Window')

        # menu bar settings
        self.menuBar = QMenuBar(self)

        # adding Menu Tabs
        self.applicationTab = self.menuBar.addMenu('Application')
        self.aboutTab = self.menuBar.addMenu('About')
        self.helpTab = self.menuBar.addMenu('Help')

        # status bar properties
        self.statusBar().showMessage('This is a status bar.')

        # central widget (main parent widget)
        self.container = QWidget(self)
        self.container.setGeometry(0, 21, 1200, 678)      # 21x2 px is taken by menu(top) and status bar(bottom)

        # layout for central widget (container)
        self.containerLayout = QHBoxLayout(self.container)

        # left most (vertical) toggle bar
        self.leftBar = LeftModulePanel(self.container)
        self.leftBar.timeTableButton.clicked.connect(self.toggle_nav)

        self.navBar = NavigationPanel(self.container)
        self.navBar.timeTableList.itemClicked.connect(self.show_widgets)

        # right sided dynamic widgets
        self.blankArea = QWidget(self.container)
        # self.blankArea.setStyleSheet('border: 1px solid green')

        # layout for widgets under blank area
        self.innerLayout = QHBoxLayout(self.blankArea)
        self.createTTWin = TimeTableWindow(self.blankArea)
        self.createTTWin.createTimeTableWindow.hide()
        self.innerLayout.addWidget(self.createTTWin.createTimeTableWindow)
        self.innerLayout.setContentsMargins(0, 0, 0, 0)
        self.blankArea.setLayout(self.innerLayout)

        # stacking all widgets on the main widget (ie container)
        self.containerLayout.addWidget(self.leftBar.modulePanel, 0)
        self.containerLayout.addWidget(self.navBar.navPanel, 0)
        self.containerLayout.addWidget(self.blankArea, 1)
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.containerLayout.setSpacing(0)
        self.container.setLayout(self.containerLayout)

    # function to show/hide "Time-Table" (navigation) bar
    def toggle_nav(self):
        status = self.navBar.navPanel.isHidden()
        if status is False:
            self.navBar.navPanel.hide()
        else:
            self.navBar.navPanel.show()

    def show_widgets(self):
        self.createTTWin.createTimeTableWindow.show()


def main():
    application = QApplication(sys.argv)
    application.setStyle('Fusion')
    main_window_obj = MainWindow()
    main_window_obj.show()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
