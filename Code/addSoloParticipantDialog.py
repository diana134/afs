import sys
sys.path.insert(0, '../Forms/')
# from PyQt4 import QtGui
from PyQt4.QtGui import QDialog, QMessageBox
# import traceback
from ui_addSoloParticipantDialog import Ui_AddSoloParticipantDialog
from participant import SoloParticipant

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
        first = str(self.ui.firstNameLineEdit.text()).strip()
        last = str(self.ui.lastNameLineEdit.text()).strip()
        address = str(self.ui.addressLineEdit.text()).strip()
        city = str(self.ui.cityLineEdit.text()).strip()
        postal = str(self.ui.postalCodeLineEdit.text()).strip()
        home = str(self.ui.homePhoneLineEdit.text()).strip()
        cell = str(self.ui.cellPhoneLineEdit.text()).strip()
        email = str(self.ui.emailLineEdit.text()).strip()
        dob = str(self.ui.dateOfBirthDateEdit.date().toString(1)).strip()
        # Error checking
        # TODO: set focus to incorrect field
        if first is None or first == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a First Name', QMessageBox.Ok)
        elif last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Last Name', QMessageBox.Ok)
        elif dob is None or dob == "1900-01-01":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Date of Birth', QMessageBox.Ok)
        else:
            self.p = SoloParticipant(first, last, address, city, postal, home, cell, email, dob)
            self.accept()

    def cancelBtn_clicked(self):
        self.reject()
        