from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class CreateExamSchedule:
    def __init__(self, base=None, heading=None):
        self.heading = heading
        if heading is None:
            self.heading = 'Oops, Create Schedule isn\'t working yet.'

        # generalized message to be shown on this template
        self.message = "We're so sorry, this submodule isn't completed yet. \n" \
                       "We are trying our best to deliver everything we promised as soon as possible.\n" \
                       "You will see this part working, very soon. Thank you for your cooperation\n."

        # a template widget for displaying 'incomplete' work status
        self.createExamScheduleWidget = QWidget(base)

        # layout for template
        self.createExamScheduleWidgetLayout = QVBoxLayout(self.createExamScheduleWidget)

        # style to heading
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(24)

        # heading of the template
        self.headingLabel = QLabel(self.heading)
        self.headingLabel.setFont(self.font)
        self.messageLabel = QLabel(self.message)

        # stacking all components/widgets vertically
        self.createExamScheduleWidgetLayout.addWidget(self.headingLabel)
        self.createExamScheduleWidgetLayout.setContentsMargins(80, 20, 0, 0)
        self.createExamScheduleWidgetLayout.addWidget(self.messageLabel)
        self.createExamScheduleWidgetLayout.addStretch(4)
