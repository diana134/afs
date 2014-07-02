import sys
sys.path.insert(0, '../Forms/')
from PyQt4.QtGui import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import sqlite3

def setupSlots():
	btn_addParticipants.clicked.connect(Participant.addToDB(conn))

def initDatabase():
	conn = sqlite3.connect('../Database/AFS.db')
	print "Opened database"
	return conn

def initMainWindow():
	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	window.show()
	sys.exit(app.exec_())

def main():
	conn = initDatabase()
	initMainWindow()
	setupSlots()

if __name__ == "__main__":
    main()