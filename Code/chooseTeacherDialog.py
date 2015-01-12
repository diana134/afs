"""Dialog for choosing an existing Teacher"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
import traceback
from PyQt4.QtGui import QDialog, QAbstractItemView, QMessageBox

from ui_chooseTeacherDialog import Ui_ChooseTeacherDialog
from databaseInteraction import dbInteractionInstance

class ChooseTeacherDialog(QDialog):
    """Dialog for choosing an existing Teacher"""
    def __init__(self, parent=None):
        super(ChooseTeacherDialog, self).__init__(parent)
        self.ui = Ui_ChooseTeacherDialog()
        self.ui.setupUi(self)
        self.ui.teacherTableView.setModel(dbInteractionInstance.teacherModel)
        self.ui.teacherTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.teacherTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.teacherTableView.hideColumn(0)
        # Initialize class variables
        self.teacherId = None
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)

    def getTeacherId(self):
        return self.teacherId

    ### Slots ###

    def okBtn_clicked(self):
        """Get the Teacher's id and return it"""
        # Get which tab we're on so we know which table to reference
        model = dbInteractionInstance.teacherModel
        view = self.ui.teacherTableView

        try:
            # Get which row in view is selected
            indexList = view.selectedIndexes() # gets all selected cells
            row = indexList[0].row()
            # Get column id is in
            column = model.fieldIndex("id")
            # Get QModelIndex of id
            modelIndex = [i for i in indexList if i.row() == row and i.column() == column][0]
            # Get id of selected Teacher
            data = model.data(modelIndex)
            teacherId = data.toString()
            # And store it for retrieval
            self.teacherId = teacherId

            # All done!
            self.accept()
        except Exception, e:
            print traceback.format_exc()
            QMessageBox.critical(self, 'Choose Teacher', 'Error reading database\n{0}'.format(e), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()
    