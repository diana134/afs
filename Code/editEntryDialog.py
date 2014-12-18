"""The dialog for editing an Entry"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QMessageBox

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

class EditEntryDialog(QDialog):
    def __init__(self, parent=None, testing=False, entryId=None):
        # Initialize object
        super(EditEntryDialog, self).__init__(parent)
        self.ui = Ui_AddEntryDialog()
        self.ui.setupUi(self)
        self.dance() # Slightly cheater way to start the ui properly
        # TODO may not need the hack here
        # HACK Make the PieceWidget in the first tab work right
        self.ui.tabWidget.removeTab(0)
        # self.ui.tabWidget.addTab(PieceWidget(), "Piece 1")
        
        # Initialize class variables
        self.testing = testing
        if entryId is None:
            QMessageBox.critical(self, 'Invalid Entry', "An invalid entry was chosen.", QMessageBox.Ok)
            self.reject()
        self.entryId = entryId
        self.entry = dbInteractionInstance.getEntryFromId(entryId)
        self.participantId = self.entry.participantID
        self.teacherId = self.entry.teacherID

        self.disciplines = {'Dance' : self.dance,   # For Pythonic switch-case
                                'Piano' : self.piano,
                                'Choral' : self.choral,
                                'Vocal' : self.vocal,
                                'Instrumental' : self.instrumental,
                                'Band' : self.band,
                                'Speech' : self.speech
                            }

        # Initialize the ui with variables
        self.ui.addEntryBtn.setText("&Update Entry")
        self.setWindowTitle("Edit Entry")
        p = dbInteractionInstance.getParticipantFromId(self.participantId)
        if p is not None:
            self.ui.participantLineEdit.setText("{0} {1}".format(p.first, p.last))
        t = dbInteractionInstance.getTeacherFromId(self.teacherId)
        if t is not None:
            self.ui.teacherLineEdit.setText("{0} {1}".format(t.first, t.last))
        index = self.ui.disciplineComboBox.findText(self.entry.discipline)
        if index < 0:
            QMessageBox.critical(self, 'Invalid Discipline', 'This entry has an invalid discipline. Setting to default discipline.', QMessageBox.Ok)
            self.ui.disciplineComboBox.setCurrentIndex(0)
        else:
            self.ui.disciplineComboBox.setCurrentIndex(index)
        self.ui.classNumberLineEdit.setText(self.entry.classNumber)
        self.ui.classNameLineEdit.setText(self.entry.className)
        self.ui.levelLineEdit.setText(self.entry.level)
        self.ui.instrumentLineEdit.setText(self.entry.instrument)
        self.ui.styleLineEdit.setText(self.entry.style)
        for i in xrange(0, len(self.entry.pieces)):
            self.ui.tabWidget.addTab(PieceWidget(piece=self.entry.pieces[i]), "Piece {0}".format(i+1))
        # trigger combobox change to set enabled fields correctly
        # but this may destroy some info if the discipline messed up
        # TODO how to handle that
        self.disciplineComboBox_changed(self.ui.disciplineComboBox.currentText())

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
        else:
            # Check there is at least one piece
            tabCount = self.ui.tabWidget.count()
            if tabCount <= 0:
                QMessageBox.warning(self, 'Missing Piece', 'Entry must have at least 1 piece', QMessageBox.Ok)
            else:
                # Check all the pieceWidgets
                pieces = []
                for i in xrange(0, tabCount):
                    pieceWidget = self.ui.tabWidget.widget(i)
                    fields = pieceWidget.getFields()

                    if fields['title'] is None or fields['title'] == "":
                        QMessageBox.warning(self, 'Missing Field', 'Piece {0} must have a Title'.format(i+1), QMessageBox.Ok)
                        break
                    # Check for valid fields
                    elif fields['performanceTime'] == "0:00" and QMessageBox.question(self, 'Validate Performance Time', 'Are you sure you want to leave performance time blank? This could cause the scheduling algorithm to make poor choices.', QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
                        # Stop here
                        break
                    else:
                        # Piece is good, add it to the list
                        pieces.append(fields)
        
                else:
                    # Everything is good, add it to the db
                    self.entry = Entry(participantID, teacherID, discipline, level, classNumber, className, style, instrument, pieces)
                    self.entry.participantID = participantID
                    self.entry.teacherID = teacherID
                    self.entry.discipline = discipline
                    self.entry.level = level
                    self.entry.classNumber = classNumber
                    self.entry.className = className
                    self.entry.style = style
                    self.entry.instrument = instrument
                    self.entry.pieces = pieces

                    result = dbInteractionInstance.updateEntry(self.entryId, self.entry)
                    if result == "":
                        QMessageBox.information(self, 'Edit Entry', 'Successfully updated entry', QMessageBox.Ok)
                        self.accept()
                    else:
                        QMessageBox.critical(self, 'Edit Entry', 'Failed to update entry\n{0}'.format(result), QMessageBox.Ok)

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
            for i in xrange(0, self.ui.tabWidget.count()):
                pieceWidget = self.ui.tabWidget.widget(i)
                pieceWidget.changeDiscipline(text)
            # self.teacherId = ""
            # self.ui.teacherLineEdit.clear()
        else:
            QMessageBox.critical(self, 'Invalid Discipline', 'An invalid discipline was selected. Please try again.', QMessageBox.Ok)

    def addPieceBtn_clicked(self):
        tabCount = self.ui.tabWidget.count()
        pieceWidget = PieceWidget()
        self.ui.tabWidget.addTab(pieceWidget, "Piece {0}".format(tabCount+1))
        # Set focus to new tab
        self.ui.tabWidget.setCurrentIndex(tabCount)
        # Set appropriate active fields on new widget
        pieceWidget.changeDiscipline(self.ui.disciplineComboBox.currentText())

    def closeTab(self, index):
        if QMessageBox.warning(self, 'Delete Piece', 
            'You are about to delete this piece and all the information it contains.\nTHIS CANNOT BE UNDONE!\n\nDo you still want to continue?', 
            QMessageBox.Yes|QMessageBox.No) == QMessageBox.No:
            return

        self.ui.tabWidget.removeTab(index)
        # rename tabs
        for i in xrange(0, self.ui.tabWidget.count()):
            self.ui.tabWidget.setTabText(i, "Piece {0}".format(i+1))

# TODO clear disabled fields
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
