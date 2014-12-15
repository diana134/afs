# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseParticipantDialog.ui'
#
# Created: Sun Dec 14 16:58:53 2014
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
        ChooseParticipantDialog.resize(876, 400)
        self.verticalLayout = QtGui.QVBoxLayout(ChooseParticipantDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.searchLineEdit = QtGui.QLineEdit(ChooseParticipantDialog)
        self.searchLineEdit.setEnabled(False)
        self.searchLineEdit.setObjectName(_fromUtf8("searchLineEdit"))
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.searchBtn = QtGui.QPushButton(ChooseParticipantDialog)
        self.searchBtn.setEnabled(False)
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.horizontalLayout.addWidget(self.searchBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.participantTypeTabWidget = QtGui.QTabWidget(ChooseParticipantDialog)
        self.participantTypeTabWidget.setObjectName(_fromUtf8("participantTypeTabWidget"))
        self.soloParticipantsTab = QtGui.QWidget()
        self.soloParticipantsTab.setObjectName(_fromUtf8("soloParticipantsTab"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.soloParticipantsTab)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.soloParticipantTableView = QtGui.QTableView(self.soloParticipantsTab)
        self.soloParticipantTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.soloParticipantTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.soloParticipantTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.soloParticipantTableView.setObjectName(_fromUtf8("soloParticipantTableView"))
        self.verticalLayout_3.addWidget(self.soloParticipantTableView)
        self.participantTypeTabWidget.addTab(self.soloParticipantsTab, _fromUtf8(""))
        self.groupParticipantsTab = QtGui.QWidget()
        self.groupParticipantsTab.setObjectName(_fromUtf8("groupParticipantsTab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupParticipantsTab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupParticipantTableView = QtGui.QTableView(self.groupParticipantsTab)
        self.groupParticipantTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.groupParticipantTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.groupParticipantTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.groupParticipantTableView.setObjectName(_fromUtf8("groupParticipantTableView"))
        self.verticalLayout_4.addWidget(self.groupParticipantTableView)
        self.participantTypeTabWidget.addTab(self.groupParticipantsTab, _fromUtf8(""))
        self.verticalLayout.addWidget(self.participantTypeTabWidget)
        self.btnBox = QtGui.QDialogButtonBox(ChooseParticipantDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ChooseParticipantDialog)
        self.participantTypeTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ChooseParticipantDialog)

    def retranslateUi(self, ChooseParticipantDialog):
        ChooseParticipantDialog.setWindowTitle(_translate("ChooseParticipantDialog", "Choose Participant", None))
        self.searchLineEdit.setPlaceholderText(_translate("ChooseParticipantDialog", "Search name...", None))
        self.searchBtn.setText(_translate("ChooseParticipantDialog", "Search", None))
        self.participantTypeTabWidget.setTabText(self.participantTypeTabWidget.indexOf(self.soloParticipantsTab), _translate("ChooseParticipantDialog", "Individuals", None))
        self.participantTypeTabWidget.setTabText(self.participantTypeTabWidget.indexOf(self.groupParticipantsTab), _translate("ChooseParticipantDialog", "Groups", None))

