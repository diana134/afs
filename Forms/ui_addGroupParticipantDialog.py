# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addGroupParticipantDialog.ui'
#
# Created: Sun Jan 11 12:52:13 2015
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

class Ui_AddGroupParticipantDialog(object):
    def setupUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setObjectName(_fromUtf8("AddGroupParticipantDialog"))
        AddGroupParticipantDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddGroupParticipantDialog.resize(459, 423)
        self.gridLayout = QtGui.QGridLayout(AddGroupParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.groupNameLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.groupNameLabel.setObjectName(_fromUtf8("groupNameLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupNameLabel)
        self.groupNameLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.groupNameLineEdit.setObjectName(_fromUtf8("groupNameLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.groupNameLineEdit)
        self.groupSizeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.groupSizeLabel.setObjectName(_fromUtf8("groupSizeLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.groupSizeLabel)
        self.groupSizeLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.groupSizeLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.groupSizeLineEdit.setObjectName(_fromUtf8("groupSizeLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.groupSizeLineEdit)
        self.schoolGradeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.schoolGradeLabel.setObjectName(_fromUtf8("schoolGradeLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.schoolGradeLabel)
        self.schoolGradeLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.schoolGradeLineEdit.setObjectName(_fromUtf8("schoolGradeLineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.schoolGradeLineEdit)
        self.averageAgeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.averageAgeLabel.setObjectName(_fromUtf8("averageAgeLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.averageAgeLabel)
        self.averageAgeLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.averageAgeLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.averageAgeLineEdit.setObjectName(_fromUtf8("averageAgeLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.averageAgeLineEdit)
        self.contactPersonLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.contactPersonLabel.setObjectName(_fromUtf8("contactPersonLabel"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.contactPersonLabel)
        self.contactPersonLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.contactPersonLineEdit.setEnabled(False)
        self.contactPersonLineEdit.setObjectName(_fromUtf8("contactPersonLineEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.contactPersonLineEdit)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.chooseContactBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.chooseContactBtn.setObjectName(_fromUtf8("chooseContactBtn"))
        self.horizontalLayout_9.addWidget(self.chooseContactBtn)
        self.createContactBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.createContactBtn.setObjectName(_fromUtf8("createContactBtn"))
        self.horizontalLayout_9.addWidget(self.createContactBtn)
        self.formLayout_2.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.earliestPerformanceTimeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.earliestPerformanceTimeLabel.setObjectName(_fromUtf8("earliestPerformanceTimeLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.earliestPerformanceTimeLabel)
        self.earliestPerformanceTimeTimeEdit = QtGui.QTimeEdit(AddGroupParticipantDialog)
        self.earliestPerformanceTimeTimeEdit.setTime(QtCore.QTime(9, 0, 0))
        self.earliestPerformanceTimeTimeEdit.setObjectName(_fromUtf8("earliestPerformanceTimeTimeEdit"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.earliestPerformanceTimeTimeEdit)
        self.latestPerformanceTimeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.latestPerformanceTimeLabel.setObjectName(_fromUtf8("latestPerformanceTimeLabel"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.latestPerformanceTimeLabel)
        self.latestPerformanceTimeTimeEdit = QtGui.QTimeEdit(AddGroupParticipantDialog)
        self.latestPerformanceTimeTimeEdit.setTime(QtCore.QTime(15, 0, 0))
        self.latestPerformanceTimeTimeEdit.setObjectName(_fromUtf8("latestPerformanceTimeTimeEdit"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.latestPerformanceTimeTimeEdit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 3)
        self.cancelBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 3, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.addParticipantBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.addParticipantBtn.setDefault(True)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.gridLayout.addWidget(self.addParticipantBtn, 3, 2, 1, 1)
        self.participantTabWidget = QtGui.QTabWidget(AddGroupParticipantDialog)
        self.participantTabWidget.setObjectName(_fromUtf8("participantTabWidget"))
        self.gridLayout.addWidget(self.participantTabWidget, 2, 0, 1, 3)

        self.retranslateUi(AddGroupParticipantDialog)
        self.participantTabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(AddGroupParticipantDialog)
        AddGroupParticipantDialog.setTabOrder(self.groupNameLineEdit, self.groupSizeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.groupSizeLineEdit, self.schoolGradeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.schoolGradeLineEdit, self.averageAgeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.averageAgeLineEdit, self.chooseContactBtn)
        AddGroupParticipantDialog.setTabOrder(self.chooseContactBtn, self.createContactBtn)
        AddGroupParticipantDialog.setTabOrder(self.createContactBtn, self.addParticipantBtn)
        AddGroupParticipantDialog.setTabOrder(self.addParticipantBtn, self.cancelBtn)
        AddGroupParticipantDialog.setTabOrder(self.cancelBtn, self.contactPersonLineEdit)

    def retranslateUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setWindowTitle(_translate("AddGroupParticipantDialog", "Add Group Participant", None))
        self.groupNameLabel.setText(_translate("AddGroupParticipantDialog", "Group Name", None))
        self.groupSizeLabel.setText(_translate("AddGroupParticipantDialog", "Number of Participants", None))
        self.schoolGradeLabel.setText(_translate("AddGroupParticipantDialog", "School Grade", None))
        self.averageAgeLabel.setText(_translate("AddGroupParticipantDialog", "Average Age", None))
        self.contactPersonLabel.setText(_translate("AddGroupParticipantDialog", "Contact Person", None))
        self.chooseContactBtn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createContactBtn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.earliestPerformanceTimeLabel.setText(_translate("AddGroupParticipantDialog", "Earliest Performance Time", None))
        self.latestPerformanceTimeLabel.setText(_translate("AddGroupParticipantDialog", "Latest Performance Time", None))
        self.cancelBtn.setText(_translate("AddGroupParticipantDialog", "&Cancel", None))
        self.addParticipantBtn.setText(_translate("AddGroupParticipantDialog", "A&dd Participant", None))

