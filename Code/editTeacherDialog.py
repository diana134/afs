"""The form for editing Teachers"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QMessageBox

from ui_addTeacherDialog import Ui_AddTeacherDialog
from utilities import *
from databaseInteraction import dbInteractionInstance

class EditTeacherDialog(QDialog):
    def __init__(self, parent=None, testing=False, teacherId=None):
        # Initialize object using ui_addTeacher
        super(EditTeacherDialog, self).__init__(parent)
        self.ui = Ui_AddTeacherDialog()
        self.ui.setupUi(self)
        
        # Initialize class variables
        self.testing = testing
        if teacherId is None:
            QMessageBox.critical(self, 'Invalid Teacher/Contact', "An invalid teacher/contact was chosen.", QMessageBox.Ok)
            self.reject()
        self.teacherId = teacherId
        self.teacher = dbInteractionInstance.getTeacherFromId(teacherId)

        # Initialize ui with variables
        self.ui.addTeacherBtn.setText("&Update Teacher/Contact")
        self.setWindowTitle("Edit Teacher")
        self.ui.firstNameLineEdit.setText(self.teacher.first)
        self.ui.lastNameLineEdit.setText(self.teacher.last)
        self.ui.addressLineEdit.setText(self.teacher.address)
        self.ui.cityLineEdit.setText(self.teacher.city)
        self.ui.postalCodeLineEdit.setText(humanPostalCodeFormat(self.teacher.postal))
        self.ui.daytimePhoneLineEdit.setText(humanPhoneNumberFormat(self.teacher.daytimePhone))
        self.ui.eveningPhoneLineEdit.setText(humanPhoneNumberFormat(self.teacher.eveningPhone))
        self.ui.emailLineEdit.setText(self.teacher.email)

        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addTeacherBtn.clicked.connect(self.addTeacherBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)

    ### Slots ###

    def addTeacherBtn_clicked(self):
        """handles the Add Teacher button being clicked"""
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
            QMessageBox.warning(self, 'Missing Field', 'Must have a First Name', QMessageBox.Ok)
            return
        
        if last is None or last == "":
            QMessageBox.warning(self, 'Missing Field', 'Must have a Last Name', QMessageBox.Ok)
            return

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

        # Check for duplicated teacher only if the name has changed
        if first != self.teacher.first or last != self.teacher.last:
            tList = dbInteractionInstance.getTeachersWithName(first=first, last=last)
            if len(tList) > 0:
                s = ""
                for t in tList:
                    s += "{0} {1}, email: {2}\n".format(t.first, t.last, t.email)

                if QMessageBox.question(self, 'Possible Duplicate', 
                    'This name exists in the database already:\n{0}\nDo you still want to update this person?'.format(s),
                    QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                    return

        self.teacher.first = first
        self.teacher.last = last
        self.teacher.address = address
        self.teacher.city = city
        self.teacher.postal = postal
        self.teacher.daytimePhone = daytimePhone
        self.teacher.eveningPhone = eveningPhone
        self.teacher.email = email
        result = dbInteractionInstance.updateTeacher(self.teacherId, self.teacher)
        if result == "":
            QMessageBox.information(self, 'Edit Teacher/Contact', 'Successfully updated teacher/contact', QMessageBox.Ok)
            self.accept()
        else:
            QMessageBox.critical(self, 'Edit Teacher/Contact', 'Failed to update teacher/contact\n{0}'.format(result), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
