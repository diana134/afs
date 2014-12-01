"""The widget for adding a Piece to an Entry"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QWidget, QMessageBox
from PyQt4.QtCore import QTime

from ui_pieceWidget import Ui_PieceWidget

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
        """Clears and resets the fields below Discipline"""
        self.ui.levelLineEdit.clear()
        self.ui.classNumberLineEdit.clear()
        self.ui.classNameLineEdit.clear()
        self.ui.styleLineEdit.clear()
        self.ui.instrumentLineEdit.clear()
        self.ui.titleLineEdit.clear()
        self.ui.composerLineEdit.clear()
        self.ui.arrangerLineEdit.clear()
        self.ui.artistLineEdit.clear()
        self.ui.authorLineEdit.clear()
        self.ui.opusLineEdit.clear()
        self.ui.movementLineEdit.clear()
        self.ui.noLineEdit.clear()
        self.ui.performanceTimeEdit.setTime(QTime(0, 0, 0))

    def changeDiscipline(self, text):
        """changes which fields are enabled based on the selected discipline"""
        if str(text) in self.disciplines:
            self.disciplines[str(text)]()
            self.clearFields()
        else:
            QMessageBox.critical(self, 'Invalid Discipline', 'An invalid discipline was selected. Please try again.', QMessageBox.Ok)


    def dance(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)

    def piano(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(True)
        self.ui.opusLineEdit.setEnabled(True)
        self.ui.noLabel.setEnabled(True)
        self.ui.noLineEdit.setEnabled(True)
        self.ui.movementLabel.setEnabled(True)
        self.ui.movementLineEdit.setEnabled(True)

    def choral(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)

    def vocal(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)

    def instrumental(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(True)
        self.ui.instrumentLineEdit.setEnabled(True)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)

    def band(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
        self.ui.arrangerLabel.setEnabled(True)
        self.ui.arrangerLineEdit.setEnabled(True)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(False)
        self.ui.authorLineEdit.setEnabled(False)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)

    def speech(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.artistLabel.setEnabled(False)
        self.ui.artistLineEdit.setEnabled(False)
        self.ui.authorLabel.setEnabled(True)
        self.ui.authorLineEdit.setEnabled(True)
        self.ui.opusLabel.setEnabled(False)
        self.ui.opusLineEdit.setEnabled(False)
        self.ui.noLabel.setEnabled(False)
        self.ui.noLineEdit.setEnabled(False)
        self.ui.movementLabel.setEnabled(False)
        self.ui.movementLineEdit.setEnabled(False)
