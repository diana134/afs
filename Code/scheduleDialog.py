"""The UI for viewing and editing a Schedule"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QTableWidgetItem, QMessageBox, QFileDialog

from ui_scheduleDialog import Ui_ScheduleDialog
from databaseInteraction import dbInteractionInstance

exportsPath = os.path.join("..", "Exports")

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
        self.ui.btnBox.accepted.connect(self.saveBtn_clicked)
        self.ui.btnBox.rejected.connect(self.cancelBtn_clicked)
        self.ui.exportScheduleBtn.clicked.connect(self.exportScheduleBtn_clicked)
        self.ui.printScheduleBtn.clicked.connect(self.printScheduleBtn_clicked)

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

    def saveBtn_clicked(self):
        """Saves schedule for future use"""
        filename = QFileDialog.getSaveFileName(self, "Save Schedule", exportsPath, "Schedule Files (*.sched)")
        if filename is not None and filename != "":
            if filename[-6:] != ".sched":
                filename += ".sched"
            self.schedule.save(filename)
            QMessageBox.information(self, 'Save Schedule', 'Schedule saved to ' + filename, QMessageBox.Ok)
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
                if len(entry.selections) > 1:
                    self.ui.entriesTableWidget.setItem(row, 0, QTableWidgetItem("<multiple>"))
                    minutes, seconds = divmod(entry.totalTime().total_seconds(), 60)
                    self.ui.entriesTableWidget.setItem(row, 2, QTableWidgetItem("{:.0f}:{:02d}".format(minutes, int(seconds))))
                else:
                    try:
                        self.ui.entriesTableWidget.setItem(row, 0, QTableWidgetItem(entry.selections[0]['title']))
                        self.ui.entriesTableWidget.setItem(row, 2, QTableWidgetItem(entry.selections[0]['performanceTime']))
                    except IndexError: # TODO This is only here because some old test data has no selections
                        self.ui.entriesTableWidget.setItem(row, 0, QTableWidgetItem("old test data"))
                        self.ui.entriesTableWidget.setItem(row, 2, QTableWidgetItem("old test data"))
                
                participant = dbInteractionInstance.getParticipantFromId(entry.participantID)
                name = ""
                try:
                    name = participant.first + " " + participant.last
                except AttributeError:
                    name = participant.groupName
                self.ui.entriesTableWidget.setItem(row, 1, QTableWidgetItem(name))
        else:
            # Clear table
            self.ui.entriesTableWidget.setRowCount(0)

    def exportScheduleBtn_clicked(self):
        """Exports a schedule to a csv"""
        filename = QFileDialog.getSaveFileName(self, "Export Schedule", exportsPath, "CSV Files (*.csv)")
        if filename is not None and filename != "":
            if filename[-4:] != ".csv":
                filename += ".csv"
            self.schedule.export(filename=filename)
            QMessageBox.information(self, 'Export Schedule', 'Schedule exported to ' + filename, QMessageBox.Ok)

    def printScheduleBtn_clicked(self):
        """Prints a schedule to a docx"""
        filename = str(QFileDialog.getSaveFileName(self, "Print Schedule", exportsPath, "Word Files (*.docx)"))
        if filename is not None and filename != "":
            if filename[-4:] != ".docx":
                filename += ".docx"
            self.schedule.toWordFile(filename=filename)
            QMessageBox.information(self, 'Print Schedule', 'Schedule print file saved to ' + filename, QMessageBox.Ok)

    def scheduleUpBtn_clicked(self):
        currRow = self.ui.scheduleTableWidget.currentRow()
        currCol = self.ui.scheduleTableWidget.currentColumn()
        # if selected is not top
        if currRow > 0:
            # swap with thing above
            # TODO make this work
            itemAbove = self.ui.scheduleTableWidget.item(currRow-1, currCol)
            currItem = self.ui.scheduleTableWidget.currentItem()
            self.ui.scheduleTableWidget.setItem(currRow, currCol, itemAbove)
            self.ui.scheduleTableWidget.setItem(currRow-1, currCol, currItem)
            self.ui.scheduleTableWidget.setCurrentItem(currItem)
        pass

    def scheduleDownBtn_clicked(self):
        # if selected is not bottom
            # swap with thing below
        pass

    def scheduleLeftBtn_clicked(self):
        # if selected is not furthest left
            # add to bottom of next left column
        pass

    def scheduleRightBtn_clicked(self):
        # if selected is not furthest right
            # add to bottom of next right column
        pass

    def entriesUpBtn_clicked(self):
        pass

    def entriesDownBtn_clicked(self):
        pass
