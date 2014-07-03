import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt4.QtCore import QDate
from ui_mainwindow import Ui_MainWindow
import sqlite3
import traceback
from participant import Participant

app = QApplication(sys.argv)

class MainWindow(QWidget):
	def __init__(self):
		# Initialize object using ui_mainwindow
		super(MainWindow, self).__init__()
		self.window = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.connectSlots()
		self.conn = self.initDatabase()

	def initDatabase(self):
		conn = sqlite3.connect('../Database/AFS')
		print "Opened database"
		return conn

	def connectSlots(self):
		self.ui.addParticipantBtn.clicked.connect(self.addParticipantBtn_clicked)

	###### Slots ######

	def addParticipantBtn_clicked(self):
		first = self.ui.firstNameLineEdit.text()
		last = self.ui.lastNameLineEdit.text()
		address = self.ui.addressLineEdit.text()
		city = self.ui.cityLineEdit.text()
		postal = self.ui.postalCodeLineEdit.text()
		home = self.ui.homePhoneLineEdit.text()
		cell = self.ui.cellPhoneLineEdit.text()
		email = self.ui.emailLineEdit.text()
		dob = self.ui.dateOfBirthDateEdit.date().toString(1)
		print address
		# Error checking
		# TODO: set focus to incorrect field
		if first is None or first == "":
			QMessageBox.warning(self, 'Missing Field', 'Participant must have a First Name', QMessageBox.Ok)
		elif last is None or last == "":
			QMessageBox.warning(self, 'Missing Field', 'Participant must have a Last Name', QMessageBox.Ok)
		elif dob is None or dob == QDate(1900, 1, 1):
			QMessageBox.warning(self, 'Missing Field', 'Participant must have a Date of Birth', QMessageBox.Ok)
		else:
			p = Participant(first, last, address, city, postal, home, cell, email, dob)
			try:
				p.addToDB(self.conn)# If we get here, we had success
				QMessageBox.information(self, 'Add Participant', 'Successfully added new participant', QMessageBox.Ok)
			except Exception, e:
				print traceback.format_exc()
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