"""The form for adding new Teachers"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox

from ui_addTeacherDialog import Ui_AddTeacherDialog
from utilities import sanitize, validateName, stripPhoneNumber
from teacher import Teacher

class AddTeacherDialog(QDialog):
    def __init__(self, parent=None, testing=False, db=None, closeAfterAdd=False):
        # Initialize object using ui_addTeacher
        super(AddTeacherDialog, self).__init__(parent)
        self.ui = Ui_AddTeacherDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        self.db = db
        self.closeAfterAdd = closeAfterAdd
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

    def clearFields(self):
        """Clears and resets all fields"""
        self.ui.firstNameLineEdit.clear()
        self.ui.lastNameLineEdit.clear()
        self.ui.addressLineEdit.clear()
        self.ui.cityLineEdit.clear()
        self.ui.postalCodeLineEdit.clear()
        self.ui.daytimePhoneLineEdit.clear()
        self.ui.eveningPhoneLineEdit.clear()
        self.ui.emailLineEdit.clear()

    ### Slots ###

    def addTeacherBtn_clicked(self):
        """handles the Add Teacher button being clicked"""
        first = str(self.ui.firstNameLineEdit.text()).strip()
        first = sanitize(first)
        last = str(self.ui.lastNameLineEdit.text()).strip()
        last = sanitize(last)
        address = str(self.ui.addressLineEdit.text()).strip()
        address = sanitize(address)
        city = str(self.ui.cityLineEdit.text()).strip()
        city = sanitize(city)
        postal = str(self.ui.postalCodeLineEdit.text()).strip()
        postal = sanitize(postal)
        daytimePhone = str(self.ui.daytimePhoneLineEdit.text()).strip()
        daytimePhone = sanitize(daytimePhone)
        daytimePhone = stripPhoneNumber(daytimePhone)
        eveningPhone = str(self.ui.eveningPhoneLineEdit.text()).strip()
        eveningPhone = sanitize(eveningPhone)
        eveningPhone = stripPhoneNumber(eveningPhone)
        email = str(self.ui.emailLineEdit.text()).strip()
        email = sanitize(email)
        
        # Check for empty fields
        if first is None or first == "":
            QMessageBox.warning(self, 'Missing Field', 'Teacher must have a First Name', QMessageBox.Ok)
        elif last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Teacher must have a Last Name', QMessageBox.Ok)
        elif (email is None or email == "") and QMessageBox.question(self, 'Missing Email', 'Are you sure you want to leave Email blank?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            # Stop here
            pass
        # Check for valid fields
        elif validateName(first) == False and QMessageBox.question(self, 'Validate First Name', 'Are you sure \'' + first + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            # Stop here
            pass
        elif validateName(last) == False and QMessageBox.question(self, 'Validate Last Name', 'Are you sure \'' + last + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            # Stop here
            pass
        else:
            self.teacher = Teacher(first, last, address, city, postal, daytimePhone, eveningPhone, email)
            result = self.teacher.addToDB(self.db)
            if result == "":
                QMessageBox.information(self, 'Add Teacher', 'Successfully added new teacher', QMessageBox.Ok)
                self.clearFields()
                if self.closeAfterAdd:
                    self.accept()
            else:
                QMessageBox.critical(self, 'Add Teacher', 'Failed to add new teacher\n{0}'.format(result), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
