"""The form for storing scheduling options"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QListWidgetItem, QMessageBox
from PyQt4.QtCore import QDate
from time import strptime

from ui_scheduleOptionsDialog import Ui_ScheduleOptionsDialog
from settingsInteraction import settingsInteractionInstance

class ScheduleOptionsDialog(QDialog):
    def __init__(self, parent=None):
        # Initialize object using ui_addGroupParticipant
        super(ScheduleOptionsDialog, self).__init__(parent)
        self.ui = Ui_ScheduleOptionsDialog()
        self.ui.setupUi(self)
        # Set session dates to be current year
        defaultYear = QDate.currentDate().year()
        self.defaultDate = QDate(defaultYear, 1, 1)
        self.ui.sessionStartDateTimeEdit.setDate(self.defaultDate)
        self.ui.sessionEndDateTimeEdit.setDate(self.defaultDate)
        # Make the buttons do things
        self.connectSlots()
        # TODO load last values

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addSessionBtn.clicked.connect(self.addSessionBtn_clicked)
        self.ui.deleteSessionBtn.clicked.connect(self.deleteSessionBtn_clicked)
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    ######

    def addSessionBtn_clicked(self):
        """Adds a session to the list widget"""
        startDatetime = self.ui.sessionStartDateTimeEdit.dateTime()
        endDatetime = self.ui.sessionEndDateTimeEdit.dateTime()
        if startDatetime >= endDatetime:
            QMessageBox.warning(self, 'Invalid Session Times', 'A session must start before it ends.', QMessageBox.Ok)
            return
        startDatetimeString = str(startDatetime.toString("yyyy/M/d h:mm AP"))
        endDatetimeString = str(endDatetime.toString("yyyy/M/d h:mm AP"))
        listWidgetString = startDatetimeString + " ==> " + endDatetimeString
        QListWidgetItem(listWidgetString, self.ui.sessionListWidget)

    def deleteSessionBtn_clicked(self):
        """Removes the selected session from the list widget"""
        if self.ui.sessionListWidget.currentRow() >= 0:
            self.ui.sessionListWidget.takeItem(self.ui.sessionListWidget.currentRow())

    def okBtn_clicked(self):
        """stores the selected settings and closes the dialog"""
        sessionDatetimes = []

        settingsInteractionInstance.storeJudgingTimePerEntry(str(self.ui.commentsTimeEdit.time().toString("mm:ss")))
        settingsInteractionInstance.storeFinalAdjudicationTime(str(self.ui.adjudicationTimeEdit.time().toString("mm:ss")))
        settingsInteractionInstance.storeTolerance(str(self.ui.toleranceTimeEdit.time().toString("mm:ss")))
        settingsInteractionInstance.storeDiscipline(str(self.ui.disciplineComboBox.currentText()).strip())

        # parse list widget items into sessions for storage
        if self.ui.sessionListWidget.count() <= 0:
            QMessageBox.warning(self, 'Invalid Session Times', 'Must have at least one session to schedule.', QMessageBox.Ok)
            return
        for row in range(self.ui.sessionListWidget.count()):
            text = str(self.ui.sessionListWidget.item(row).text())
            tokens = text.split(" ==> ")
            startDatetime = tokens[0]
            endDatetime = tokens[1]
            sessionDatetimes.append((startDatetime, endDatetime))

        settingsInteractionInstance.storeSessionDatetimes(sessionDatetimes)

        self.accept()

    def cancelBtn_clicked(self):
        self.reject()
