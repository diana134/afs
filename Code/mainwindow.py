"""A scheduling program for the RFOTA"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
# import datetime

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
        filename = QFileDialog.getOpenFileName(self, "Load Schedule", "", "Schedule Files (*.sched)")
        if filename is not None and filename != "":
            try:
                schedule.load(filename)
                dialog = ScheduleDialog(schedule=schedule)
                result = dialog.exec_()
                if result == True:
                    pass
            except Exception:
                QMessageBox.critical("Error", "Failed to load schedule.", QMessageBox.Ok)

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
                QMessageBox.critical("Error", "Unrecognized Participant", QMessageBox.Ok)

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
