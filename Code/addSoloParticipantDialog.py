import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog, QMessageBox
from ui_addSoloParticipantDialog import Ui_AddSoloParticipantDialog
import traceback
from participant import Participant

class AddSoloParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False):
        # Initialize object using ui_addSoloParticipant
        super(AddSoloParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddSoloParticipantDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
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

    ### Slots ###

    def addParticipantBtn_clicked(self):
        """handles the Add Participant button being clicked"""
        first = self.ui.firstNameLineEdit.text()
        last = self.ui.lastNameLineEdit.text()
        address = self.ui.addressLineEdit.text()
        city = self.ui.cityLineEdit.text()
        postal = self.ui.postalCodeLineEdit.text()
        home = self.ui.homePhoneLineEdit.text()
        cell = self.ui.cellPhoneLineEdit.text()
        email = self.ui.emailLineEdit.text()
        dob = self.ui.dateOfBirthDateEdit.date().toString(1)
        # Error checking
        # TODO: set focus to incorrect field
        if first is None or first == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a First Name', QMessageBox.Ok)
        elif last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Last Name', QMessageBox.Ok)
        elif dob is None or dob == "1900-01-01":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Date of Birth', QMessageBox.Ok)
        else:
            self.p = Participant(first, last, address, city, postal, home, cell, email, dob)
            self.accept()

    def cancelBtn_clicked(self):
        self.reject()