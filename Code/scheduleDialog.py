"""The UI for viewing and editing a Schedule"""

import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QDialog, QTableWidgetItem, QMessageBox

from ui_scheduleDialog import Ui_ScheduleDialog
from databaseInteraction import dbInteractionInstance

class ScheduleDialog(QDialog):
    def __init__(self, parent=None, schedule=None):
        super(ScheduleDialog, self).__init__(parent)
        self.ui = Ui_ScheduleDialog()
        self.ui.setupUi(self)
        self.schedule = schedule
        self.displaySchedule()
        self.connectSlots()    

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.scheduleTableWidget.itemSelectionChanged.connect(self.scheduleTableWidget_itemSelectionChanged)
        self.ui.scheduleUpBtn.clicked.connect(self.scheduleUpBtn_clicked)
        self.ui.scheduleDownBtn.clicked.connect(self.scheduleDownBtn_clicked)
        self.ui.scheduleLeftBtn.clicked.connect(self.scheduleLeftBtn_clicked)
        self.ui.scheduleRightBtn.clicked.connect(self.scheduleRightBtn_clicked)
        self.ui.entriesUpBtn.clicked.connect(self.entriesUpBtn_clicked)
        self.ui.entriesDownBtn.clicked.connect(self.entriesDownBtn_clicked)
        self.ui.btnBox.accepted.connect(self.okBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)
        self.ui.exportScheduleBtn.clicked.connect(self.exportScheduleBtn_clicked)

    def displaySchedule(self):
        """Displays the schedule in scheduleTableWidget"""
        self.ui.scheduleTableWidget.setColumnCount(len(self.schedule.sessions))

        tableHeader = []
        for col in xrange(len(self.schedule.sessions)):
            # Set column label
            tableHeader.append(str(self.schedule.sessions[col].startDatetime))
            session = self.schedule.sessions[col]
            # Check if we need more rows
            if len(session.eventList) > self.ui.scheduleTableWidget.rowCount():
                self.ui.scheduleTableWidget.setRowCount(len(session.eventList))
            for row in xrange(len(session.eventList)):
                event = session.eventList[row]
                newItem = QTableWidgetItem(event.classNumber)
                self.ui.scheduleTableWidget.setItem(row, col, newItem)

        self.ui.scheduleTableWidget.setHorizontalHeaderLabels(tableHeader)

    ##### Slots #####

    def okBtn_clicked(self):
        """Saves schedule for future use"""
        # TODO user can choose filename
        self.schedule.save("testSchedule")
        # All done!
        self.accept()

    def cancelBtn_clicked(self):
        """Discards the schedule and closes the window"""
        self.reject()

    def scheduleTableWidget_itemSelectionChanged(self):
        """Displays the entries of the selected event in entriesTableWidget"""
        # Get which Event is selected
        eventTableItem = self.ui.scheduleTableWidget.currentItem()
        if eventTableItem is not None:
            col = self.ui.scheduleTableWidget.column(eventTableItem)
            event = next(x for x in self.schedule.sessions[col].eventList if x.classNumber == eventTableItem.text())

            # Set up columns
            self.ui.entriesTableWidget.setColumnCount(3)
            tableHeader = ["Title", "Participant", "Performance Time"]
            self.ui.entriesTableWidget.setHorizontalHeaderLabels(tableHeader)

            # Set up rows
            self.ui.entriesTableWidget.setRowCount(len(event.entries))
            for row in xrange(len(event.entries)):
                entry = event.entries[row]
                self.ui.entriesTableWidget.setItem(row, 0, QTableWidgetItem(entry.title))
                participant = dbInteractionInstance.getParticipantFromId(entry.participantID)
                name = ""
                try:
                    name = participant.first + " " + participant.last
                except AttributeError:
                    name = participant.groupName
                self.ui.entriesTableWidget.setItem(row, 1, QTableWidgetItem(name))
                self.ui.entriesTableWidget.setItem(row, 2, QTableWidgetItem(entry.performanceTime))
        else:
            # Clear table
            self.ui.entriesTableWidget.setRowCount(0)

    def exportScheduleBtn_clicked(self):
        """Exports a schedule to a csv"""
        filename = "testScheduleCSV.csv"
        self.schedule.export(filename=filename)
        QMessageBox.information(self, 'Export Schedule', 'Schedule exported to ' + filename, QMessageBox.Ok)

    def scheduleUpBtn_clicked(self):
        pass

    def scheduleDownBtn_clicked(self):
        pass

    def scheduleLeftBtn_clicked(self):
        pass

    def scheduleRightBtn_clicked(self):
        pass

    def entriesUpBtn_clicked(self):
        pass

    def entriesDownBtn_clicked(self):
        pass
