# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Tue Jan 13 20:52:24 2015
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
        MainWindow.resize(407, 376)
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.addSoloParticipantBtn = QtGui.QPushButton(self.groupBox)
        self.addSoloParticipantBtn.setObjectName(_fromUtf8("addSoloParticipantBtn"))
        self.verticalLayout.addWidget(self.addSoloParticipantBtn)
        self.addGroupParticipantBtn = QtGui.QPushButton(self.groupBox)
        self.addGroupParticipantBtn.setObjectName(_fromUtf8("addGroupParticipantBtn"))
        self.verticalLayout.addWidget(self.addGroupParticipantBtn)
        self.editParticipantBtn = QtGui.QPushButton(self.groupBox)
        self.editParticipantBtn.setObjectName(_fromUtf8("editParticipantBtn"))
        self.verticalLayout.addWidget(self.editParticipantBtn)
        self.deleteParticipantBtn = QtGui.QPushButton(self.groupBox)
        self.deleteParticipantBtn.setObjectName(_fromUtf8("deleteParticipantBtn"))
        self.verticalLayout.addWidget(self.deleteParticipantBtn)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addTeacherBtn = QtGui.QPushButton(self.groupBox_2)
        self.addTeacherBtn.setObjectName(_fromUtf8("addTeacherBtn"))
        self.verticalLayout_2.addWidget(self.addTeacherBtn)
        self.editTeacherBtn = QtGui.QPushButton(self.groupBox_2)
        self.editTeacherBtn.setObjectName(_fromUtf8("editTeacherBtn"))
        self.verticalLayout_2.addWidget(self.editTeacherBtn)
        self.deleteTeacherBtn = QtGui.QPushButton(self.groupBox_2)
        self.deleteTeacherBtn.setObjectName(_fromUtf8("deleteTeacherBtn"))
        self.verticalLayout_2.addWidget(self.deleteTeacherBtn)
        self.gridLayout.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.addEntryBtn = QtGui.QPushButton(self.groupBox_3)
        self.addEntryBtn.setObjectName(_fromUtf8("addEntryBtn"))
        self.verticalLayout_3.addWidget(self.addEntryBtn)
        self.editEntryBtn = QtGui.QPushButton(self.groupBox_3)
        self.editEntryBtn.setObjectName(_fromUtf8("editEntryBtn"))
        self.verticalLayout_3.addWidget(self.editEntryBtn)
        self.deleteEntryBtn = QtGui.QPushButton(self.groupBox_3)
        self.deleteEntryBtn.setObjectName(_fromUtf8("deleteEntryBtn"))
        self.verticalLayout_3.addWidget(self.deleteEntryBtn)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.makeScheduleBtn = QtGui.QPushButton(self.groupBox_4)
        self.makeScheduleBtn.setObjectName(_fromUtf8("makeScheduleBtn"))
        self.verticalLayout_4.addWidget(self.makeScheduleBtn)
        self.loadScheduleBtn = QtGui.QPushButton(self.groupBox_4)
        self.loadScheduleBtn.setObjectName(_fromUtf8("loadScheduleBtn"))
        self.verticalLayout_4.addWidget(self.loadScheduleBtn)
        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backupDbBtn = QtGui.QPushButton(self.groupBox_5)
        self.backupDbBtn.setObjectName(_fromUtf8("backupDbBtn"))
        self.horizontalLayout.addWidget(self.backupDbBtn)
        self.restoreDbBtn = QtGui.QPushButton(self.groupBox_5)
        self.restoreDbBtn.setObjectName(_fromUtf8("restoreDbBtn"))
        self.horizontalLayout.addWidget(self.restoreDbBtn)
        self.createNewDbBtn = QtGui.QPushButton(self.groupBox_5)
        self.createNewDbBtn.setEnabled(False)
        self.createNewDbBtn.setObjectName(_fromUtf8("createNewDbBtn"))
        self.horizontalLayout.addWidget(self.createNewDbBtn)
        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Arts Festival Scheduler", None))
        self.groupBox.setTitle(_translate("MainWindow", "Participants", None))
        self.addSoloParticipantBtn.setText(_translate("MainWindow", "Add &Solo Participant", None))
        self.addGroupParticipantBtn.setText(_translate("MainWindow", "Add &Group Participant", None))
        self.editParticipantBtn.setText(_translate("MainWindow", "E&dit Participant", None))
        self.deleteParticipantBtn.setText(_translate("MainWindow", "Delete Participant", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Teachers/Contacts", None))
        self.addTeacherBtn.setText(_translate("MainWindow", "Add &Teacher/Contact", None))
        self.editTeacherBtn.setText(_translate("MainWindow", "Ed&it Teacher/Contact", None))
        self.deleteTeacherBtn.setText(_translate("MainWindow", "Delete Teacher/Contact", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Entries", None))
        self.addEntryBtn.setText(_translate("MainWindow", "Add &Entry", None))
        self.editEntryBtn.setText(_translate("MainWindow", "Edit E&ntry", None))
        self.deleteEntryBtn.setText(_translate("MainWindow", "Delete Entry", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Schedules", None))
        self.makeScheduleBtn.setText(_translate("MainWindow", "&Make Schedule", None))
        self.loadScheduleBtn.setText(_translate("MainWindow", "&Load Schedule", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Database", None))
        self.backupDbBtn.setText(_translate("MainWindow", "Backup Database", None))
        self.restoreDbBtn.setText(_translate("MainWindow", "Restore Database", None))
        self.createNewDbBtn.setText(_translate("MainWindow", "Create New Database", None))

