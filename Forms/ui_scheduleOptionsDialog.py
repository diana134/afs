# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheduleOptionsDialog.ui'
#
# Created: Thu Oct 23 16:56:58 2014
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

class Ui_scheduleOptionsDialog(object):
    def setupUi(self, scheduleOptionsDialog):
        scheduleOptionsDialog.setObjectName(_fromUtf8("scheduleOptionsDialog"))
        scheduleOptionsDialog.resize(685, 202)
        self.horizontalLayout = QtGui.QHBoxLayout(scheduleOptionsDialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.timeToWriteCommentsLabel = QtGui.QLabel(scheduleOptionsDialog)
        self.timeToWriteCommentsLabel.setObjectName(_fromUtf8("timeToWriteCommentsLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.timeToWriteCommentsLabel)
        self.commentsTimeEdit = QtGui.QTimeEdit(scheduleOptionsDialog)
        self.commentsTimeEdit.setObjectName(_fromUtf8("commentsTimeEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.commentsTimeEdit)
        self.adjudicationTimePerEntryLabel = QtGui.QLabel(scheduleOptionsDialog)
        self.adjudicationTimePerEntryLabel.setObjectName(_fromUtf8("adjudicationTimePerEntryLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.adjudicationTimePerEntryLabel)
        self.adjudicationTimeEdit = QtGui.QTimeEdit(scheduleOptionsDialog)
        self.adjudicationTimeEdit.setObjectName(_fromUtf8("adjudicationTimeEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.adjudicationTimeEdit)
        self.toleranceForOvertimeLabel = QtGui.QLabel(scheduleOptionsDialog)
        self.toleranceForOvertimeLabel.setObjectName(_fromUtf8("toleranceForOvertimeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.toleranceForOvertimeLabel)
        self.toleranceTimeEdit = QtGui.QTimeEdit(scheduleOptionsDialog)
        self.toleranceTimeEdit.setObjectName(_fromUtf8("toleranceTimeEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.toleranceTimeEdit)
        self.sessionDateAndTimeLabel = QtGui.QLabel(scheduleOptionsDialog)
        self.sessionDateAndTimeLabel.setObjectName(_fromUtf8("sessionDateAndTimeLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.sessionDateAndTimeLabel)
        self.sessionDateTimeEdit = QtGui.QDateTimeEdit(scheduleOptionsDialog)
        self.sessionDateTimeEdit.setCalendarPopup(True)
        self.sessionDateTimeEdit.setObjectName(_fromUtf8("sessionDateTimeEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sessionDateTimeEdit)
        self.addSessionBtn = QtGui.QPushButton(scheduleOptionsDialog)
        self.addSessionBtn.setObjectName(_fromUtf8("addSessionBtn"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.addSessionBtn)
        self.deleteSessionBtn = QtGui.QPushButton(scheduleOptionsDialog)
        self.deleteSessionBtn.setObjectName(_fromUtf8("deleteSessionBtn"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.deleteSessionBtn)
        self.horizontalLayout.addLayout(self.formLayout)
        self.groupBox = QtGui.QGroupBox(scheduleOptionsDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.sessionListWidget = QtGui.QListWidget(self.groupBox)
        self.sessionListWidget.setObjectName(_fromUtf8("sessionListWidget"))
        self.verticalLayout.addWidget(self.sessionListWidget)
        self.buttonBox = QtGui.QDialogButtonBox(self.groupBox)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(scheduleOptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(scheduleOptionsDialog)

    def retranslateUi(self, scheduleOptionsDialog):
        scheduleOptionsDialog.setWindowTitle(_translate("scheduleOptionsDialog", "Schedule Options", None))
        self.timeToWriteCommentsLabel.setText(_translate("scheduleOptionsDialog", "Time to Write Comments", None))
        self.commentsTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.adjudicationTimePerEntryLabel.setText(_translate("scheduleOptionsDialog", "Adjudication Time Per Entry", None))
        self.adjudicationTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.toleranceForOvertimeLabel.setText(_translate("scheduleOptionsDialog", "Tolerance for Overtime", None))
        self.toleranceTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.sessionDateAndTimeLabel.setText(_translate("scheduleOptionsDialog", "Session Date and Time", None))
        self.sessionDateTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "yyyy/M/d h:mm AP", None))
        self.addSessionBtn.setText(_translate("scheduleOptionsDialog", "&Add Session", None))
        self.deleteSessionBtn.setText(_translate("scheduleOptionsDialog", "&Delete Session", None))
        self.groupBox.setTitle(_translate("scheduleOptionsDialog", "Session Dates and Times", None))

