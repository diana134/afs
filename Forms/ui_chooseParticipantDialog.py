# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseParticipantDialog.ui'
#
# Created: Sun Jan 31 03:09:04 2016
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

class Ui_ChooseParticipantDialog(object):
    def setupUi(self, ChooseParticipantDialog):
        ChooseParticipantDialog.setObjectName(_fromUtf8("ChooseParticipantDialog"))
        ChooseParticipantDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ChooseParticipantDialog.resize(862, 320)
        self.verticalLayout = QtGui.QVBoxLayout(ChooseParticipantDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.participantTableView = QtGui.QTableView(ChooseParticipantDialog)
        self.participantTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.participantTableView.setAlternatingRowColors(True)
        self.participantTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.participantTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.participantTableView.setSortingEnabled(True)
        self.participantTableView.setObjectName(_fromUtf8("participantTableView"))
        self.participantTableView.horizontalHeader().setSortIndicatorShown(True)
        self.participantTableView.verticalHeader().setSortIndicatorShown(False)
        self.participantTableView.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.participantTableView)
        self.btnBox = QtGui.QDialogButtonBox(ChooseParticipantDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ChooseParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(ChooseParticipantDialog)

    def retranslateUi(self, ChooseParticipantDialog):
        ChooseParticipantDialog.setWindowTitle(_translate("ChooseParticipantDialog", "Choose Participant", None))

