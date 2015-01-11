"""The form for adding a new GroupParticipant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QMessageBox

from ui_addGroupParticipantDialog import Ui_AddGroupParticipantDialog
# from addSoloParticipantDialog import AddSoloParticipantDialog
# from chooseParticipantDialog import ChooseParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from addTeacherDialog import AddTeacherDialog
from participantWidget import ParticipantWidget
from participant import GroupParticipant
from utilities import sanitize, validateName
from databaseInteraction import dbInteractionInstance

class AddGroupParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, closeAfterAdd=False):
        # Initialize object using ui_addGroupParticipant
        super(AddGroupParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddGroupParticipantDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        self.closeAfterAdd = closeAfterAdd
        self.gp = None
        self.participantIds = []
        self.contactId = None
        # Set up the widgets
        for i in xrange(0, 6):
            self.ui.participantTabWidget.addTab(ParticipantWidget(), "Participant {0}".format(i+1))
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.chooseContactBtn.clicked.connect(self.chooseContactBtn_clicked)
        self.ui.createContactBtn.clicked.connect(self.createContactBtn_clicked)

    def getGroupParticipant(self):
        """returns the Participant object created from user data"""
        return self.gp

    def clearFields(self):
        """Clears and resets all fields"""
        self.participantIds = []
        self.ui.groupNameLineEdit.clear()
        self.ui.groupSizeLineEdit.clear()
        self.ui.schoolGradeLineEdit.clear()
        self.ui.averageAgeLineEdit.clear()
        self.ui.contactPersonLineEdit.clear()
        self.contactId = None
        for i in xrange(self.ui.participantTabWidget.count()):
            participantWidget = self.ui.participantTabWidget.widget(i)
            participantWidget.clearFields()

    ### Slots ###

    def addParticipantBtn_clicked(self):
        """handles the Add Participant button being clicked"""
        groupName = str(self.ui.groupNameLineEdit.text()).strip()
        groupName = sanitize(groupName)
        groupSize = str(self.ui.groupSizeLineEdit.text()).strip()
        groupSize = sanitize(groupSize)
        schoolGrade = str(self.ui.schoolGradeLineEdit.text()).strip()
        schoolGrade = sanitize(schoolGrade)
        averageAge = str(self.ui.averageAgeLineEdit.text()).strip()
        averageAge = sanitize(averageAge)
        for i in xrange(self.ui.participantTabWidget.count()):
            participantWidget = self.ui.participantTabWidget.widget(i)
            if participantWidget.participantId is not None:
                self.participantIds.append(participantWidget.participantId)
        participants = ','.join(self.participantIds)
        earliestPerformanceTime = ""
        latestPerformanceTime = ""
        if self.ui.timeConstraintsGroupBox.isChecked():
            earliestPerformanceTime = str(self.ui.earliestPerformanceTimeTimeEdit.time().toString("HH:mm"))
            latestPerformanceTime = str(self.ui.latestPerformanceTimeTimeEdit.time().toString("HH:mm"))
        
        # Check for empty fields
        if groupName is None or groupName == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Group Name', QMessageBox.Ok)
            return

        # Check for valid fields
        if validateName(groupName) == False:
            if QMessageBox.question(self, 'Validate Group Name', 'Are you sure \'' + groupName + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        if groupSize != "" and not groupSize.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Group Size must be a number', QMessageBox.Ok)
            return

        if schoolGrade != "" and not schoolGrade.isalnum():
            QMessageBox.warning(self, 'Incorrect Field', 'School Grade must be only letters and numbers', QMessageBox.Ok)
            return

        if averageAge != "" and not averageAge.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Average Age must be a whole number', QMessageBox.Ok)
            return

        # Check for duplicated participants
        pList = dbInteractionInstance.getGroupParticipantsWithName(name=groupName)
        if len(pList) > 0:
            s = ""
            for p in pList:
                s += "{0}, grade {1}\n".format(p.groupName, p.schoolGrade)

            if QMessageBox.question(self, 'Possible Duplicate', 
                'This name exists in the database already:\n{0}\nDo you still want to add this group?'.format(s),
                QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                return

        self.gp = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants, self.contactId, earliestPerformanceTime, latestPerformanceTime)
        result = dbInteractionInstance.addGroupParticipant(self.gp)
        if result == "":
            QMessageBox.information(self, 'Add Group Participant', 'Successfully added new group participant', QMessageBox.Ok)
            self.clearFields()
            if self.closeAfterAdd:
                self.accept()

    def cancelBtn_clicked(self):
        self.reject()

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
