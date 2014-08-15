# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Fri Aug 15 01:37:03 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(384, 291)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addGroupParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.addGroupParticipantBtn.setObjectName(_fromUtf8("addGroupParticipantBtn"))
        self.gridLayout.addWidget(self.addGroupParticipantBtn, 0, 1, 1, 1)
        self.addSoloParticipantBtn = QtGui.QPushButton(self.centralwidget)
        self.addSoloParticipantBtn.setObjectName(_fromUtf8("addSoloParticipantBtn"))
        self.gridLayout.addWidget(self.addSoloParticipantBtn, 0, 0, 1, 1)
        self.addTeacherBtn = QtGui.QPushButton(self.centralwidget)
        self.addTeacherBtn.setObjectName(_fromUtf8("addTeacherBtn"))
        self.gridLayout.addWidget(self.addTeacherBtn, 1, 0, 1, 1)
        self.addEntryBtn = QtGui.QPushButton(self.centralwidget)
        self.addEntryBtn.setObjectName(_fromUtf8("addEntryBtn"))
        self.gridLayout.addWidget(self.addEntryBtn, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Arts Festival Scheduler", None, QtGui.QApplication.UnicodeUTF8))
        self.addGroupParticipantBtn.setText(QtGui.QApplication.translate("MainWindow", "Add &Group Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.addSoloParticipantBtn.setText(QtGui.QApplication.translate("MainWindow", "Add &Solo Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.addTeacherBtn.setText(QtGui.QApplication.translate("MainWindow", "Add &Teacher", None, QtGui.QApplication.UnicodeUTF8))
        self.addEntryBtn.setText(QtGui.QApplication.translate("MainWindow", "Add &Entry", None, QtGui.QApplication.UnicodeUTF8))

