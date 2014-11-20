"""The dialog for adding a SoloParticipant"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QDate

from ui_addSoloParticipantDialog import Ui_AddSoloParticipantDialog
from participant import SoloParticipant
from utilities import *
from databaseInteraction import dbInteractionInstance

class AddSoloParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, closeAfterAdd=False):
        # Initialize object using ui_addSoloParticipant
        super(AddSoloParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddSoloParticipantDialog()
        self.ui.setupUi(self)
        # Set default date to January 1 18 years ago
        defaultYear = (QDate.currentDate().addYears(-18)).year()
        self.defaultDate = QDate(defaultYear, 1, 1)
        self.ui.dateOfBirthDateEdit.setDate(self.defaultDate)
        # Initialize class variables
        self.testing = testing
        self.closeAfterAdd = closeAfterAdd
        self.p = None
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)

    def getParticipant(self):
        """returns the Participant object created from user data"""
        return self.p

    def clearFields(self):
        """Clears and resets all fields"""
        self.ui.firstNameLineEdit.clear()
        self.ui.lastNameLineEdit.clear()
        self.ui.addressLineEdit.clear()
        self.ui.cityLineEdit.clear()
        self.ui.postalCodeLineEdit.clear()
        self.ui.homePhoneLineEdit.clear()
        self.ui.cellPhoneLineEdit.clear()
        self.ui.emailLineEdit.clear()
        self.ui.dateOfBirthDateEdit.setDate(self.defaultDate)

    ### Slots ###

    def addParticipantBtn_clicked(self):
        """handles the Add Participant button being clicked"""
        # Get the data and sanitize it
        first = str(self.ui.firstNameLineEdit.text()).strip()
        first = sanitize(first)
        last = str(self.ui.lastNameLineEdit.text()).strip()
        last = sanitize(last)
        address = str(self.ui.addressLineEdit.text()).strip()
        address = sanitize(address)
        city = str(self.ui.cityLineEdit.text()).strip()
        city = sanitize(city)
        postal = str(self.ui.postalCodeLineEdit.text()).replace(" ", "")
        postal = sanitize(postal)
        postal = stripPostal(postal)
        home = str(self.ui.homePhoneLineEdit.text()).strip()
        home = sanitize(home)
        home = stripPhoneNumber(home)
        cell = str(self.ui.cellPhoneLineEdit.text()).strip()
        cell = sanitize(cell)
        cell = stripPhoneNumber(cell)
        email = str(self.ui.emailLineEdit.text()).strip()
        email = sanitize(email)
        # Don't need to sanitize this one, it can only be a date
        dob = str(self.ui.dateOfBirthDateEdit.date().toString(1)).strip()

        # Check for empty fields
        if first is None or first == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a First Name', QMessageBox.Ok)
            return
        
        if last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Last Name', QMessageBox.Ok)
            return
        
        # if dob is None or dob == "1900-01-01":
        #     QMessageBox.warning(self, 'Missing Field', 'Participant must have a Date of Birth', QMessageBox.Ok)
        #     return

        # Check for valid fields
        if email != "" and validEmail(email) == False:
            QMessageBox.warning(self, 'Invalid Email', email + ' is not a valid email format', QMessageBox.Ok)
            return

        if validateName(first) == False:
            if QMessageBox.question(self, 'Validate First Name', 'Are you sure \'' + first + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if validateName(last) == False:
            if QMessageBox.question(self, 'Validate Last Name', 'Are you sure \'' + last + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        self.p = SoloParticipant(first, last, address, city, postal, home, cell, email, dob)
        result = dbInteractionInstance.addSoloParticipant(self.p)
        if result == "":
            QMessageBox.information(self, 'Add Participant', 'Successfully added new participant', QMessageBox.Ok)
            self.clearFields()
            if self.closeAfterAdd:
                self.accept()
        else:
            QMessageBox.critical(self, 'Add Participant', 'Failed to add new participant\n{0}'.format(result), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
        