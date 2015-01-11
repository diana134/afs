"""The widget for adding a Participant to an Group"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QWidget

from ui_participantWidget import Ui_ParticipantWidget
from addSoloParticipantDialog import AddSoloParticipantDialog
from chooseParticipantDialog import ChooseParticipantDialog
from databaseInteraction import dbInteractionInstance

class ParticipantWidget(QWidget):
    def __init__(self, parent=None, participantId=None):
        # Initialize object
        super(ParticipantWidget, self).__init__(parent)
        self.ui = Ui_ParticipantWidget()
        self.ui.setupUi(self)
        # Initialize class variables
        self.participantId = participantId
        if self.participantId is not None:
            self.setParticipant()
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.chooseParticipantBtn.clicked.connect(self.chooseParticipantBtn_clicked)
        self.ui.createNewParticipantBtn.clicked.connect(self.createNewParticipantBtn_clicked)

    def clearFields(self):
        self.ui.participantLineEdit.clear()
        self.participantId = None

    def setParticipant(self):
        """sets all the stuff related to self.participantId"""
        # Use the id to get the name for display
        p = dbInteractionInstance.getParticipantFromId(self.participantId)
        name = ""
        # Deal with it whether it's a solo or group
        try:
            name = p.first + " " + p.last
        except AttributeError:
            name = p.groupName
        self.ui.participantLineEdit.setText(name)

#####Slots#####

    def chooseParticipantBtn_clicked(self):
        """opens Choose Participant Dialog"""
        dialog = ChooseParticipantDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            self.participantId = dialog.getParticipantId()
            # Use the id to get the name for display
            p = dbInteractionInstance.getParticipantFromId(self.participantId)
            name = ""
            # Deal with it whether it's a solo or group
            try:
                name = p.first + " " + p.last
            except AttributeError:
                name = p.groupName
            self.ui.participantLineEdit.setText(name)

    def createNewParticipantBtn_clicked(self):
        """opens Add Solo Participant Dialog"""
        dialog = AddSoloParticipantDialog(closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            self.ui.participantLineEdit.setText(p.first + ' ' + p.last)
            self.participantId = dbInteractionInstance.getLastSoloParticipantId()
