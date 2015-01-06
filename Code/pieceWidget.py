"""The widget for adding a Selection to an Entry"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QTime

from ui_pieceWidget import Ui_PieceWidget
from utilities import sanitize

class PieceWidget(QWidget):
    def __init__(self, parent=None, piece=None):
        # Initialize object
        super(PieceWidget, self).__init__(parent)
        self.ui = Ui_PieceWidget()
        self.ui.setupUi(self)
        self.dance() # Slightly cheater way to start the ui properly
        # Initialize class variables
        self.disciplines = {'Dance' : self.dance,   # For Pythonic switch-case
                                'Piano' : self.piano,
                                'Choral' : self.choral,
                                'Vocal' : self.vocal,
                                'Instrumental' : self.instrumental,
                                'Band' : self.band,
                                'Speech' : self.speech
                            }

        # Initialize ui if piece was given
        if piece is not None:
            self.ui.titleLineEdit.setText(piece['title'])
            self.ui.composerLineEdit.setText(piece['composerArranger'])
            self.ui.opusNoLineEdit.setText(piece['opusNo'])
            self.ui.movementLineEdit.setText(piece['movement'])
            time = piece['performanceTime']
            if len(piece['performanceTime']) < 5:
                # pad with leading 0 
                time = '0' + time
            self.ui.performanceTimeEdit.setTime(QTime.fromString(time, "mm:ss"))

    def clearFields(self):
        """Clears and resets the fields"""
        self.ui.titleLineEdit.clear()
        self.ui.composerLineEdit.clear()
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLineEdit.clear()
        self.ui.performanceTimeEdit.setTime(QTime(0, 0, 0))

    def getFields(self):
        """Returns a dictionary of all the fields, stripped and sanitized"""
        fields = {}
        fields['title'] = str(self.ui.titleLineEdit.text()).strip()
        fields['title'] = sanitize(fields['title'])
        fields['composerArranger'] = str(self.ui.composerLineEdit.text()).strip()
        fields['composerArranger'] = sanitize(fields['composerArranger'])
        fields['opusNo'] = str(self.ui.opusNoLineEdit.text()).strip()
        fields['opusNo'] = sanitize(fields['opusNo'])
        fields['movement'] = str(self.ui.movementLineEdit.text()).strip()
        fields['movement'] = sanitize(fields['movement'])
        # Don't need to sanitize a timeEdit
        fields['performanceTime'] = str(self.ui.performanceTimeEdit.time().toString("m:ss"))

        return fields

    def changeDiscipline(self, text):
        """changes which fields are enabled based on the selected discipline"""
        if str(text) in self.disciplines:
            self.disciplines[str(text)]()
            # self.clearFields()

    def dance(self):
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.composerLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def piano(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(True)
        self.ui.opusNoLineEdit.setEnabled(True)
        self.ui.movementLabel.setEnabled(True)
        self.ui.movementLineEdit.setEnabled(True)

    def choral(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def vocal(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def instrumental(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def band(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def speech(self):
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.composerLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusNoLineEdit.setEnabled(False)
        self.ui.opusNoLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()
