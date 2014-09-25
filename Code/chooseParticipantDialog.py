"""Dialog for choosing an existing Participant"""

import sys
sys.path.insert(0, '../Forms/')
import traceback
from PyQt4.QtGui import QDialog, QAbstractItemView, QMessageBox
# from PyQt4.QtCore import QModelIndex

from ui_chooseParticipantDialog import Ui_ChooseParticipantDialog

class ChooseParticipantDialog(QDialog):
    """Dialog for choosing an existing Participant"""
    def __init__(self, soloParticipantModel, groupParticipantModel, parent=None):
        super(ChooseParticipantDialog, self).__init__(parent)
        self.ui = Ui_ChooseParticipantDialog()
        self.ui.setupUi(self)
        self.ui.soloParticipantTableView.setModel(soloParticipantModel)
        self.ui.soloParticipantTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.soloParticipantTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.groupParticipantTableView.setModel(groupParticipantModel)
        self.ui.groupParticipantTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.groupParticipantTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Initialize class variables
        self.soloParticipantModel = soloParticipantModel
        self.groupParticipantModel = groupParticipantModel
        self.participantId = -1
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    def getParticipantId(self):
        return self.participantId

    ### Slots ###

    def okBtn_clicked(self):
        """Get the Participant's id and return it"""
        # Get which tab we're on so we know which table to reference
        model = None
        view = None
        prefix = None

        if self.ui.participantTypeTabWidget.currentIndex() == 0:
            # Do Solo Participant stuff
            model = self.soloParticipantModel
            view = self.ui.soloParticipantTableView
            prefix = "s"
        else:
            # Do Group Participant stuff
            model = self.groupParticipantModel
            view = self.ui.groupParticipantTableView
            prefix = "g"

        try:
            # Get which row in view is selected
            indexList = view.selectedIndexes() # gets all selected cells
            row = indexList[0].row()
            # Get column id is in
            column = model.fieldIndex("id")
            # Get QModelIndex of id
            modelIndex = [i for i in indexList if i.row() == row and i.column() == column][0]
            # Get id of selected participant
            data = model.data(modelIndex)
            participantId = data.toString()
            # Add appropriate prefix (so we know which table the index is from)
            participantId = prefix + participantId
            # And store it for retrieval
            self.participantId = participantId

            # All done!
            self.accept()
        except Exception, e:
            print traceback.format_exc()
            QMessageBox.critical(self, 'Choose Participant', 'Error reading database\n{0}'.format(e), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
    