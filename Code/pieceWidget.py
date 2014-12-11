"""The widget for adding a Piece to an Entry"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QTime

from ui_pieceWidget import Ui_PieceWidget
from utilities import sanitize

class PieceWidget(QWidget):
    def __init__(self, parent=None):
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

    def clearFields(self):
        """Clears and resets the fields"""
        self.ui.titleLineEdit.clear()
        self.ui.composerLineEdit.clear()
        self.ui.arrangerLineEdit.clear()
        self.ui.artistLineEdit.clear()
        self.ui.authorLineEdit.clear()
        self.ui.opusLineEdit.clear()
        self.ui.movementLineEdit.clear()
        self.ui.noLineEdit.clear()
        self.ui.performanceTimeEdit.setTime(QTime(0, 0, 0))

    def getFields(self):
        """Returns a dictionary of all the fields, stripped and sanitized"""
        fields = {}
        fields['title'] = str(self.ui.titleLineEdit.text()).strip()
        fields['title'] = sanitize(fields['title'])
        fields['composer'] = str(self.ui.composerLineEdit.text()).strip()
        fields['composer'] = sanitize(fields['composer'])
        fields['arranger'] = str(self.ui.arrangerLineEdit.text()).strip()
        fields['arranger'] = sanitize(fields['arranger'])
        fields['artist'] = str(self.ui.artistLineEdit.text()).strip()
        fields['artist'] = sanitize(fields['artist'])
        fields['author'] = str(self.ui.authorLineEdit.text()).strip()
        fields['author'] = sanitize(fields['author'])
        fields['opus'] = str(self.ui.opusLineEdit.text()).strip()
        fields['opus'] = sanitize(fields['opus'])
        fields['no'] = str(self.ui.noLineEdit.text()).strip()
        fields['no'] = sanitize(fields['no'])
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
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.arrangerLineEdit.clear()
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def piano(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.arrangerLineEdit.clear()
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(True)
        self.ui.opusLineEdit.setEnabled(True)
        self.ui.noLabel.setEnabled(True)
        self.ui.noLineEdit.setEnabled(True)
        self.ui.movementLabel.setEnabled(True)
        self.ui.movementLineEdit.setEnabled(True)

    def choral(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def vocal(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def instrumental(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def band(self):
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.authorLineEdit.clear()
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()

    def speech(self):
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.composerLineEdit.clear()
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.arrangerLineEdit.clear()
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.artistLineEdit.clear()
        self.ui.authorLabel.setEnabled(True)
        self.ui.authorLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.opusLineEdit.clear()
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.noLineEdit.clear()
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
        self.ui.movementLineEdit.clear()
