"""A scheduling program for the RFOTA"""

import sys
sys.path.insert(0, '../Forms/')
# from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox
# from PyQt4.QtCore import QDate
from ui_mainwindow import Ui_MainWindow
from addSoloParticipantDialog import AddSoloParticipantDialog
from addGroupParticipantDialog import AddGroupParticipantDialog
from addTeacherDialog import AddTeacherDialog
from addEntryDialog import AddEntryDialog
from scheduleDialog import ScheduleDialog
from databaseInteraction import DatabaseInteraction
from scheduler import Scheduler
from schedule import Schedule
# import sqlite3
import traceback
import datetime

app = QApplication(sys.argv)

class MainWindow(QWidget):
    """The main window of the program"""
    def __init__(self, testing=False):
        # Initialize object using ui_mainwindow
        super(MainWindow, self).__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.db = DatabaseInteraction()
        self.connectSlots()
        self.testing = testing
        self.scheduler = Scheduler(self.db)
        # if testConn is not None:
        #     self.conn = testConn
        # else:
        #     self.conn = self.initDatabase()     

    # def initDatabase(self):
    #     """initializes the database, returns connection"""
    #     conn = sqlite3.connect('../Database/AFS')
    #     print "Opened database"
    #     return conn

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addSoloParticipantBtn.clicked.connect(self.addSoloParticipantBtn_clicked)
        self.ui.addGroupParticipantBtn.clicked.connect(self.addGroupParticipantBtn_clicked)
        self.ui.addTeacherBtn.clicked.connect(self.addTeacherBtn_clicked)
        self.ui.addEntryBtn.clicked.connect(self.addEntryBtn_clicked)
        self.ui.makeScheduleBtn.clicked.connect(self.makeScheduleBtn_clicked)
        self.ui.loadScheduleBtn.clicked.connect(self.loadScheduleBtn_clicked)

    ###### Slots ######

    def addSoloParticipantBtn_clicked(self):
        dialog = AddSoloParticipantDialog(testing=self.testing, db=self.db)
        # For Modal dialog
        dialog.exec_()

    def addGroupParticipantBtn_clicked(self):
        dialog = AddGroupParticipantDialog(testing=self.testing, db=self.db)
        # For Modal dialog
        result = dialog.exec_()

    def addTeacherBtn_clicked(self):
        dialog = AddTeacherDialog(testing=self.testing, db=self.db)
        # For Modal dialog
        result = dialog.exec_()

    def addEntryBtn_clicked(self):
        dialog = AddEntryDialog(testing=self.testing, db=self.db)
        # For Modal dialog
        result = dialog.exec_()

    def makeScheduleBtn_clicked(self):
        ### Test Code ###
        s1Start = datetime.datetime(2014, 4, 7, 9)
        s1End = datetime.datetime(2014, 4, 7, 12)
        s2Start = datetime.datetime(2014, 4, 7, 13)
        s2End = datetime.datetime(2014, 4, 7, 17)
        s3Start = datetime.datetime(2014, 4, 7, 18)
        s3End = datetime.datetime(2014, 4, 7, 21)
        sessionDatetimes = [(s1Start, s1End), (s2Start, s2End), (s3Start, s3End)]
        entries = self.db.getAllEntriesInDiscipline("Piano")
        ####
        solution = self.scheduler.process(entries, sessionDatetimes)
        print solution
        dialog = ScheduleDialog(schedule=solution, db=self.db)
        result = dialog.exec_()
        if result == True:
            pass

    def loadScheduleBtn_clicked(self):
        """Loads a schedule from file"""
        # TODO let user choose
        schedule = Schedule()
        schedule.load("testSchedule")
        dialog = ScheduleDialog(schedule=schedule, db=self.db)
        result = dialog.exec_()
        if result == True:
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
