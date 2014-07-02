import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow, QWidget
from ui_mainwindow import Ui_MainWindow
import sqlite3

app = QApplication(sys.argv)

class MainWindow(QWidget):
	def __init__(self):
		# Initialize object using ui_mainwindow
		super(MainWindow, self).__init__()
		self.window = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.window)
		self.connectSlots()
		self.initDatabase()

	def initDatabase(self):
		conn = sqlite3.connect('../Database/AFS')
		print "Opened database"

	def connectSlots(self):
		self.ui.btn_addParticipant.clicked.connect(self.btn_addParticipant_clicked)

	###### Slots ######

	def btn_addParticipant_clicked(self):
		print "Participant!"

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