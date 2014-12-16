# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseEntryDialog.ui'
#
# Created: Sun Dec 14 21:16:58 2014
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

class Ui_ChooseEntryDialog(object):
    def setupUi(self, ChooseEntryDialog):
        ChooseEntryDialog.setObjectName(_fromUtf8("ChooseEntryDialog"))
        ChooseEntryDialog.resize(820, 320)
        self.verticalLayout = QtGui.QVBoxLayout(ChooseEntryDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.entryTableView = QtGui.QTableView(ChooseEntryDialog)
        self.entryTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.entryTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.entryTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.entryTableView.setObjectName(_fromUtf8("entryTableView"))
        self.verticalLayout.addWidget(self.entryTableView)
        self.btnBox = QtGui.QDialogButtonBox(ChooseEntryDialog)
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ChooseEntryDialog)
        QtCore.QObject.connect(self.btnBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseEntryDialog.accept)
        QtCore.QObject.connect(self.btnBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseEntryDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseEntryDialog)

    def retranslateUi(self, ChooseEntryDialog):
        ChooseEntryDialog.setWindowTitle(_translate("ChooseEntryDialog", "Choose Entry", None))

