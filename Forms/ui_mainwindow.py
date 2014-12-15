# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Sun Dec 14 16:51:38 2014
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
        MainWindow.resize(384, 291)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.makeScheduleBtn = QtGui.QPushButton(self.centralwidget)
        self.makeScheduleBtn.setObjectName(_fromUtf8("makeScheduleBtn"))
        self.gridLayout.addWidget(self.makeScheduleBtn, 2, 0, 1, 1)
        self.addSoloParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.addSoloParticipantBtn.setObjectName(_fromUtf8("addSoloParticipantBtn"))
        self.gridLayout.addWidget(self.addSoloParticipantBtn, 0, 0, 1, 1)
        self.addEntryBtn = QtGui.QPushButton(self.centralwidget)
        self.addEntryBtn.setObjectName(_fromUtf8("addEntryBtn"))
        self.gridLayout.addWidget(self.addEntryBtn, 1, 1, 1, 1)
        self.loadScheduleBtn = QtGui.QPushButton(self.centralwidget)
        self.loadScheduleBtn.setObjectName(_fromUtf8("loadScheduleBtn"))
        self.gridLayout.addWidget(self.loadScheduleBtn, 2, 1, 1, 1)
        self.addTeacherBtn = QtGui.QPushButton(self.centralwidget)
        self.addTeacherBtn.setObjectName(_fromUtf8("addTeacherBtn"))
        self.gridLayout.addWidget(self.addTeacherBtn, 1, 0, 1, 1)
        self.addGroupParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.addGroupParticipantBtn.setObjectName(_fromUtf8("addGroupParticipantBtn"))
        self.gridLayout.addWidget(self.addGroupParticipantBtn, 0, 1, 1, 1)
        self.editParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.editParticipantBtn.setObjectName(_fromUtf8("editParticipantBtn"))
        self.gridLayout.addWidget(self.editParticipantBtn, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Arts Festival Scheduler", None))
        self.makeScheduleBtn.setText(_translate("MainWindow", "&Make Schedule", None))
        self.addSoloParticipantBtn.setText(_translate("MainWindow", "Add &Solo Participant", None))
        self.addEntryBtn.setText(_translate("MainWindow", "Add &Entry", None))
        self.loadScheduleBtn.setText(_translate("MainWindow", "&Load Schedule", None))
        self.addTeacherBtn.setText(_translate("MainWindow", "Add &Teacher", None))
        self.addGroupParticipantBtn.setText(_translate("MainWindow", "Add &Group Participant", None))
        self.editParticipantBtn.setText(_translate("MainWindow", "E&dit Participant", None))

