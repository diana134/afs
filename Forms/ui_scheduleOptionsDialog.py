# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheduleOptionsDialog.ui'
#
# Created: Thu Oct 23 17:18:47 2014
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
        scheduleOptionsDialog.resize(390, 374)
        self.verticalLayout_2 = QtGui.QVBoxLayout(scheduleOptionsDialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox_2 = QtGui.QGroupBox(scheduleOptionsDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.timeToWriteCommentsLabel = QtGui.QLabel(self.groupBox_2)
        self.timeToWriteCommentsLabel.setObjectName(_fromUtf8("timeToWriteCommentsLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.timeToWriteCommentsLabel)
        self.commentsTimeEdit = QtGui.QTimeEdit(self.groupBox_2)
        self.commentsTimeEdit.setObjectName(_fromUtf8("commentsTimeEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.commentsTimeEdit)
        self.adjudicationTimePerEntryLabel = QtGui.QLabel(self.groupBox_2)
        self.adjudicationTimePerEntryLabel.setObjectName(_fromUtf8("adjudicationTimePerEntryLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.adjudicationTimePerEntryLabel)
        self.adjudicationTimeEdit = QtGui.QTimeEdit(self.groupBox_2)
        self.adjudicationTimeEdit.setObjectName(_fromUtf8("adjudicationTimeEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.adjudicationTimeEdit)
        self.toleranceForOvertimeLabel = QtGui.QLabel(self.groupBox_2)
        self.toleranceForOvertimeLabel.setObjectName(_fromUtf8("toleranceForOvertimeLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.toleranceForOvertimeLabel)
        self.toleranceTimeEdit = QtGui.QTimeEdit(self.groupBox_2)
        self.toleranceTimeEdit.setObjectName(_fromUtf8("toleranceTimeEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.toleranceTimeEdit)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(scheduleOptionsDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.sessionStartDateTimeEdit = QtGui.QDateTimeEdit(self.groupBox)
        self.sessionStartDateTimeEdit.setCalendarPopup(True)
        self.sessionStartDateTimeEdit.setObjectName(_fromUtf8("sessionStartDateTimeEdit"))
        self.horizontalLayout_4.addWidget(self.sessionStartDateTimeEdit)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.sessionEndDateTimeEdit = QtGui.QDateTimeEdit(self.groupBox)
        self.sessionEndDateTimeEdit.setCalendarPopup(True)
        self.sessionEndDateTimeEdit.setObjectName(_fromUtf8("sessionEndDateTimeEdit"))
        self.horizontalLayout_4.addWidget(self.sessionEndDateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addSessionBtn = QtGui.QPushButton(self.groupBox)
        self.addSessionBtn.setObjectName(_fromUtf8("addSessionBtn"))
        self.horizontalLayout.addWidget(self.addSessionBtn)
        self.deleteSessionBtn = QtGui.QPushButton(self.groupBox)
        self.deleteSessionBtn.setObjectName(_fromUtf8("deleteSessionBtn"))
        self.horizontalLayout.addWidget(self.deleteSessionBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sessionListWidget = QtGui.QListWidget(self.groupBox)
        self.sessionListWidget.setObjectName(_fromUtf8("sessionListWidget"))
        self.verticalLayout.addWidget(self.sessionListWidget)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(scheduleOptionsDialog)
        QtCore.QMetaObject.connectSlotsByName(scheduleOptionsDialog)

    def retranslateUi(self, scheduleOptionsDialog):
        scheduleOptionsDialog.setWindowTitle(_translate("scheduleOptionsDialog", "Schedule Options", None))
        self.groupBox_2.setTitle(_translate("scheduleOptionsDialog", "Timing Options", None))
        self.timeToWriteCommentsLabel.setToolTip(_translate("scheduleOptionsDialog", "The time between entries in a class while the adjudicator writes comments.", None))
        self.timeToWriteCommentsLabel.setText(_translate("scheduleOptionsDialog", "Time to Write Comments PerEntry", None))
        self.commentsTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.adjudicationTimePerEntryLabel.setToolTip(_translate("scheduleOptionsDialog", "The time at the end of the class to adjudicate each of the entries.", None))
        self.adjudicationTimePerEntryLabel.setText(_translate("scheduleOptionsDialog", "Adjudication Time Per Entry", None))
        self.adjudicationTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.toleranceForOvertimeLabel.setToolTip(_translate("scheduleOptionsDialog", "The time past the end of the session entries can be allowed to run.", None))
        self.toleranceForOvertimeLabel.setText(_translate("scheduleOptionsDialog", "Tolerance for Overtime", None))
        self.toleranceTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "HH:mm", None))
        self.groupBox.setTitle(_translate("scheduleOptionsDialog", "Session Dates and Times", None))
        self.label.setText(_translate("scheduleOptionsDialog", "Start", None))
        self.sessionStartDateTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "yyyy/M/d h:mm AP", None))
        self.label_2.setText(_translate("scheduleOptionsDialog", "End", None))
        self.sessionEndDateTimeEdit.setDisplayFormat(_translate("scheduleOptionsDialog", "yyyy/M/d h:mm AP", None))
        self.addSessionBtn.setText(_translate("scheduleOptionsDialog", "&Add Session", None))
        self.deleteSessionBtn.setText(_translate("scheduleOptionsDialog", "&Delete Session", None))

