"""The widget for calculating average age"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QListWidgetItem
from PyQt4.QtCore import QDate
# from time import strptime
import time

from ui_averageAgeCalculatorDialog import Ui_AverageAgeCalculatorDialog

class AverageAgeCalculatorDialog(QDialog):
    def __init__(self, parent=None):
        # Initialize object using ui_addGroupParticipant
        super(AverageAgeCalculatorDialog, self).__init__(parent)
        self.ui = Ui_AverageAgeCalculatorDialog()
        self.ui.setupUi(self)

         # Set the age as of default date
        self.defaultDate = QDate(QDate.currentDate().year(), 1, 1)
        self.ui.asOfDateEdit.setDate(self.defaultDate)

        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addBirthdateBtn.clicked.connect(self.addBirthdateBtn_clicked)
        self.ui.deleteBirthdateBtn.clicked.connect(self.deleteBirthdateBtn_clicked)
        self.ui.asOfDateEdit.dateChanged.connect(self.asOfDate_changed)
        self.ui.btnBox.rejected.connect(self.closeBtn_clicked)

    def averageDates(self):
        """Calculates and displays the average age"""
        ages = []
        asOfDate = self.ui.asOfDateEdit.date()
        averageAge = 0

        for row in range(self.ui.birthdateListWidget.count()):
            text = str(self.ui.birthdateListWidget.item(row).text())
            date = QDate.fromString(text, "d/M/yyyy")
            age = int(date.daysTo(asOfDate) / 365)
            ages.append(age)

        if len(ages) > 0:
            averageAge = sum(ages)/float(len(ages))

        self.ui.averageAgeLineEdit.setText(str(averageAge))

    ######

    def addBirthdateBtn_clicked(self):
        """Adds a birthdate to the list widget"""
        birthdate = self.ui.birthdateDateEdit.date()

        # Create the string to display
        birthdateString = str(birthdate.toString("d/M/yyyy"))
        QListWidgetItem(birthdateString, self.ui.birthdateListWidget)

        # Re-average the dates
        self.averageDates()

        # Set focus back to date edit
        self.ui.birthdateDateEdit.setFocus()

    def deleteBirthdateBtn_clicked(self):
        """Removes the selected birthdate from the list widget"""
        if self.ui.birthdateListWidget.currentRow() >= 0:
            self.ui.birthdateListWidget.takeItem(self.ui.birthdateListWidget.currentRow())

        # Re-average the dates
        self.averageDates()

    def asOfDate_changed(self):
        """Calls for a re-averaging"""
        self.averageDates()

    def closeBtn_clicked(self):
        """closes the dialog"""
        self.accept()
