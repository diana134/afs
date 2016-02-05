"""The dialog for adding a Participant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QDate

from ui_addParticipantDialog import Ui_AddParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from addTeacherDialog import AddTeacherDialog
# from participantWidget import ParticipantWidget
from averageAgeCalculatorDialog import AverageAgeCalculatorDialog
from participant import Participant
from utilities import *
from databaseInteraction import dbInteractionInstance

class AddParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, closeAfterAdd=False):
        # Initialize object using ui_addSoloParticipant
        super(AddParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddParticipantDialog()
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
        # self.participantIds = []
        self.contactId = None
        # Set up the widgets
        # for i in xrange(0, 6):
        #     self.ui.participantTabWidget.addTab(ParticipantWidget(), "Participant {0}".format(i+1))
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.dateOfBirthDateEdit.dateChanged.connect(self.dob_changed)
        self.ui.chooseContactBtn.clicked.connect(self.chooseContactBtn_clicked)
        self.ui.createContactBtn.clicked.connect(self.createContactBtn_clicked)
        self.ui.clearContactBtn.clicked.connect(self.clearContactBtn_clicked)
        self.ui.calculateAverageAgeBtn.clicked.connect(self.calculateAverageAgeBtn_clicked)

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
        # self.participantIds = []
        self.ui.groupNameLineEdit.clear()
        self.ui.numberParticipantsLineEdit.clear()
        self.ui.averageAgeLineEdit.clear()
        self.ui.contactPersonLineEdit.clear()
        self.contactId = None
        self.ui.participantsTextEdit.clear()
        self.ui.timeConstraintsGroupBox.setChecked(False)

    def dobValid(self):
        """checks if the date of birth is valid given the age"""
        dob = self.ui.dateOfBirthDateEdit.date()
        compareDate = QDate(QDate.currentDate().year(), 1, 1)
        age = int(dob.daysTo(compareDate) / 365)
        return age == int(self.ui.ageSpinBox.value())

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
        schoolAttending = str(self.ui.schoolAttendingLineEdit.text()).strip()
        schoolAttending = sanitize(schoolAttending)
        parent = str(self.ui.parentLineEdit.text()).strip()
        parent = sanitize(parent)
        # Don't need to sanitize this one, it can only be a number
        age = str(self.ui.ageSpinBox.value())
        schoolGrade = str(self.ui.schoolGradeLineEdit.text()).strip()
        schoolGrade = sanitize(schoolGrade)

        groupName = str(self.ui.groupNameLineEdit.text()).strip()
        groupName = sanitize(groupName)
        numberParticipants = str(self.ui.numberParticipantsLineEdit.text()).strip()
        numberParticipants = sanitize(numberParticipants)
        averageAge = str(self.ui.averageAgeLineEdit.text()).strip()
        averageAge = sanitize(averageAge)
        # for i in xrange(self.ui.participantTabWidget.count()):
        #     participantWidget = self.ui.participantTabWidget.widget(i)
        #     if participantWidget.participantId is not None:
        #         self.participantIds.append(participantWidget.participantId)
        # participants = ','.join(self.participantIds)
        participants = str(self.ui.participantsTextEdit.toPlainText()).strip()
        participants = sanitize(participants)
        earliestPerformanceTime = ""
        latestPerformanceTime = ""
        if self.ui.timeConstraintsGroupBox.isChecked():
            earliestPerformanceTime = str(self.ui.earliestPerformanceTimeTimeEdit.time().toString("HH:mm"))
            latestPerformanceTime = str(self.ui.latestPerformanceTimeTimeEdit.time().toString("HH:mm"))

        # Check if dob is valid relative to age
        # if not, we won't save dob
        if not self.dobValid():
            dob = ""

        # Check for empty fields
        # if first is None or first == "":
        #     QMessageBox.warning(self, 'Missing Field', 'Participant must have a First Name', QMessageBox.Ok)
        #     return

        # if last is None or last == "":
        #     QMessageBox.warning(self, 'Missing Field', 'Participant must have a Last Name', QMessageBox.Ok)
        #     return

        # if dob is None or dob == "1900-01-01":
        #     QMessageBox.warning(self, 'Missing Field', 'Participant must have a Date of Birth', QMessageBox.Ok)
        #     return

        # if email is None or email == "":
        #     if QMessageBox.question(self, 'Missing Email', 'Are you sure you want to leave Email blank?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
        #         return
        # Check for valid fields
        # if (email is not None or email != "") and validEmail(email) == False:
        #     QMessageBox.warning(self, 'Invalid Email', email + ' is not a valid email format', QMessageBox.Ok)
        #     return

        # if (first is not None or first != "") and validateName(first) == False:
        #     if QMessageBox.question(self, 'Validate First Name', 'Are you sure \'' + first + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
        #         return

        # if (last is not None or last != "") and validateName(last) == False:
        #     if QMessageBox.question(self, 'Validate Last Name', 'Are you sure \'' + last + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
        #         return

        if numberParticipants != "" and not numberParticipants.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Number of Participants must be a number', QMessageBox.Ok)
            return

        if schoolGrade != "" and not schoolGrade.isalnum():
            QMessageBox.warning(self, 'Incorrect Field', 'School Grade must be only letters and numbers', QMessageBox.Ok)
            return

        if averageAge != "" and not averageAge.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Average Age must be a whole number', QMessageBox.Ok)
            return

        # Check for duplicated participants
        # pList = dbInteractionInstance.getParticipantsWithName(first=first, last=last)
        # print pList
        # if len(pList) > 0:
        #     s = ""
        #     for p in pList:
        #         print p
        #         s += "{0} {1}, born {2}\n".format(p.first, p.last, p.dob)

        #     if QMessageBox.question(self, 'Possible Duplicate',
        #         'This name exists in the database already:\n{0}\nDo you still want to add this person?'.format(s),
        #         QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
        #         return

        self.p = Participant(first, last, address, city, postal, home, cell, email, dob, schoolAttending, parent, age, schoolGrade, groupName, numberParticipants, averageAge, participants, self.contactId, earliestPerformanceTime, latestPerformanceTime)
        result = dbInteractionInstance.addParticipant(self.p)
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

    def chooseContactBtn_clicked(self):
        """opens Choose Teacher Dialog"""
        dialog = ChooseTeacherDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            self.contactId = dialog.getTeacherId()
            # Use the id to get the name for display
            t = dbInteractionInstance.getTeacherFromId(self.contactId)
            name = name = t.first + " " + t.last
            self.ui.contactPersonLineEdit.setText(name)

    def createContactBtn_clicked(self):
        """opens Add Teacher Dialog"""
        dialog = AddTeacherDialog(testing=self.testing, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            t = dialog.getTeacher()
            self.ui.teacherLineEdit.setText(t.first + ' ' + t.last)
            self.contactId = dbInteractionInstance.getLastTeacherId()

    def clearContactBtn_clicked(self):
        """Clears the contact field"""
        self.ui.contactPersonLineEdit.clear()
        self.contactId = None

    def calculateAverageAgeBtn_clicked(self):
        """Shows the average age calculator"""
        dialog = AverageAgeCalculatorDialog(self) # Note: "self" is very important, won't show otherwise
        dialog.show()
