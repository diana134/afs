"""Dialog for choosing an existing Entry"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
import traceback
from PyQt4.QtGui import QDialog, QAbstractItemView, QMessageBox

from ui_chooseEntryDialog import Ui_ChooseEntryDialog
from databaseInteraction import dbInteractionInstance

class ChooseEntryDialog(QDialog):
    """Dialog for choosing an existing Entry"""
    def __init__(self, parent=None):
        super(ChooseEntryDialog, self).__init__(parent)
        self.ui = Ui_ChooseEntryDialog()
        self.ui.setupUi(self)
        self.ui.entryTableView.setModel(dbInteractionInstance.entryModel)
        self.ui.entryTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.entryTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Initialize class variables
        self.entryId = None
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    def getentryId(self):
        return self.entryId

    ### Slots ###

    def okBtn_clicked(self):
        """Get the Entry's id and return it"""
        # Get which tab we're on so we know which table to reference
        model = dbInteractionInstance.entryModel
        view = self.ui.entryTableView

        try:
            # Get which row in view is selected
            indexList = view.selectedIndexes() # gets all selected cells
            row = indexList[0].row()
            # Get column id is in
            column = model.fieldIndex("id")
            # Get QModelIndex of id
            modelIndex = [i for i in indexList if i.row() == row and i.column() == column][0]
            # Get id of selected Entry
            data = model.data(modelIndex)
            entryId = data.toString()
            # And store it for retrieval
            self.entryId = entryId

            # All done!
            self.accept()
        except Exception, e:
            print traceback.format_exc()
            QMessageBox.critical(self, 'Choose Entry', 'Error reading database\n{0}'.format(e), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
    