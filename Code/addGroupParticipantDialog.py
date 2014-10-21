"""The form for adding a new GroupParticipant"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox

from ui_addGroupParticipantDialog import Ui_AddGroupParticipantDialog
from addSoloParticipantDialog import AddSoloParticipantDialog
from chooseParticipantDialog import ChooseParticipantDialog
from participant import GroupParticipant
from utilities import sanitize, validateName

class AddGroupParticipantDialog(QDialog):
    def __init__(self, parent=None, testing=False, db=None, closeAfterAdd=False):
        # Initialize object using ui_addGroupParticipant
        super(AddGroupParticipantDialog, self).__init__(parent)
        self.ui = Ui_AddGroupParticipantDialog()
        self.ui.setupUi(self)
        # Initialize class variables
        self.testing = testing
        self.db = db
        self.closeAfterAdd = closeAfterAdd
        self.gp = None
        self.participantIds = []
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

    def getGroupParticipant(self):
        """returns the Participant object created from user data"""
        return self.gp

    def clearFields(self):
        """Clears and resets all fields"""
        self.ui.groupNameLineEdit.clear()
        self.ui.groupSizeLineEdit.clear()
        self.ui.schoolGradeLineEdit.clear()
        self.ui.averageAgeLineEdit.clear()
        self.ui.p1LineEdit.clear()
        self.ui.p2LineEdit.clear()
        self.ui.p3LineEdit.clear()
        self.ui.p4LineEdit.clear()

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
        # Check for valid fields
        elif validateName(groupName) == False and QMessageBox.question(self, 'Validate Group Name', 'Are you sure \'' + groupName + '\' is correct?', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            # Stop here
            pass
        elif groupSize != "" and not groupSize.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Group Size must be a number', QMessageBox.Ok)
        elif schoolGrade != "" and not schoolGrade.isalphanumeric():
            QMessageBox.warning(self, 'Incorrect Field', 'School Grade must be only letters and numbers', QMessageBox.Ok)
        elif averageAge != "" and not averageAge.isdigit():
            QMessageBox.warning(self, 'Incorrect Field', 'Average Age must be a whole number', QMessageBox.Ok)
        else:
            self.gp = GroupParticipant(groupName, groupSize, schoolGrade, averageAge, participants)
            result = self.gp.addToDB(self.db)
            if result == "":
                QMessageBox.information(self, 'Add Group Participant', 'Successfully added new group participant', QMessageBox.Ok)
                self.clearFields()
                if self.closeAfterAdd:
                    self.accept()

    def cancelBtn_clicked(self):
        self.reject()

    def chooseBtn_clicked(self, lineToFill):
        """opens Choose Participant Dialog"""
        dialog = ChooseParticipantDialog(self.db.soloParticipantModel)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            pId = dialog.getParticipantId()
            self.participantIds.append(pId)
            # Use the id to get the name for display
            p = self.db.getParticipantFromId(pId)
            name = p.first + " " + p.last
            lineToFill.setText(name)

    def createNewBtn_clicked(self, lineToFill):
        """opens Add Solo Participant Dialog"""
        dialog = AddSoloParticipantDialog(testing=self.testing, db=self.db, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            lineToFill.setText(p.first + ' ' + p.last)
            self.participantId.append(self.db.getLastSoloParticipantId())

    def chooseP1Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p1LineEdit)

    def chooseP2Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p2LineEdit)

    def chooseP3Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p3LineEdit)

    def chooseP4Btn_clicked(self):
        """opens Choose Participant Dialog"""
        self.chooseBtn_clicked(self.ui.p4LineEdit)

    def createNewP1Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p1LineEdit)

    def createNewP2Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p2LineEdit)

    def createNewP3Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p3LineEdit)

    def createNewP4Btn_clicked(self):
        """opens Add Solo Participant Dialog"""
        self.createNewBtn_clicked(self.ui.p4LineEdit)
