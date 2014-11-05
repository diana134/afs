"""The form for storing scheduling options"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QListWidgetItem

from ui_scheduleOptionsDialog import Ui_ScheduleOptionsDialog

class ScheduleOptionsDialog(QDialog):
    def __init__(self, parent=None):
        # Initialize object using ui_addGroupParticipant
        super(ScheduleOptionsDialog, self).__init__(parent)
        self.ui = Ui_ScheduleOptionsDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addSessionBtn.clicked.connect(self.addSessionBtn_clicked)
        self.ui.deleteSessionBtn.clicked.connect(self.deleteSessionBtn_clicked)
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    ######

    def addSessionBtn_clicked(self):
        """Adds a session to the list widget"""
        startDatetimeString = str(self.ui.sessionStartDateTimeEdit.dateTime().toString("yyyy/M/d h:mm AP"))
        endDatetimeString = str(self.ui.sessionEndDateTimeEdit.dateTime().toString("yyyy/M/d h:mm AP"))
        listWidgetString = startDatetimeString + " ==> " + endDatetimeString
        QListWidgetItem(listWidgetString, self.ui.sessionListWidget)

    def deleteSessionBtn_clicked(self):
        """Removes the selected session from the list widget"""
        if self.ui.sessionListWidget.currentRow() >= 0:
            self.ui.sessionListWidget.takeItem(self.ui.sessionListWidget.currentRow())

    def okBtn_clicked(self):
        # TODO save settings
        self.accept()

    def cancelBtn_clicked(self):
        self.reject()
