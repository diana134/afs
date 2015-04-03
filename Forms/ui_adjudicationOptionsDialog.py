# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_adjudicationOptionsDialog.ui'
#
# Created: Thu Apr  2 21:57:07 2015
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

class Ui_AdjudicationOptionsDialog(object):
    def setupUi(self, AdjudicationOptionsDialog):
        AdjudicationOptionsDialog.setObjectName(_fromUtf8("AdjudicationOptionsDialog"))
        AdjudicationOptionsDialog.resize(403, 139)
        self.gridLayout = QtGui.QGridLayout(AdjudicationOptionsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBox = QtGui.QDialogButtonBox(AdjudicationOptionsDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.gridLayout.addWidget(self.btnBox, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.locationLabel = QtGui.QLabel(AdjudicationOptionsDialog)
        self.locationLabel.setEnabled(False)
        self.locationLabel.setObjectName(_fromUtf8("locationLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.locationLabel)
        self.locationLineEdit = QtGui.QLineEdit(AdjudicationOptionsDialog)
        self.locationLineEdit.setEnabled(False)
        self.locationLineEdit.setObjectName(_fromUtf8("locationLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.locationLineEdit)
        self.yearLabel = QtGui.QLabel(AdjudicationOptionsDialog)
        self.yearLabel.setEnabled(False)
        self.yearLabel.setObjectName(_fromUtf8("yearLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.yearLabel)
        self.yearLineEdit = QtGui.QLineEdit(AdjudicationOptionsDialog)
        self.yearLineEdit.setEnabled(False)
        self.yearLineEdit.setObjectName(_fromUtf8("yearLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.yearLineEdit)
        self.adjudicatorLabel = QtGui.QLabel(AdjudicationOptionsDialog)
        self.adjudicatorLabel.setObjectName(_fromUtf8("adjudicatorLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.adjudicatorLabel)
        self.adjudicatorLineEdit = QtGui.QLineEdit(AdjudicationOptionsDialog)
        self.adjudicatorLineEdit.setObjectName(_fromUtf8("adjudicatorLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.adjudicatorLineEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.retranslateUi(AdjudicationOptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(AdjudicationOptionsDialog)

    def retranslateUi(self, AdjudicationOptionsDialog):
        AdjudicationOptionsDialog.setWindowTitle(_translate("AdjudicationOptionsDialog", "Adjudication Sheet Options", None))
        self.locationLabel.setText(_translate("AdjudicationOptionsDialog", "Location", None))
        self.yearLabel.setText(_translate("AdjudicationOptionsDialog", "Year", None))
        self.adjudicatorLabel.setText(_translate("AdjudicationOptionsDialog", "Adjudicator", None))

