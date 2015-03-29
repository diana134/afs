"""The form for getting adjudication sheet options"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QMessageBox
import datetime

from ui_adjudicationOptionsDialog import Ui_AdjudicationOptionsDialog

class AdjudicationOptionsDialog(QDialog):
    def __init__(self, parent=None):
        super(AdjudicationOptionsDialog, self).__init__(parent)
        self.ui = Ui_AdjudicationOptionsDialog()
        self.ui.setupUi(self)
        # Set year to be current year
        self.year = datetime.datetime.now().year
        self.ui.yearLineEdit.setText(str(self.year))
        self.location = ""
        self.adjudicator = ""
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    ######

    def okBtn_clicked(self):
        """Makes sure no fields are blank and hangs on to them for printing"""

        self.location = self.ui.locationLineEdit.text()
        self.year = self.ui.yearLineEdit.text()
        self.adjudicator = self.ui.adjudicatorLineEdit.text()

        # Check for empty fields
        if self.location == "":
            QMessageBox.warning(self, 'Missing Field', 'Need a location', QMessageBox.Ok)
        elif self.year == "":
            QMessageBox.warning(self, 'Missing Field', 'Need a year', QMessageBox.Ok)
        elif self.adjudicator == "":
            QMessageBox.warning(self, 'Missing Field', 'Need an adjudicator', QMessageBox.Ok)
        else:
            # All good
            self.accept()

    def cancelBtn_clicked(self):
        self.reject()