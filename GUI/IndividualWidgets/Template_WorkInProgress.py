from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


class WorkInProgress:
    def __init__(self, base=None, heading=None):
        self.heading = heading
        if heading is None:
            self.heading = 'Oops, This isn\'t working yet.'

        # generalized message to be shown on this template
        self.message = "We're so sorry, this submodule isn't completed yet. \n" \
                       "We are trying our best to deliver everything we promised as soon as possible.\n" \
                       "You will see this part working, very soon. Thank you for your cooperation\n."

        # a template for displaying 'incomplete' work status
        self.incompleteWorkTemplate = QWidget(base)

        # layout for template
        self.incompleteWorkTemplateLayout = QVBoxLayout(self.incompleteWorkTemplate)

        # style to heading
        self.font = QFont()
        self.font.setBold(True)
        self.font.setPointSize(16)

        # heading of the template
        self.headingLabel = QLabel(self.heading)
        self.headingLabel.setFont(self.font)
        self.messageLabel = QLabel(self.message)

        # stacking all components/widgets vertically
        self.incompleteWorkTemplateLayout.addWidget(self.headingLabel)
        # self.incompleteWorkTemplateLayout.addStretch(1)
        self.incompleteWorkTemplateLayout.addWidget(self.messageLabel)
        self.incompleteWorkTemplateLayout.addStretch(4)
