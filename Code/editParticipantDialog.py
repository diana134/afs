"""The dialog for editing a Participant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))

from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QDate, QTime

from ui_addParticipantDialog import Ui_AddParticipantDialog
from averageAgeCalculatorDialog import AverageAgeCalculatorDialog
from chooseTeacherDialog import ChooseTeacherDialog
from addTeacherDialog import AddTeacherDialog
from utilities import *
from databaseInteraction import dbInteractionInstance

class EditParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, participantId=None):
        # Initialize object using ui_addParticipant
        super(EditParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddParticipantDialog()
        self.ui.setupUi(self)

        # Initialize class variables
        self.testing = testing
        if participantId is None:
            QMessageBox.critical(self, 'Invalid Participant', "An invalid participant was chosen.", QMessageBox.Ok)
            self.reject()
        # if participantId[0] == 's':
        #     self.participantId = participantId[1:]
        # else:
        #     self.participantId = participantId
        self.participantId = participantId
        self.participant = dbInteractionInstance.getParticipantFromId(participantId)

        # Set up the contact
        self.contactId = self.participant.contact
        if self.contactId:
            c = dbInteractionInstance.getTeacherFromId(self.contactId)
            if c is not None:
                self.ui.contactPersonLineEdit.setText("{0} {1}".format(c.first, c.last))

        # Initialize ui with variables
        self.ui.addParticipantBtn.setText("&Update Participant")
        self.setWindowTitle("Edit Participant")
        self.ui.firstNameLineEdit.setText(self.participant.first)
        self.ui.lastNameLineEdit.setText(self.participant.last)
        self.ui.addressLineEdit.setText(self.participant.address)
        self.ui.cityLineEdit.setText(self.participant.city)
        self.ui.postalCodeLineEdit.setText(humanPostalCodeFormat(self.participant.postal))
        self.ui.homePhoneLineEdit.setText(humanPhoneNumberFormat(self.participant.home))
        self.ui.cellPhoneLineEdit.setText(humanPhoneNumberFormat(self.participant.cell))
        self.ui.emailLineEdit.setText(self.participant.email)
        self.ui.dateOfBirthDateEdit.setDate(QDate.fromString(self.participant.dob, "yyyy-MM-dd"))
        self.ui.ageLabel.setText("Age as of Jan. 1 {0}".format(QDate.currentDate().year()))
        self.ui.schoolAttendingLineEdit.setText(self.participant.schoolAttending)
        self.ui.parentLineEdit.setText(self.participant.parent)
        self.ui.schoolGradeLineEdit.setText(self.participant.schoolGrade)
        self.ui.groupNameLineEdit.setText(self.participant.groupName)
        self.ui.numberParticipantsLineEdit.setText(self.participant.numberParticipants)
        self.ui.schoolGradeLineEdit.setText(self.participant.schoolGrade)
        self.ui.averageAgeLineEdit.setText(self.participant.averageAge)
        if self.participant.earliestPerformanceTime != "":
            self.ui.timeConstraintsGroupBox.setChecked(True)
            self.ui.earliestPerformanceTimeTimeEdit.setTime(QTime.fromString(self.participant.earliestPerformanceTime, "h:mm A"))
            self.ui.latestPerformanceTimeTimeEdit.setTime(QTime.fromString(self.participant.latestPerformanceTime, "h:mm A"))
        self.ui.participantsTextEdit.setText(self.participant.participants)

        # Set the age display
        self.dob_changed()

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
        # Check for valid fields64
        if (email is not None or email != "") and validEmail(email) == False:
            QMessageBox.warning(self, 'Invalid Email', email + ' is not a valid email format', QMessageBox.Ok)
            return

        if (first is not None or first != "") and validateName(first) == False:
            if QMessageBox.question(self, 'Validate First Name', 'Are you sure \'' + first + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if (last is not None or last != "") and validateName(last) == False:
            if QMessageBox.question(self, 'Validate Last Name', 'Are you sure \'' + last + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if numberParticipants != "" and not numberParticipants.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Group Size must be a number', QMessageBox.Ok)
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

        self.participant.first = first
        self.participant.last = last
        self.participant.address = address
        self.participant.city = city
        self.participant.postal = postal
        self.participant.home = home
        self.participant.cell = cell
        self.participant.email = email
        self.participant.dob = dob
        self.participant.schoolAttending = schoolAttending
        self.participant.parent = parent
        self.participant.age = age
        self.participant.schoolGrade = schoolGrade
        self.participant.groupName = groupName
        self.participant.numberParticipants = numberParticipants
        self.participant.averageAge = averageAge
        self.participant.participants = participants
        self.participant.contact = self.contactId
        self.participant.earliestPerformanceTime = earliestPerformanceTime
        self.participant.latestPerformanceTime = latestPerformanceTime
        result = dbInteractionInstance.updateParticipant(self.participantId, self.participant)
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
        dialog = AverageAgeCalculatorDialog(self)  # Note: "self" is very important, won't show otherwise
        dialog.show()
