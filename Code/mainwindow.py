"""A scheduling program for the RFOTA"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
import shutil
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog

from ui_mainwindow import Ui_MainWindow
from addSoloParticipantDialog import AddSoloParticipantDialog
from addGroupParticipantDialog import AddGroupParticipantDialog
from addTeacherDialog import AddTeacherDialog
from addEntryDialog import AddEntryDialog
from scheduleDialog import ScheduleDialog
from scheduleOptionsDialog import ScheduleOptionsDialog
from chooseParticipantDialog import ChooseParticipantDialog
from editSoloParticipantDialog import EditSoloParticipantDialog
from editGroupParticipantDialog import EditGroupParticipantDialog
from chooseTeacherDialog import ChooseTeacherDialog
from editTeacherDialog import EditTeacherDialog
from chooseEntryDialog import ChooseEntryDialog
from editEntryDialog import EditEntryDialog

from databaseInteraction import dbInteractionInstance
from settingsInteraction import settingsInteractionInstance
from scheduler import Scheduler
from schedule import Schedule

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
        self.ui.addSoloParticipantBtn.clicked.connect(self.addSoloParticipantBtn_clicked)
        self.ui.addGroupParticipantBtn.clicked.connect(self.addGroupParticipantBtn_clicked)
        self.ui.addTeacherBtn.clicked.connect(self.addTeacherBtn_clicked)
        self.ui.addEntryBtn.clicked.connect(self.addEntryBtn_clicked)
        self.ui.makeScheduleBtn.clicked.connect(self.makeScheduleBtn_clicked)
        self.ui.loadScheduleBtn.clicked.connect(self.loadScheduleBtn_clicked)
        self.ui.editParticipantBtn.clicked.connect(self.editParticipantBtn_clicked)
        self.ui.editTeacherBtn.clicked.connect(self.editTeacherBtn_clicked)
        self.ui.editEntryBtn.clicked.connect(self.editEntryBtn_clicked)
        self.ui.deleteParticipantBtn.clicked.connect(self.deleteParticipantBtn_clicked)
        self.ui.deleteTeacherBtn.clicked.connect(self.deleteTeacherBtn_clicked)
        self.ui.deleteEntryBtn.clicked.connect(self.deleteEntryBtn_clicked)
        self.ui.backupDbBtn.clicked.connect(self.backupDbBtn_clicked)
        self.ui.restoreDbBtn.clicked.connect(self.restoreDbBtn_clicked)
        self.ui.createNewDbBtn.clicked.connect(self.createNewDbBtn_clicked)

    ###### Slots ######

    def addSoloParticipantBtn_clicked(self):
        dialog = AddSoloParticipantDialog(testing=self.testing)
        # For Modal dialog
        dialog.exec_()

    def addGroupParticipantBtn_clicked(self):
        dialog = AddGroupParticipantDialog(testing=self.testing)
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
        """Opens chooseParticipantDialog then dialog for editing"""
        dialog = ChooseParticipantDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            participantId = dialog.getParticipantId()
            # Open appropriate edit dialog with participant
            if participantId[0] == 's':
                dialog = EditSoloParticipantDialog(participantId=participantId)
                dialog.exec_()
            elif participantId[0] == 'g':
                dialog = EditGroupParticipantDialog(participantId=participantId)
                dialog.exec_()
            else:
                QMessageBox.critical(self, "Error", "Unrecognized Participant", QMessageBox.Ok)

    def editTeacherBtn_clicked(self):
        """Opens chooseTeacherDialog then dialog for editing"""
        dialog = ChooseTeacherDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            teacherId = dialog.getTeacherId()
            # Open edit dialog with teacher
            dialog = EditTeacherDialog(teacherId=teacherId)
            dialog.exec_()

    def editEntryBtn_clicked(self):
        """Opens chooseEntryDialog then dialog for editing"""
        dialog = ChooseEntryDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            entryId = dialog.entryId
            # Open edit dialog with entry
            dialog = EditEntryDialog(entryId=entryId)
            dialog.exec_()

    def editParticipantBtn_clicked(self):
        """Opens chooseParticipantDialog then dialog for editing"""
        dialog = ChooseParticipantDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            participantId = dialog.getParticipantId()
            # Open appropriate edit dialog with participant
            if participantId[0] == 's':
                dialog = EditSoloParticipantDialog(participantId=participantId)
                dialog.exec_()
            elif participantId[0] == 'g':
                dialog = EditGroupParticipantDialog(participantId=participantId)
                dialog.exec_()
            else:
                QMessageBox.critical(self, "Error", "Unrecognized Participant", QMessageBox.Ok)

    def deleteTeacherBtn_clicked(self):
        """Opens chooseTeacherDialog for deleting"""
        dialog = ChooseTeacherDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            teacherId = dialog.getTeacherId()
            if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this teacher/contact?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
                # Delete the teacher
                dbInteractionInstance.deleteTeacherFromId(teacherId)

    def deleteEntryBtn_clicked(self):
        """Opens chooseEntryDialog for deleting"""
        dialog = ChooseEntryDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            entryId = dialog.entryId
            if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this entry?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
                # Delete the entry
                dbInteractionInstance.deleteEntryFromId(entryId)

    def deleteParticipantBtn_clicked(self):
        """Opens chooseParticipantDialog for deleting"""
        dialog = ChooseParticipantDialog()
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            participantId = dialog.getParticipantId()
            if QMessageBox.question(self, "Cannot be undone!", "Warning! This action cannot be undone. \nAre you sure you want to delete this participant?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
                # Call appropriate delete
                if participantId[0] == 's':
                    dbInteractionInstance.deleteSoloParticipantFromId(participantId[1:])
                elif participantId[0] == 'g':
                    dbInteractionInstance.deleteGroupParticipantFromId(participantId[1:])
                else:
                    QMessageBox.critical(self, "Error", "Unrecognized Participant", QMessageBox.Ok)

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
