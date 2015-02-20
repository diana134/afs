"""The UI for viewing and editing a Schedule"""

import sys
import os.path
sys.path.insert(0, os.path.join("..", "Forms"))
from PyQt4.QtGui import QDialog, QTableWidgetItem, QMessageBox, QFileDialog
import datetime

from ui_scheduleDialog import Ui_ScheduleDialog
from databaseInteraction import dbInteractionInstance
from settingsInteraction import settingsInteractionInstance

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
        self.ui.validateBtn.clicked.connect(self.validateBtn_clicked)

    def displaySchedule(self):
        """Displays the schedule in scheduleTableWidget"""

        # start by clearing everything
        self.ui.scheduleTableWidget.clear()

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
        # Make sure something is selected
        if self.ui.scheduleTableWidget.selectedItems() is not None:
            # Get which Event is selected
            col = self.ui.scheduleTableWidget.currentColumn()
            eventIndex = self.ui.scheduleTableWidget.currentRow()
            event = self.schedule.sessions[col].eventList[eventIndex]

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
            if filename[-5:] != ".docx":
                filename += ".docx"
            self.schedule.toWordFile(filename=filename)
            QMessageBox.information(self, 'Print Schedule', 'Schedule print file saved to ' + filename, QMessageBox.Ok)

    def validateBtn_clicked(self):
        """checks that the schedule has everything from the db and nothing goes overtime"""
        valid = True
        # check that no sessions go overtime
        for session in self.schedule.sessions:
            overtime = session.emptyTime() + settingsInteractionInstance.loadTolerance()
            if overtime < datetime.timedelta():
                valid = False
                QMessageBox.warning(self, 'Session Overtime', 'Session beginning at {0} runs {1} overtime, taking adjudication time and tolerance for overtime into account.'.format(session.startDatetime, overtime), QMessageBox.Ok)

        if valid:
            QMessageBox.information(self, 'Valid Schedule', 'Everything checks out. Nothing runs overtime.', QMessageBox.Ok)

        # TODO check has everything from db (in case maybe this schedule was loaded from memory after changes were made)

    def scheduleUpBtn_clicked(self):
        # make sure something is selected
        if self.ui.scheduleTableWidget.selectedItems() is None:
            return

        # get indexes
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not top
        if eventIndex > 0:
            # swap with thing above
            self.schedule.sessions[sessionIndex].eventList[eventIndex], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex-1] = \
            self.schedule.sessions[sessionIndex].eventList[eventIndex-1], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex]
            
            # clear selection
            self.ui.scheduleTableWidget.clearSelection()
            self.displaySchedule()
            # reset selection
            index = self.ui.scheduleTableWidget.model().index(eventIndex-1, sessionIndex)
            self.ui.scheduleTableWidget.setCurrentIndex(index)

    def scheduleDownBtn_clicked(self):
        # make sure something is selected
        if self.ui.scheduleTableWidget.selectedItems() is None:
            return

        # get indexes
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not bottom
        if eventIndex <= self.ui.scheduleTableWidget.rowCount():
            # swap with thing below
            self.schedule.sessions[sessionIndex].eventList[eventIndex], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex+1] = \
            self.schedule.sessions[sessionIndex].eventList[eventIndex+1], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex]
            
            # clear selection
            self.ui.scheduleTableWidget.clearSelection()
            self.displaySchedule()
            # reset selection
            index = self.ui.scheduleTableWidget.model().index(eventIndex+1, sessionIndex)
            self.ui.scheduleTableWidget.setCurrentIndex(index)

    def scheduleLeftBtn_clicked(self):
        # make sure something is selected
        if self.ui.scheduleTableWidget.selectedItems() is None:
            return

        # get indexes
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not furthest left
        if sessionIndex > 0:
            # insert to the left
            self.schedule.sessions[sessionIndex-1].eventList.insert(eventIndex, \
            self.schedule.sessions[sessionIndex].eventList[eventIndex])
            # and remove it from where it was
            self.schedule.sessions[sessionIndex].eventList.pop(eventIndex)
            
            # clear selection
            self.ui.scheduleTableWidget.clearSelection()
            self.displaySchedule()
            # reset selection
            index = self.ui.scheduleTableWidget.model().index(eventIndex, sessionIndex-1)
            self.ui.scheduleTableWidget.setCurrentIndex(index)

    def scheduleRightBtn_clicked(self):
        # make sure something is selected
        if self.ui.scheduleTableWidget.selectedItems() is None:
            return

        # get indexes
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not furthest right
        if sessionIndex <= self.ui.scheduleTableWidget.columnCount():
            # insert to the right
            self.schedule.sessions[sessionIndex+1].eventList.insert(eventIndex, \
            self.schedule.sessions[sessionIndex].eventList[eventIndex])
            # and remove it from where it was
            self.schedule.sessions[sessionIndex].eventList.pop(eventIndex)
            
            # clear selection
            self.ui.scheduleTableWidget.clearSelection()
            self.displaySchedule()
            # reset selection
            index = self.ui.scheduleTableWidget.model().index(eventIndex, sessionIndex+1)
            self.ui.scheduleTableWidget.setCurrentIndex(index)

    def entriesUpBtn_clicked(self):
        # make sure something is selected
        if self.ui.entriesTableWidget.selectedItems() is None:
            return

        # get indexes
        entryIndex = self.ui.entriesTableWidget.currentRow()
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not top
        if entryIndex > 0:
            # swap with thing above
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex-1] = \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex-1], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex]
            
            # clear selection
            self.ui.entriesTableWidget.clearSelection()
            self.scheduleTableWidget_itemSelectionChanged()
            # reset selection
            index = self.ui.entriesTableWidget.model().index(entryIndex-1, 0)
            self.ui.entriesTableWidget.setCurrentIndex(index)

    def entriesDownBtn_clicked(self):
        # make sure something is selected
        if self.ui.entriesTableWidget.selectedItems() is None:
            return

        # get indexes
        entryIndex = self.ui.entriesTableWidget.currentRow()
        eventIndex = self.ui.scheduleTableWidget.currentRow()
        sessionIndex = self.ui.scheduleTableWidget.currentColumn()

        # if selected is not bottom
        if entryIndex <= self.ui.entriesTableWidget.rowCount():
            # swap with thing below
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex+1] = \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex+1], \
            self.schedule.sessions[sessionIndex].eventList[eventIndex].entries[entryIndex]
            
            # clear selection
            self.ui.entriesTableWidget.clearSelection()
            self.scheduleTableWidget_itemSelectionChanged()
            # reset selection
            index = self.ui.entriesTableWidget.model().index(entryIndex+1, 0)
            self.ui.entriesTableWidget.setCurrentIndex(index)
