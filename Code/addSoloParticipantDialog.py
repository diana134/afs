"""The dialog for adding a SoloParticipant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
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
        # Set the age display
        self.ui.ageLabel.setText("Age as of Jan. 1 {0}".format(QDate.currentDate().year()))
        self.dob_changed()
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
        self.ui.dateOfBirthDateEdit.dateChanged.connect(self.dob_changed)

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
        self.ui.schoolAttendingLineEdit.clear()
        self.ui.parentLineEdit.clear()
        self.ui.ageSpinBox.setValue(18)
        self.ui.schoolGradeLineEdit.clear()

    def dobValid(self):
        """checks if the date of birth is valid given the age; if age is blank returns True"""
        if self.ui.age.text() != "":
            dob = self.ui.dateOfBirthDateEdit.date()
            compareDate = QDate(QDate.currentDate().year(), 1, 1)
            age = int(dob.daysTo(compareDate) / 365)
            return age == int(self.ui.age.text())
        return False

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
        city = str(self.ui.cityLineEdit.text()).strip().capitalize()
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
        schoolAttending = str(self.ui.schoolAttendingLineEdit.text()).strip()
        schoolAttending = sanitize(schoolAttending)
        parent = str(self.ui.parentLineEdit.text()).strip()
        parent = sanitize(parent)
        # Don't need to sanitize this one, it can only be a number
        age = str(self.ui.ageLineEdit.cleanText())
        schoolGrade = str(self.ui.schoolGradeLineEdit.text()).strip()
        schoolGrade = sanitize(schoolGrade)

        # Check if dob is valid relative to age
        # if not, we won't save dob
        if not self.dobValid():
            dob = ""

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

        if email is None or email == "":
            if QMessageBox.question(self, 'Missing Email', 'Are you sure you want to leave Email blank?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return
        # Check for valid fields
        elif validEmail(email) == False:
            QMessageBox.warning(self, 'Invalid Email', email + ' is not a valid email format', QMessageBox.Ok)
            return

        if validateName(first) == False:
            if QMessageBox.question(self, 'Validate First Name', 'Are you sure \'' + first + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if validateName(last) == False:
            if QMessageBox.question(self, 'Validate Last Name', 'Are you sure \'' + last + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        # Check for duplicated participants
        pList = dbInteractionInstance.getSoloParticipantsWithName(first=first, last=last)
        if len(pList) > 0:
            s = ""
            for p in pList:
                s += "{0} {1}, born {2}\n".format(p.first, p.last, p.dob)

            if QMessageBox.question(self, 'Possible Duplicate', 
                'This name exists in the database already:\n{0}\nDo you still want to add this person?'.format(s),
                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        self.p = SoloParticipant(first, last, address, city, postal, home, cell, email, dob, schoolAttending, parent, age, schoolGrade)
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

    def dob_changed(self):
        dob = self.ui.dateOfBirthDateEdit.date()
        compareDate = QDate(QDate.currentDate().year(), 1, 1)
        age = int(dob.daysTo(compareDate) / 365)
        self.ui.ageSpinBox.setValue(age)
