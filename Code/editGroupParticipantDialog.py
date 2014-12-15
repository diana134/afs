"""The form for adding a new GroupParticipant"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox

from ui_addGroupParticipantDialog import Ui_AddGroupParticipantDialog
from addSoloParticipantDialog import AddSoloParticipantDialog
from chooseParticipantDialog import ChooseParticipantDialog
from participant import GroupParticipant
from utilities import sanitize, validateName
from databaseInteraction import dbInteractionInstance

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
        self.participantIds = self.participant.participants.split(',')

        # Initialize ui with variables
        self.ui.addParticipantBtn.setText("&Update Participant")
        self.setWindowTitle("Edit Participant")
        self.ui.groupNameLineEdit.setText(self.participant.groupName)
        self.ui.groupSizeLineEdit.setText(self.participant.groupSize)
        self.ui.schoolGradeLineEdit.setText(self.participant.schoolGrade)
        self.ui.averageAgeLineEdit.setText(self.participant.averageAge)
        if len(self.participantIds) >= 1:
            p = dbInteractionInstance.getParticipantFromId(self.participantIds[0])
            self.ui.p1LineEdit.setText("{0} {1}".format(p.first, p.last))
        if len(self.participantIds) >= 2:
            p = dbInteractionInstance.getParticipantFromId(self.participantIds[1])
            self.ui.p2LineEdit.setText("{0} {1}".format(p.first, p.last))
        if len(self.participantIds) >= 3:
            p = dbInteractionInstance.getParticipantFromId(self.participantIds[2])
            self.ui.p3LineEdit.setText("{0} {1}".format(p.first, p.last))
        if len(self.participantIds) >= 4:
            p = dbInteractionInstance.getParticipantFromId(self.participantIds[3])
            self.ui.p4LineEdit.setText("{0} {1}".format(p.first, p.last))

        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.chooseP1Btn.clicked.connect(self.chooseP1Btn_clicked)
        self.ui.chooseP2Btn.clicked.connect(self.chooseP2Btn_clicked)
        self.ui.chooseP3Btn.clicked.connect(self.chooseP3Btn_clicked)
        self.ui.chooseP4Btn.clicked.connect(self.chooseP4Btn_clicked)
        self.ui.createNewP1Btn.clicked.connect(self.createNewP1Btn_clicked)
        self.ui.createNewP2Btn.clicked.connect(self.createNewP2Btn_clicked)
        self.ui.createNewP3Btn.clicked.connect(self.createNewP3Btn_clicked)
        self.ui.createNewP4Btn.clicked.connect(self.createNewP4Btn_clicked)

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
        participants = ','.join(self.participantIds)
        
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

        self.participant.groupName = groupName
        self.participant.groupSize = groupSize
        self.participant.schoolGrade = schoolGrade
        self.participant.averageAge = averageAge
        self.participant.participants = participants
        result = dbInteractionInstance.updateGroupParticipant(self.participantId, self.participant)
        if result == "":
            QMessageBox.information(self, 'Edit Group Participant', 'Successfully updated group participant', QMessageBox.Ok)
            self.accept()        
        else:
            QMessageBox.critical(self, 'Edit Group Participant', 'Failed to update group participant\n{0}'.format(result), QMessageBox.Ok)


    def cancelBtn_clicked(self):
        self.reject()

    def chooseBtn_clicked(self, lineToFill, position):
        """opens Choose Participant Dialog"""
        dialog = ChooseParticipantDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            pId = dialog.getParticipantId()
            if pId not in self.participantIds:
                self.participantIds[position] = pId
                
                # Use the id to get the name for display
                p = dbInteractionInstance.getParticipantFromId(pId)
                name = p.first + " " + p.last
                lineToFill.setText(name)
            else:
                QMessageBox.warning(self, 'Choose Participant', 'That participant has already been chosen.', QMessageBox.Ok)

    def createNewBtn_clicked(self, lineToFill, position):
        """opens Add Solo Participant Dialog"""
        dialog = AddSoloParticipantDialog(testing=self.testing, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            lineToFill.setText(p.first + ' ' + p.last)
            self.participantIds[position] = dbInteractionInstance.getLastSoloParticipantId()

    def chooseP1Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p1LineEdit, 0)

    def chooseP2Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p2LineEdit, 1)

    def chooseP3Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p3LineEdit, 2)

    def chooseP4Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p4LineEdit, 3)

    def createNewP1Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p1LineEdit, 0)

    def createNewP2Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p2LineEdit, 1)

    def createNewP3Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p3LineEdit, 2)

    def createNewP4Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p4LineEdit, 3)
