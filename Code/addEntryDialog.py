import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QDialog, QMessageBox
import traceback
from ui_addEntryDialog import Ui_AddEntryDialog
from addSoloParticipantDialog import AddSoloParticipantDialog
from addGroupParticipantDialog import AddGroupParticipantDialog
from addTeacherDialog import AddTeacherDialog

class AddEntryDialog(QDialog):
    def __init__(self, parent=None, testing=False, conn=None):
        # Initialize object using ui_addEntry
        super(AddEntryDialog, self).__init__(parent)
        self.ui = Ui_AddEntryDialog()
        self.ui.setupUi(self)
        self.dance() # Slightly cheater way to start the ui properly
        # Initialize class variables
        self.testing = testing
        self.conn = conn
        self.disciplines = {'Dance' : self.dance,   # For Pythonic switch-case
                                'Piano' : self.piano,
                                'Choral' : self.choral,
                                'Vocal' : self.vocal,
                                'Instrumental' : self.instrumental,
                                'Band' : self.band,
                                'Speech' : self.speech
                            }
        # Make the buttons do things
        self.connectSlots()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addEntryBtn.clicked.connect(self.addEntryBtn_clicked)
        self.ui.cancelBtn.clicked.connect(self.cancelBtn_clicked)
        self.ui.createNewSoloParticipantBtn.clicked.connect(self.createNewSoloParticipantBtn_clicked)
        self.ui.createNewGroupParticipantBtn.clicked.connect(self.createNewGroupParticipantBtn_clicked)
        self.ui.createNewTeacherBtn.clicked.connect(self.createNewTeacherBtn_clicked)
        self.ui.disciplineComboBox.currentIndexChanged['QString'].connect(self.disciplineComboBox_changed)

    ### Slots ###

    def addEntryBtn_clicked(self):
        """handles the Add Entry button being clicked"""
        pass

    def cancelBtn_clicked(self):
        self.reject()

    def createNewSoloParticipantBtn_clicked(self):
        """opens Add Solo Participant Dialog"""
        dialog = AddSoloParticipantDialog(testing=self.testing)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            try:
                p.addToDB(self.conn)
                self.ui.participantLineEdit.setText(p.first + ' ' + p.last)
                # TODO get PK from db to attach new participant to this entry
                QMessageBox.information(self, 'Add Participant', 'Successfully added new participant', QMessageBox.Ok)
            except Exception, e:
                print traceback.format_exc()
                QMessageBox.critical(self, 'Add Participant', 'Failed to add new participant\n{0}'.format(e), QMessageBox.Ok)

    def createNewGroupParticipantBtn_clicked(self):
        """opens Add Group Participant Dialog"""
        dialog = AddGroupParticipantDialog(testing=self.testing)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            gp = dialog.getGroupParticipant()
            try:
                gp.addToDB(self.conn)
                self.ui.participantLineEdit.setText(gp.groupName)
                # TODO get PK from db to attach new participant to this entry
                QMessageBox.information(self, 'Add Group Participant', 'Successfully added new group participant', QMessageBox.Ok)
            except Exception, e:
                print traceback.format_exc()
                QMessageBox.critical(self, 'Add Group Participant', 'Failed to add new gorup participant\n{0}'.format(e), QMessageBox.Ok)

    def createNewTeacherBtn_clicked(self):
        """opens Add Teacher Dialog"""
        dialog = AddTeacherDialog(testing=self.testing)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            t = dialog.getTeacher()
            try:
                t.addToDB(self.conn)
                self.ui.teacherLineEdit.setText(t.first + ' ' + t.last)
                # TODO get PK from db to attach new teacher to this entry
                QMessageBox.information(self, 'Add Teacher', 'Successfully added new teacher', QMessageBox.Ok)
            except Exception, e:
                print traceback.format_exc()
                QMessageBox.critical(self, 'Add Teacher', 'Failed to add new teacher\n{0}'.format(e), QMessageBox.Ok)

    def disciplineComboBox_changed(self, text):
        """changes which fields are enabled based on the selected discipline"""
        if str(text) in self.disciplines:
            self.disciplines[str(text)]()
        else:
            QMessageBox.warning(self, 'Invalid Discipline', 'An invalid discipline was selected. Please try again.', QMessageBox.Ok)

    def dance(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
        self.ui.composerLabel.setEnabled(False)
        self.ui.composerLineEdit.setEnabled(False)
        self.ui.arrangerLabel.setEnabled(False)
        self.ui.arrangerLineEdit.setEnabled(False)
        self.ui.artistLabel.setEnabled(True)
        self.ui.artistLineEdit.setEnabled(True)
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

    def instrumental(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(True)
        self.ui.instrumentLineEdit.setEnabled(True)
        self.ui.composerLabel.setEnabled(True)
        self.ui.composerLineEdit.setEnabled(True)
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

    def band(self):
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