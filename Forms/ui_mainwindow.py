# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Fri Jan 29 22:06:41 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1321, 777)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.participantTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.participantTableWidget.setObjectName(_fromUtf8("participantTableWidget"))
        self.participantTableWidget.setColumnCount(12)
        self.participantTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 7, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 8, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 9, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 10, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(0, 11, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 6, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 7, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 8, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 9, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 10, item)
        item = QtGui.QTableWidgetItem()
        self.participantTableWidget.setItem(1, 11, item)
        self.verticalLayout.addWidget(self.participantTableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.horizontalLayout.addWidget(self.addParticipantBtn)
        self.editParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.editParticipantBtn.setObjectName(_fromUtf8("editParticipantBtn"))
        self.horizontalLayout.addWidget(self.editParticipantBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.teacherTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.teacherTableWidget.setObjectName(_fromUtf8("teacherTableWidget"))
        self.teacherTableWidget.setColumnCount(6)
        self.teacherTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.teacherTableWidget.setItem(1, 5, item)
        self.verticalLayout_2.addWidget(self.teacherTableWidget)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.addTeacherBtn = QtGui.QPushButton(self.centralwidget)
        self.addTeacherBtn.setObjectName(_fromUtf8("addTeacherBtn"))
        self.horizontalLayout_4.addWidget(self.addTeacherBtn)
        self.editTeacherBtn = QtGui.QPushButton(self.centralwidget)
        self.editTeacherBtn.setObjectName(_fromUtf8("editTeacherBtn"))
        self.horizontalLayout_4.addWidget(self.editTeacherBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.splitter_2 = QtGui.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.splitter_2)
        self.verticalLayoutWidget_4.setObjectName(_fromUtf8("verticalLayoutWidget_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_4.addWidget(self.label_4)
        self.entryTableWidget = QtGui.QTableWidget(self.verticalLayoutWidget_4)
        self.entryTableWidget.setObjectName(_fromUtf8("entryTableWidget"))
        self.entryTableWidget.setColumnCount(7)
        self.entryTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 5, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(0, 6, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 5, item)
        item = QtGui.QTableWidgetItem()
        self.entryTableWidget.setItem(1, 6, item)
        self.verticalLayout_4.addWidget(self.entryTableWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.addEntryBtn = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.addEntryBtn.setObjectName(_fromUtf8("addEntryBtn"))
        self.horizontalLayout_3.addWidget(self.addEntryBtn)
        self.editEntryBtn = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.editEntryBtn.setObjectName(_fromUtf8("editEntryBtn"))
        self.horizontalLayout_3.addWidget(self.editEntryBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.splitter_2)
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_3.addWidget(self.label)
        self.pieceTableWidget = QtGui.QTableWidget(self.verticalLayoutWidget_3)
        self.pieceTableWidget.setObjectName(_fromUtf8("pieceTableWidget"))
        self.pieceTableWidget.setColumnCount(4)
        self.pieceTableWidget.setRowCount(2)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.pieceTableWidget.setItem(1, 3, item)
        self.verticalLayout_3.addWidget(self.pieceTableWidget)
        self.gridLayout.addWidget(self.splitter_2, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1321, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Schedule = QtGui.QMenu(self.menubar)
        self.menu_Schedule.setObjectName(_fromUtf8("menu_Schedule"))
        self.menu_Database = QtGui.QMenu(self.menubar)
        self.menu_Database.setObjectName(_fromUtf8("menu_Database"))
        MainWindow.setMenuBar(self.menubar)
        self.action_Create_Backup = QtGui.QAction(MainWindow)
        self.action_Create_Backup.setObjectName(_fromUtf8("action_Create_Backup"))
        self.action_Load_Backup = QtGui.QAction(MainWindow)
        self.action_Load_Backup.setObjectName(_fromUtf8("action_Load_Backup"))
        self.actionE_xit = QtGui.QAction(MainWindow)
        self.actionE_xit.setObjectName(_fromUtf8("actionE_xit"))
        self.menu_File.addAction(self.actionE_xit)
        self.menu_Database.addAction(self.action_Create_Backup)
        self.menu_Database.addAction(self.action_Load_Backup)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Schedule.menuAction())
        self.menubar.addAction(self.menu_Database.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Arts Festival Organizer", None))
        self.label_2.setText(_translate("MainWindow", "Participants", None))
        item = self.participantTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.participantTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.participantTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First Name", None))
        item = self.participantTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.participantTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Group Name", None))
        item = self.participantTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Group Piece Title", None))
        item = self.participantTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date of Birth", None))
        item = self.participantTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Age as of Jan. 1", None))
        item = self.participantTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Avg. Age/Level/Grade", None))
        item = self.participantTableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "List of Particpants", None))
        item = self.participantTableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Mailing Address", None))
        item = self.participantTableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Home Phone", None))
        item = self.participantTableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Cell Phone", None))
        item = self.participantTableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Email", None))
        __sortingEnabled = self.participantTableWidget.isSortingEnabled()
        self.participantTableWidget.setSortingEnabled(False)
        item = self.participantTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Diana", None))
        item = self.participantTableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Carrier", None))
        item = self.participantTableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "11/03/1991", None))
        item = self.participantTableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "24", None))
        item = self.participantTableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "Box 1946, Stonewall, MB, R0C 2Z0", None))
        item = self.participantTableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "467-5761", None))
        item = self.participantTableWidget.item(0, 11)
        item.setText(_translate("MainWindow", "umcarr77@gmail.com", None))
        item = self.participantTableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "SCI High School Band", None))
        item = self.participantTableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "Take Five", None))
        item = self.participantTableWidget.item(1, 6)
        item.setText(_translate("MainWindow", "12", None))
        self.participantTableWidget.setSortingEnabled(__sortingEnabled)
        self.addParticipantBtn.setText(_translate("MainWindow", "Add New Participant", None))
        self.editParticipantBtn.setText(_translate("MainWindow", "Edit Participant", None))
        self.label_3.setText(_translate("MainWindow", "Teachers", None))
        item = self.teacherTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.teacherTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.teacherTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "First Name", None))
        item = self.teacherTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Last Name", None))
        item = self.teacherTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mailing Address", None))
        item = self.teacherTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Daytime Phone", None))
        item = self.teacherTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Evening Phone", None))
        item = self.teacherTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Email", None))
        __sortingEnabled = self.teacherTableWidget.isSortingEnabled()
        self.teacherTableWidget.setSortingEnabled(False)
        item = self.teacherTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "May", None))
        item = self.teacherTableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Dupname", None))
        item = self.teacherTableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "123 Somewhere St., Stonewall, MB. R0C 2Z0", None))
        item = self.teacherTableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "555-1234", None))
        item = self.teacherTableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "555-4321", None))
        item = self.teacherTableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "may.dupname@gmail.com", None))
        item = self.teacherTableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Don", None))
        item = self.teacherTableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Horbas", None))
        item = self.teacherTableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Somewhere", None))
        item = self.teacherTableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "555-1234", None))
        item = self.teacherTableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "5555-4321", None))
        item = self.teacherTableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "you.get@the.idea", None))
        self.teacherTableWidget.setSortingEnabled(__sortingEnabled)
        self.addTeacherBtn.setText(_translate("MainWindow", "Add New Teacher", None))
        self.editTeacherBtn.setText(_translate("MainWindow", "Edit Teacher", None))
        self.label_4.setText(_translate("MainWindow", "Entries", None))
        item = self.entryTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.entryTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.entryTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Participant", None))
        item = self.entryTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Teacher", None))
        item = self.entryTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Discipline", None))
        item = self.entryTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Class Number", None))
        item = self.entryTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Class Name", None))
        item = self.entryTableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Instrument", None))
        item = self.entryTableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Special Scheduling Requirements", None))
        __sortingEnabled = self.entryTableWidget.isSortingEnabled()
        self.entryTableWidget.setSortingEnabled(False)
        item = self.entryTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Diana Carrier", None))
        item = self.entryTableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "May Dupname", None))
        item = self.entryTableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Instrumental", None))
        item = self.entryTableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "AB 1234", None))
        item = self.entryTableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "Trumpet Solo", None))
        item = self.entryTableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "Trumpet", None))
        item = self.entryTableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "SCI High School Band", None))
        item = self.entryTableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Don Horbas", None))
        item = self.entryTableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Band", None))
        item = self.entryTableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "BA 1234", None))
        item = self.entryTableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "Something Jazzy", None))
        self.entryTableWidget.setSortingEnabled(__sortingEnabled)
        self.addEntryBtn.setText(_translate("MainWindow", "Add New Entry", None))
        self.editEntryBtn.setText(_translate("MainWindow", "Edit Entry", None))
        self.label.setText(_translate("MainWindow", "Pieces", None))
        item = self.pieceTableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1", None))
        item = self.pieceTableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2", None))
        item = self.pieceTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title", None))
        item = self.pieceTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title of Musical/Opera/Oratorio", None))
        item = self.pieceTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Composter/Arranger/Author", None))
        item = self.pieceTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Performance Time", None))
        __sortingEnabled = self.pieceTableWidget.isSortingEnabled()
        self.pieceTableWidget.setSortingEnabled(False)
        item = self.pieceTableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Take Five", None))
        item = self.pieceTableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "Some Guy", None))
        item = self.pieceTableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "2:00", None))
        item = self.pieceTableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Children of Sanchez", None))
        item = self.pieceTableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "Some Otherguy", None))
        item = self.pieceTableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "2:30", None))
        self.pieceTableWidget.setSortingEnabled(__sortingEnabled)
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Schedule.setTitle(_translate("MainWindow", "&Schedule", None))
        self.menu_Database.setTitle(_translate("MainWindow", "&Database", None))
        self.action_Create_Backup.setText(_translate("MainWindow", "&Create Backup", None))
        self.action_Load_Backup.setText(_translate("MainWindow", "&Load Backup", None))
        self.actionE_xit.setText(_translate("MainWindow", "E&xit", None))

