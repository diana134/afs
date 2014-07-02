import sys
sys.path.insert(0, '../Forms/')
from PyQt4 import QtGui
from PyQt4.QtGui import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import sqlite3

def btn_addParticipant_clicked(self):
	print "Participant!"

def connectSlots(ui):
	ui.btn_addParticipant.clicked.connect(btn_addParticipant_clicked)

def initDatabase():
	conn = sqlite3.connect('../Database/AFS')
	print "Opened database"
	return conn

def initMainWindow():
	app = QApplication(sys.argv)
	window = QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(window)
	connectSlots(ui)
	window.show()
	sys.exit(app.exec_())

def main():
	conn = initDatabase()
	initMainWindow()

if __name__ == "__main__":
    main()