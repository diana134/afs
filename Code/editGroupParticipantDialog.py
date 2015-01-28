"""The form for editing a GroupParticipant"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QTime

from ui_addGroupParticipantDialog import Ui_AddGroupParticipantDialog
# from addSoloParticipantDialog import AddSoloParticipantDialog
# from chooseParticipantDialog import ChooseParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from addTeacherDialog import AddTeacherDialog
from utilities import sanitize, validateName
from databaseInteraction import dbInteractionInstance
from participantWidget import ParticipantWidget

class EditGroupParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, participantId=None):
        # Initialize object using ui_addGroupParticipant
        super(EditGroupParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddGroupParticipantDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        if participantId is None:
            QMessageBox.critical(self, 'Invalid Participant', "An invalid participant was chosen.", QMessageBox.Ok)
            self.reject()
        if participantId[0] == 'g':
            self.participantId = participantId[1:]
        else:
            self.participantId = participantId
        self.participant = dbInteractionInstance.getParticipantFromId(participantId)
        if len(self.participant.participants) > 0:
            self.participantIds = self.participant.participants.split(',')
        else:
            self.participantIds = []
        self.contactId = self.participant.contact
        c = dbInteractionInstance.getTeacherFromId(self.contactId)
        if c is not None:
            self.ui.contactPersonLineEdit.setText("{0} {1}".format(c.first, c.last))

        # Initialize ui with variables
        self.ui.addParticipantBtn.setText("&Update Participant")
        self.setWindowTitle("Edit Participant")
        self.ui.groupNameLineEdit.setText(self.participant.groupName)
        self.ui.groupSizeLineEdit.setText(self.participant.groupSize)
        self.ui.schoolGradeLineEdit.setText(self.participant.schoolGrade)
        self.ui.averageAgeLineEdit.setText(self.participant.averageAge)
        if self.participant.earliestPerformanceTime != "":
            self.ui.timeConstraintsGroupBox.setChecked(True)
            self.ui.earliestPerformanceTimeTimeEdit.setTime(QTime.fromString(self.participant.earliestPerformanceTime, "h:mm A"))
            self.ui.latestPerformanceTimeTimeEdit.setTime(QTime.fromString(self.participant.latestPerformanceTime, "h:mm A"))

        for i in xrange(len(self.participantIds)):
            # participantWidget = self.ui.participantTabWidget.widget(i)
            # participantWidget.setParticipant(self.participantIds[i])
            self.ui.participantTabWidget.addTab(ParticipantWidget(participantId=self.participantIds[i]), "Participant {0}".format(i+1))

        if len(self.participantIds) < 6:
            for i in xrange(len(self.participantIds), 6):
                self.ui.participantTabWidget.addTab(ParticipantWidget(), "Participant {0}".format(i+1))

        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.chooseContactBtn.clicked.connect(self.chooseContactBtn_clicked)
        self.ui.createContactBtn.clicked.connect(self.createContactBtn_clicked)
        self.ui.clearContactBtn.clicked.connect(self.clearContactBtn_clicked)

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
        # if groupName is None or groupName == "":
        #     QMessageBox.warning(self, 'Missing Field', 'Participant must have a Group Name', QMessageBox.Ok)
        #     return

        # Check for valid fields
        # if validateName(groupName) == False:
        #     if QMessageBox.question(self, 'Validate Group Name', 'Are you sure \'' + groupName + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
        #         return

        if groupSize != "" and not groupSize.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Group Size must be a number', QMessageBox.Ok)
            return

        if schoolGrade != "" and not schoolGrade.isalnum():
            QMessageBox.warning(self, 'Incorrect Field', 'School Grade must be only letters and numbers', QMessageBox.Ok)
            return

        if averageAge != "" and not averageAge.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Average Age must be a whole number', QMessageBox.Ok)
            return

        # Check for duplicated participants only if the name has changed
        if groupName != self.participant.groupName:
            pList = dbInteractionInstance.getGroupParticipantsWithName(name=groupName)
            if len(pList) > 0:
                s = ""
                for p in pList:
                    s += "{0}, grade {1}\n".format(p.groupName, p.schoolGrade)

                if QMessageBox.question(self, 'Possible Duplicate', 
                    'This name exists in the database already:\n{0}\nDo you still want to update this group?'.format(s),
                    QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                    return

        self.participant.groupName = groupName
        self.participant.groupSize = groupSize
        self.participant.schoolGrade = schoolGrade
        self.participant.averageAge = averageAge
        self.participant.participants = participants
        self.participant.contact = self.contactId
        self.participant.earliestPerformanceTime = earliestPerformanceTime
        self.participant.latestPerformanceTime = latestPerformanceTime
        result = dbInteractionInstance.updateGroupParticipant(self.participantId, self.participant)
        if result == "":
            QMessageBox.information(self, 'Edit Group Participant', 'Successfully updated group participant', QMessageBox.Ok)
            self.accept()        
        else:
            QMessageBox.critical(self, 'Edit Group Participant', 'Failed to update group participant\n{0}'.format(result), QMessageBox.Ok)

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

    def clearContactBtn_clicked(self):
        """Clears the contact field"""
        self.ui.contactPersonLineEdit.clear()
        self.contactId = None
