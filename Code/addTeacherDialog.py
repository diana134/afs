import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog, QMessageBox
from ui_addTeacherDialog import Ui_AddTeacherDialog
import traceback
from teacher import Teacher

class AddTeacherDialog(QDialog):
    def __init__(self, parent=None, testing=False):
        # Initialize object using ui_addTeacher
        super(AddTeacherDialog, self).__init__(parent)
        self.ui = Ui_AddTeacherDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        self.teacher = None
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addTeacherBtn.clicked.connect(self.addTeacherBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)

    def getTeacher(self):
        """returns the Teacher object created from user data"""
        return self.teacher

    ### Slots ###

    def addTeacherBtn_clicked(self):
        """handles the Add Teacher button being clicked"""
        first = self.ui.firstNameLineEdit.text()
        last = self.ui.lastNameLineEdit.text()
        address = self.ui.addressLineEdit.text()
        city = self.ui.cityLineEdit.text()
        postal = self.ui.postalCodeLineEdit.text()
        daytimePhone = self.ui.daytimePhoneLineEdit.text()
        eveningPhone = self.ui.eveningPhoneLineEdit.text()
        email = self.ui.emailLineEdit.text()
        
        # Error checking
        # TODO: set focus to incorrect field
        if first is None or first == "":
            QMessageBox.warning(self, 'Missing Field', 'Teacher must have a First Name', QMessageBox.Ok)
        elif last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Teacher must have a Last Name', QMessageBox.Ok)
        elif email is None or email == "":
            QMessageBox.warning(self, 'Missing Field', 'Teacher must have email', QMessageBox.Ok)
        else:
            self.teacher = Teacher(first, last, address, city, postal, daytimePhone, eveningPhone, email)
            self.accept()

    def cancelBtn_clicked(self):
        self.reject()