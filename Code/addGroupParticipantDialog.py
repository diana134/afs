import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog, QMessageBox
from ui_addGroupParticipantDialog import Ui_AddGroupParticipantDialog
import traceback
from participant import Participant, GroupParticipant

class AddGroupParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False):
        # Initialize object using ui_addGroupParticipant
        super(AddGroupParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddGroupParticipantDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        self.gp = None
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)

    def getGroupParticipant(self):
        """returns the Participant object created from user data"""
        return self.gp

    ### Slots ###

    def addParticipantBtn_clicked(self):
        """handles the Add Participant button being clicked"""
        groupName = self.ui.groupNameLineEdit.text()
        groupSize = self.ui.groupSizeLineEdit.text()
        schoolGrade = self.ui.schoolGradeLineEdit.text()
        averageAge = self.ui.averageAgeLineEdit.text()
        participants = self.ui.participantsLineEdit.text()
        
        # Error checking
        # TODO: set focus to incorrect field
        if groupName is None or groupName == "":
            QMessageBox.warning(self, 'Missing Field', 'Participant must have a Group Name', QMessageBox.Ok)
        else:
            self.gp = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants)
            self.accept()

    def cancelBtn_clicked(self):
        self.reject()