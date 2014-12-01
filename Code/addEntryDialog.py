"""The dialog for adding an Entry"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox
from PyQt4.QtCore import QTime

from ui_addEntryDialog import Ui_AddEntryDialog
from addSoloParticipantDialog import AddSoloParticipantDialog
from addGroupParticipantDialog import AddGroupParticipantDialog
from addTeacherDialog import AddTeacherDialog
from chooseParticipantDialog import ChooseParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from pieceWidget import PieceWidget
from entry import Entry
from utilities import sanitize
from databaseInteraction import dbInteractionInstance

class AddEntryDialog(QDialog):
    def __init__(self, parent=None, testing=False, closeAfterAdd=False):
        # Initialize object using ui_addEntry
        super(AddEntryDialog, self).__init__(parent)
        self.ui = Ui_AddEntryDialog()
        self.ui.setupUi(self)
        self.dance() # Slightly cheater way to start the ui properly
        # HACK Make the PieceWidget in the first tab work right
        self.ui.tabWidget.removeTab(0)
        self.ui.tabWidget.addTab(PieceWidget(), "Piece 1")
        # Initialize class variables
        self.testing = testing
        self.closeAfterAdd = closeAfterAdd
        self.entry = None
        self.participantId = None
        self.teacherId = None
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
        self.ui.chooseParticipantBtn.clicked.connect(self.chooseParticipantBtn_clicked)
        self.ui.chooseTeacherBtn.clicked.connect(self.chooseTeacherBtn_clicked)
        self.ui.createNewSoloParticipantBtn.clicked.connect(self.createNewSoloParticipantBtn_clicked)
        self.ui.createNewGroupParticipantBtn.clicked.connect(self.createNewGroupParticipantBtn_clicked)
        self.ui.createNewTeacherBtn.clicked.connect(self.createNewTeacherBtn_clicked)
        self.ui.disciplineComboBox.currentIndexChanged['QString'].connect(self.disciplineComboBox_changed)
        self.ui.addPieceBtn.clicked.connect(self.addPieceBtn_clicked)
        self.ui.tabWidget.tabCloseRequested['int'].connect(self.closeTab)

    def getEntry(self):
        return self.entry

    def clearFields(self):
        self.ui.levelLineEdit.clear()
        self.ui.classNumberLineEdit.clear()
        self.ui.classNameLineEdit.clear()
        self.ui.styleLineEdit.clear()
        self.ui.instrumentLineEdit.clear()

    ### Slots ###

    def addEntryBtn_clicked(self):
        """handles the Add Entry button being clicked"""
        participantID = self.participantId
        teacherID = self.teacherId
        discipline = str(self.ui.disciplineComboBox.currentText()).strip()
        level = str(self.ui.levelLineEdit.text()).strip()
        level = sanitize(level)
        classNumber = str(self.ui.classNumberLineEdit.text()).strip()
        classNumber = sanitize(classNumber)
        className = str(self.ui.classNameLineEdit.text()).strip()
        className = sanitize(className)
        style = str(self.ui.styleLineEdit.text()).strip()
        style = sanitize(style)
        instrument = str(self.ui.instrumentLineEdit.text()).strip()
        instrument = sanitize(instrument)
        title = str(self.ui.titleLineEdit.text()).strip()
        title = sanitize(title)
        composer = str(self.ui.composerLineEdit.text()).strip()
        composer = sanitize(composer)
        arranger = str(self.ui.arrangerLineEdit.text()).strip()
        arranger = sanitize(arranger)
        artist = str(self.ui.artistLineEdit.text()).strip()
        artist = sanitize(artist)
        author = str(self.ui.authorLineEdit.text()).strip()
        author = sanitize(author)
        opus = str(self.ui.opusLineEdit.text()).strip()
        opus = sanitize(opus)
        no = str(self.ui.noLineEdit.text()).strip()
        no = sanitize(no)
        movement = str(self.ui.movementLineEdit.text()).strip()
        movement = sanitize(movement)
        # Don't need to sanitize a timeEdit
        performanceTime = str(self.ui.performanceTimeEdit.time().toString("m:ss"))

        # Check for empty fields
        if participantID is None or participantID == "":
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Participant', QMessageBox.Ok)
        elif teacherID is None or teacherID == "":
            # TODO how to handle this for disciplines that don't usually have teachers? (speech)
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Teacher', QMessageBox.Ok)
        elif discipline is None or discipline == "":
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Discipline', QMessageBox.Ok)
        elif classNumber is None or classNumber == "":
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Class Number', QMessageBox.Ok)
        elif className is None or className == "":
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Class Name', QMessageBox.Ok)
        elif title is None or title == "":
            QMessageBox.warning(self, 'Missing Field', 'Entry must have a Title', QMessageBox.Ok)
        # Check for valid fields
        elif performanceTime == "0:00" and QMessageBox.question(self, 'Validate Performance Time', 'Are you sure you want to leave performance time blank? This could cause the scheduling algorithm to make poor choices.', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            # Stop here
            pass
        else:
            self.entry = Entry(participantID, teacherID, discipline, level, classNumber, className, title, performanceTime, style, composer, opus, no, movement, arranger, artist, instrument, author)
            result = dbInteractionInstance.addEntry(self.entry)
            if result == "":
                QMessageBox.information(self, 'Add Entry', 'Successfully added new entry', QMessageBox.Ok)
                self.clearFields()
                if self.closeAfterAdd:
                    self.accept()
            else:
                QMessageBox.critical(self, 'Add Entry', 'Failed to add new entry\n{0}'.format(result), QMessageBox.Ok)

    def cancelBtn_clicked(self):
        self.reject()

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

    def chooseTeacherBtn_clicked(self):
        """opens Choose Teacher Dialog"""
        dialog = ChooseTeacherDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            self.teacherId = dialog.getTeacherId()
            # Use the id to get the name for display
            t = dbInteractionInstance.getTeacherFromId(self.teacherId)
            name = name = t.first + " " + t.last
            self.ui.teacherLineEdit.setText(name)

    def createNewSoloParticipantBtn_clicked(self):
        """opens Add Solo Participant Dialog"""
        dialog = AddSoloParticipantDialog(testing=self.testing, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            self.ui.participantLineEdit.setText(p.first + ' ' + p.last)
            self.participantId = dbInteractionInstance.getLastSoloParticipantId()

    def createNewGroupParticipantBtn_clicked(self):
        """opens Add Group Participant Dialog"""
        dialog = AddGroupParticipantDialog(testing=self.testing, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            gp = dialog.getGroupParticipant()
            self.ui.participantLineEdit.setText(gp.groupName)
            self.participantId = dbInteractionInstance.getLastGroupParticipantId()

    def createNewTeacherBtn_clicked(self):
        """opens Add Teacher Dialog"""
        dialog = AddTeacherDialog(testing=self.testing, closeAfterAdd=True)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            t = dialog.getTeacher()
            self.ui.teacherLineEdit.setText(t.first + ' ' + t.last)
            self.teacherId = dbInteractionInstance.getLastTeacherId()

    def disciplineComboBox_changed(self, text):
        """changes which fields are enabled based on the selected discipline"""
        if str(text) in self.disciplines:
            self.disciplines[str(text)]()
            self.clearFields()
            for i in xrange(0, self.ui.tabWidget.count()):
                pieceWidget = self.ui.tabWidget.widget(i)
                pieceWidget.changeDiscipline(text)
            self.teacherId = ""
            self.ui.teacherLineEdit.clear()
        else:
            QMessageBox.critical(self, 'Invalid Discipline', 'An invalid discipline was selected. Please try again.', QMessageBox.Ok)

    def addPieceBtn_clicked(self):
        tabCount = self.ui.tabWidget.count()
        self.ui.tabWidget.addTab(PieceWidget(), "Piece {0}".format(tabCount+1))

    def closeTab(self, index):
        self.ui.tabWidget.removeTab(index)
        # rename tabs
        for i in xrange(0, self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabText(i, "Piece {0}".format(i+1))

    def dance(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)

    def piano(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)

    def choral(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)

    def vocal(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)

    def instrumental(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(True)
        self.ui.instrumentLineEdit.setEnabled(True)

    def band(self):
        self.ui.styleLabel.setEnabled(True)
        self.ui.styleLineEdit.setEnabled(True)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)

    def speech(self):
        self.ui.styleLabel.setEnabled(False)
        self.ui.styleLineEdit.setEnabled(False)
        self.ui.instrumentLabel.setEnabled(False)
        self.ui.instrumentLineEdit.setEnabled(False)
