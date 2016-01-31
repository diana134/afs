"""A scheduling program for the RFOTA"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
import shutil
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QItemSelectionModel, QAbstractItemView
from PyQt4.QtCore import Qt

from ui_mainwindow import Ui_MainWindow
from addParticipantDialog import AddParticipantDialog
from addTeacherDialog import AddTeacherDialog
from addEntryDialog import AddEntryDialog
from scheduleDialog import ScheduleDialog
from scheduleOptionsDialog import ScheduleOptionsDialog
from chooseParticipantDialog import ChooseParticipantDialog
from editParticipantDialog import EditParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from editTeacherDialog import EditTeacherDialog
from chooseEntryDialog import ChooseEntryDialog
from editEntryDialog import EditEntryDialog

from databaseInteraction import dbInteractionInstance
from settingsInteraction import settingsInteractionInstance
from scheduler import Scheduler
from schedule import Schedule
from entry import Entry

app = QApplication(sys.argv)
exportsPath = os.path.join("..", "Exports")
dbPath = os.path.join("..", "Database")

class MainWindow(QWidget):
    """The main window of the program"""
    def __init__(self, testing=False):
        # Initialize object using ui_mainwindow
        super(MainWindow, self).__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.connectSlots()
        self.testing = testing
        self.scheduler = Scheduler()

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)
        self.ui.addTeacherBtn.clicked.connect(self.addTeacherBtn_clicked)
        self.ui.addEntryBtn.clicked.connect(self.addEntryBtn_clicked)
        # self.ui.makeScheduleBtn.clicked.connect(self.makeScheduleBtn_clicked)
        # self.ui.loadScheduleBtn.clicked.connect(self.loadScheduleBtn_clicked)
        self.ui.editParticipantBtn.clicked.connect(self.editParticipantBtn_clicked)
        self.ui.editTeacherBtn.clicked.connect(self.editTeacherBtn_clicked)
        self.ui.editEntryBtn.clicked.connect(self.editEntryBtn_clicked)
        # self.ui.deleteParticipantBtn.clicked.connect(self.deleteParticipantBtn_clicked)
        # self.ui.deleteTeacherBtn.clicked.connect(self.deleteTeacherBtn_clicked)
        # self.ui.deleteEntryBtn.clicked.connect(self.deleteEntryBtn_clicked)
        # self.ui.backupDbBtn.clicked.connect(self.backupDbBtn_clicked)
        # self.ui.restoreDbBtn.clicked.connect(self.restoreDbBtn_clicked)
        # self.ui.createNewDbBtn.clicked.connect(self.createNewDbBtn_clicked)
        # self.ui.entriesByDisciplineBtn.clicked.connect(self.entriesByDisciplineBtn_clicked)
        # self.ui.entriesByTeacherBtn.clicked.connect(self.entriesByTeacherBtn_clicked)
        # self.ui.entriesByGroupBtn.clicked.connect(self.entriesByGroupBtn_clicked)
        # self.ui.dumpBtn.clicked.connect(self.dumpBtn_clicked)

        self.ui.participantTableView.setModel(dbInteractionInstance.participantModel)
        self.ui.participantTableView.model().sort(9, Qt.DescendingOrder)
        self.ui.participantTableView.setSelectionModel(QItemSelectionModel(dbInteractionInstance.participantModel))
        self.ui.participantTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.participantTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.participantTableView.hideColumn(9) # id

        self.ui.teacherTableView.setModel(dbInteractionInstance.teacherModel)
        self.ui.teacherTableView.model().sort(0, Qt.DescendingOrder)
        self.ui.teacherTableView.setSelectionModel(QItemSelectionModel(dbInteractionInstance.teacherModel))
        self.ui.teacherTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.teacherTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.teacherTableView.hideColumn(0) # id

        self.ui.entryTableView.setModel(dbInteractionInstance.entryModel)
        self.ui.entryTableView.model().sort(0, Qt.DescendingOrder)
        self.ui.entryTableView.setSelectionModel(QItemSelectionModel(dbInteractionInstance.entryModel))
        self.ui.entryTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.entryTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.entryTableView.hideColumn(0) # id

        self.ui.pieceTableView.setModel(dbInteractionInstance.pieceModel)
        self.ui.pieceTableView.model().sort(0, Qt.DescendingOrder)
        self.ui.pieceTableView.setSelectionModel(QItemSelectionModel(dbInteractionInstance.pieceModel))
        self.ui.pieceTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.pieceTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.pieceTableView.hideColumn(0) # id
        self.ui.pieceTableView.hideColumn(4) # entryId

    ###### Slots ######

    def addParticipantBtn_clicked(self):
        dialog = AddParticipantDialog(testing=self.testing)
        # For Modal dialog
        dialog.exec_()

    def addTeacherBtn_clicked(self):
        dialog = AddTeacherDialog(testing=self.testing)
        # For Modal dialog
        dialog.exec_()

    def addEntryBtn_clicked(self):
        dialog = AddEntryDialog(testing=self.testing)
        # For Modal dialog
        dialog.exec_()

    def makeScheduleBtn_clicked(self):
        ### Test Code ###
        # s1Start = datetime.datetime(2014, 4, 7, 9)
        # s1End = datetime.datetime(2014, 4, 7, 12)
        # s2Start = datetime.datetime(2014, 4, 7, 13)
        # s2End = datetime.datetime(2014, 4, 7, 17)
        # s3Start = datetime.datetime(2014, 4, 7, 18)
        # s3End = datetime.datetime(2014, 4, 7, 21)
        # sessionDatetimes = [(s1Start, s1End), (s2Start, s2End), (s3Start, s3End)]
        ####
        scheduleOptionsDialog = ScheduleOptionsDialog()
        result = scheduleOptionsDialog.exec_()
        if result == True:
            entries = dbInteractionInstance.getAllEntriesInDiscipline(settingsInteractionInstance.loadDiscipline())
            solution = self.scheduler.process(entries, settingsInteractionInstance.loadSessionDatetimes())
            print solution            
            if solution is None:
                QMessageBox.warning(self, 'No schedule found', 'No schedule was found for the specified parameters. Try increasing tolerance for overtime or making the sessions longer.', 
                    QMessageBox.Ok)
                return
            dialog = ScheduleDialog(schedule=solution)
            result = dialog.exec_()
            if result == True:
                pass

    def loadScheduleBtn_clicked(self):
        """Loads a schedule from file"""
        schedule = Schedule()
        filename = QFileDialog.getOpenFileName(self, "Load Schedule", exportsPath, "Schedule Files (*.sched)")
        if filename is not None and filename != "":
            try:
                schedule.load(filename)
                dialog = ScheduleDialog(schedule=schedule)
                result = dialog.exec_()
                if result == True:
                    pass
            except Exception:
                QMessageBox.critical(self, "Error", "Failed to load schedule.", QMessageBox.Ok)

    def editParticipantBtn_clicked(self):
        """Opens the dialog for editing"""
        # TODO get participant id
        participantId = 0
        dialog = EditParticipantDialog(participantId=participantId)
        # For Modal dialog
        dialog.exec_()

    def editTeacherBtn_clicked(self):
        """Opens dialog for editing"""
        # TODO get teacher id
        teacherId = 0
        dialog = EditTeacherDialog(teacherId=teacherId)
        # For Modal dialog
        dialog.exec_()

    def editEntryBtn_clicked(self):
        """Opens dialog for editing"""
        # TODO get entry id
        entryId = 0
        dialog = EditEntryDialog(entryId=entryId)
        # For Modal dialog
        dialog.exec_()

    def deleteTeacherBtn_clicked(self):
        """Deletes selected teacher"""
         # TODO get teacher id
        teacherId = 0

        if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this teacher/contact?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            # Delete the teacher
            dbInteractionInstance.deleteTeacherFromId(teacherId)

    def deleteEntryBtn_clicked(self):
        """Deletes selected entry"""
         # TODO get entry id
        entryId = 0

        if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this entry?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            # Delete the entry
            dbInteractionInstance.deleteEntryFromId(entryId)

    def deleteParticipantBtn_clicked(self):
        """Deletes selected participant"""
         # TODO get participant id
        participantId = 0

        if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this participant?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            # Delete the participant
            dbInteractionInstance.deleteParticipantFromId(participantId[1:])

    def backupDbBtn_clicked(self):
        """Copies the current db file to AFS-YYYY-MM-DD-HH-MM-SS.bak"""
        result = dbInteractionInstance.backupDb()
        if result == "":
            QMessageBox.information(self, "Success", "Database successfully backed up.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Failed", "Could not create backup. Aborted with error:\n{0}".format(result))

    def restoreDbBtn_clicked(self):
        """Grabs the most recent backup, backs up the current db, copies recent backup to current db"""
        result = dbInteractionInstance.restoreDb()
        if result == "":
            QMessageBox.information(self, "Success", "Database successfully restored.", QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Failed", "Could not restore from backup. Aborted with error:\n{0}".format(result))

    def createNewDbBtn_clicked(self):
        """Backs up current db, then drops and recreates all the tables"""
        # TODO low priority, probably don't need it until after the festival
        pass

    def entriesByDisciplineBtn_clicked(self):
        """Saves a csv of all the entries sorted by Discipline"""
        filename = QFileDialog.getSaveFileName(self, "Report Entries by Discipline", exportsPath, "CSV Files (*.csv)")
        if filename is not None and filename != "":
            if filename[-4:] != ".csv":
                filename += ".csv"
            entries = dbInteractionInstance.getAllEntries()
            # Get participant and teacher names for entries
            # Note super bad hack where I replace the ID with a name
            for entry in entries:
                participant = dbInteractionInstance.getParticipantFromId(entry.participantID)
                try:
                    entry.participantID = "{last}, {first}".format(last=participant.last, first=participant.first)
                except Exception:
                    entry.participantID = "{groupName}".format(groupName=participant.groupName)

                if entry.teacherID != "":
                    teacher = dbInteractionInstance.getTeacherFromId(entry.teacherID)
                    entry.teacherID = "{last}, {first}".format(last=teacher.last, first=teacher.first)

            entries.sort(key=lambda x: (x.discipline, x.classNumber, x.participantID))
            fout = open(filename, 'w')
            fout.write(Entry.reportByDisciplineHeader())
            for entry in entries:
                entry.reportByDiscipline(fout)
            fout.close()
            QMessageBox.information(self, 'Report Entries by Discipline', 'Report saved to ' + filename, QMessageBox.Ok)

    def entriesByTeacherBtn_clicked(self):
        """Saves a csv of all the entries sorted by Teacher"""
        filename = QFileDialog.getSaveFileName(self, "Report Entries by Teacher", exportsPath, "CSV Files (*.csv)")
        if filename is not None and filename != "":
            if filename[-4:] != ".csv":
                filename += ".csv"
            entries = dbInteractionInstance.getAllEntries()
            # Get participant and teacher names for entries
            # Note super bad hack where I replace the ID with a name
            for entry in entries:
                participant = dbInteractionInstance.getParticipantFromId(entry.participantID)
                try:
                    entry.participantID = "{last}, {first}".format(last=participant.last, first=participant.first)
                except Exception:
                    entry.participantID = "{groupName}".format(groupName=participant.groupName)

                if entry.teacherID != "":
                    teacher = dbInteractionInstance.getTeacherFromId(entry.teacherID)
                    entry.teacherID = "{last}, {first}".format(last=teacher.last, first=teacher.first)

            entries.sort(key=lambda x: (x.teacherID, x.participantID, x.discipline, x.classNumber))
            fout = open(filename, 'w')
            fout.write(Entry.reportByTeacherHeader())
            for entry in entries:
                entry.reportByTeacher(fout)
            fout.close()
            QMessageBox.information(self, 'Report Entries by Teacher', 'Report saved to ' + filename, QMessageBox.Ok)

    def entriesByGroupBtn_clicked(self):
        """Saves a csv of all the entries sorted by Group"""
        filename = QFileDialog.getSaveFileName(self, "Report Entries by School/Group", exportsPath, "CSV Files (*.csv)")
        if filename is not None and filename != "":
            if filename[-4:] != ".csv":
                filename += ".csv"
            entries = dbInteractionInstance.getAllEntries()
            # TODO sort by school then group name (for group participants only)
            # entries.sort(key=lambda x: (x.discipline, x.classNumber))
            for entry in entries:
                print entry
            # TODO write csv
            QMessageBox.information(self, 'Report Entries by School/Group', 'Report saved to ' + filename, QMessageBox.Ok)

    def dumpBtn_clicked(self):
        """Saves a csv of all the data so they can do what they want with it"""
        filename = QFileDialog.getSaveFileName(self, "Database Dump", exportsPath, "CSV Files (*.csv)")
        if filename is not None and filename != "":
            if filename[-4:] != ".csv":
                filename += ".csv"

            entries = dbInteractionInstance.getAllEntries()
            fout = open(filename, 'w')
            fout.write(Entry.dumpHeader())
            for entry in entries:
                entry.dump(fout)
            fout.close()
            QMessageBox.information(self, 'Database Dump', 'Data saved to ' + filename, QMessageBox.Ok)

    ##########

    def run(self):
        # Show the form
        self.window.show()
        # Run the application
        app.exec_()

def main():
    myApp = MainWindow()
    myApp.run()

if __name__ == "__main__":
    main()
