"""The dialog for editing a SoloParticipant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))

from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QDate

from ui_addSoloParticipantDialog import Ui_AddSoloParticipantDialog
# from participant import SoloParticipant
from utilities import *
from databaseInteraction import dbInteractionInstance

class EditSoloParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, participantId=None):
        # Initialize object using ui_addSoloParticipant
        super(EditSoloParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddSoloParticipantDialog()
        self.ui.setupUi(self)
       
        # Initialize class variables
        self.testing = testing
        if participantId is None:
            QMessageBox.critical(self, 'Invalid Participant', "An invalid participant was chosen.", QMessageBox.Ok)
            self.reject()
        if participantId[0] == 's':
            self.participantId = participantId[1:]
        else:
            self.participantId = participantId
        self.participant = dbInteractionInstance.getParticipantFromId(participantId)

        # Initialize ui with variables
        self.ui.addParticipantBtn.setText("&Update Participant")
        self.setWindowTitle("Edit Participant")
        self.ui.firstNameLineEdit.setText(self.participant.first)
        self.ui.lastNameLineEdit.setText(self.participant.last)
        self.ui.addressLineEdit.setText(self.participant.address)
        self.ui.cityLineEdit.setText(self.participant.town)
        self.ui.postalCodeLineEdit.setText(humanPostalCodeFormat(self.participant.postal))
        self.ui.homePhoneLineEdit.setText(humanPhoneNumberFormat(self.participant.home))
        self.ui.cellPhoneLineEdit.setText(humanPhoneNumberFormat(self.participant.cell))
        self.ui.emailLineEdit.setText(self.participant.email)
        self.ui.dateOfBirthDateEdit.setDate(QDate.fromString(self.participant.dob, "yyyy-MM-dd"))
        self.ui.schoolAttendingLineEdit.setText(self.participant.schoolAttending)
        self.ui.parent.setText(self.participant.parent)

        # Set the age display
        self.dob_changed()

        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.dateOfBirthDateEdit.dateChanged.connect(self.dob_changed)

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

        # Check for duplicated participants only if the name has changed
        if first != self.participant.first or last != self.participant.last:
            pList = dbInteractionInstance.getSoloParticipantsWithName(first=first, last=last)
            if len(pList) > 0:
                s = ""
                for p in pList:
                    s += "{0} {1}, born {2}\n".format(p.first, p.last, p.dob)

                if QMessageBox.question(self, 'Possible Duplicate', 
                    'This name exists in the database already:\n{0}\nDo you still want to update this person?'.format(s),
                    QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                    return

        self.participant.first = first
        self.participant.last = last
        self.participant.address = address
        self.participant.town = city
        self.participant.postal = postal
        self.participant.home = home
        self.participant.cell = cell
        self.participant.email = email
        self.participant.dob = dob
        self.participant.schoolAttending = schoolAttending
        self.participant.parent = parent
        result = dbInteractionInstance.updateSoloParticipant(self.participantId, self.participant)
        if result == "":
            QMessageBox.information(self, 'Edit Participant', 'Successfully updated participant', QMessageBox.Ok)
            self.accept()
        else:
            QMessageBox.critical(self, 'Edit Participant', 'Failed to update participant\n{0}'.format(result), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()

    def dob_changed(self):
        dob = self.ui.dateOfBirthDateEdit.date()
        compareDate = QDate(QDate.currentDate().year(), 1, 1)
        age = int(dob.daysTo(compareDate) / 365)
        self.ui.ageLineEdit.setText("{0}".format(age))
