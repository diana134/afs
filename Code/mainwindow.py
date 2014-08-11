import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt4.QtCore import QDate
from ui_mainwindow import Ui_MainWindow
from addSoloParticipantDialog import AddSoloParticipantDialog
import sqlite3
import traceback
from participant import Participant

app = QApplication(sys.argv)

class MainWindow(QWidget):
    def __init__(self, testing=False, testConn=None):
        # Initialize object using ui_mainwindow
        super(MainWindow, self).__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.connectSlots()
        self.testing = testing
        if testConn is not None:
            self.conn = testConn
        else:
            self.conn = self.initDatabase()     

    def initDatabase(self):
        """initializes the database, returns connection"""
        conn = sqlite3.connect('../Database/AFS')
        print "Opened database"
        return conn

    def connectSlots(self):
        """connect the various ui signals to their slots"""
        self.ui.addSoloParticipantBtn.clicked.connect(self.addSoloParticipantBtn_clicked)

    ###### Slots ######

    def addSoloParticipantBtn_clicked(self):
        dialog = AddSoloParticipantDialog(testing=self.testing)
        # For Modal dialog
        result = dialog.exec_()

        if result == True:
            p = dialog.getParticipant()
            try:
                p.addToDB(self.conn)
                if not self.testing:
                    QMessageBox.information(self, 'Add Participant', 'Successfully added new participant', QMessageBox.Ok)
            except Exception, e:
                print traceback.format_exc()
                if not self.testing:
                    QMessageBox.critical(self, 'Add Participant', 'Failed to add new participant\n{0}'.format(e), QMessageBox.Ok)

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