from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont


class RemoveTimeTable:
    def __init__(self, base=None, heading=None):
        self.heading = heading
        if heading is None:
            self.heading = 'Oops, Remove time-table window isn\'t working yet.'

        # generalized message to be shown on this template
        self.message = "We're so sorry, this sub-module isn't completed yet. \n" \
                       "We are trying our best to deliver everything we promised as soon as possible.\n" \
                       "You will see this part working, very soon. Thank you for your cooperation\n."

        # a template for displaying 'incomplete' work status
        self.timeTableRemoveWidget = QWidget(base)

        # layout for template
        self.incompleteWorkTemplateLayout = QVBoxLayout(self.timeTableRemoveWidget)

        # style to heading
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(24)

        # heading of the template
        self.headingLabel = QLabel(self.heading)
        self.headingLabel.setFont(self.font)
        self.messageLabel = QLabel(self.message)

        # stacking all components/widgets vertically
        self.incompleteWorkTemplateLayout.addWidget(self.headingLabel)
        self.incompleteWorkTemplateLayout.setContentsMargins(80, 20, 0, 0)
        self.incompleteWorkTemplateLayout.addWidget(self.messageLabel)
        self.incompleteWorkTemplateLayout.addStretch(4)
