# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addGroupParticipantDialog.ui'
#
# Created: Tue Jan  6 20:54:02 2015
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
        AddGroupParticipantDialog.resize(459, 601)
        self.gridLayout = QtGui.QGridLayout(AddGroupParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addParticipantBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.addParticipantBtn.setDefault(True)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.gridLayout.addWidget(self.addParticipantBtn, 1, 2, 1, 1)
        self.cancelBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
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
        self.groupBox = QtGui.QGroupBox(AddGroupParticipantDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.p1LineEdit = QtGui.QLineEdit(self.groupBox)
        self.p1LineEdit.setEnabled(False)
        self.p1LineEdit.setObjectName(_fromUtf8("p1LineEdit"))
        self.verticalLayout_9.addWidget(self.p1LineEdit)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.chooseP1Btn = QtGui.QPushButton(self.groupBox)
        self.chooseP1Btn.setObjectName(_fromUtf8("chooseP1Btn"))
        self.horizontalLayout_8.addWidget(self.chooseP1Btn)
        self.createNewP1Btn = QtGui.QPushButton(self.groupBox)
        self.createNewP1Btn.setObjectName(_fromUtf8("createNewP1Btn"))
        self.horizontalLayout_8.addWidget(self.createNewP1Btn)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.p2LineEdit = QtGui.QLineEdit(self.groupBox)
        self.p2LineEdit.setEnabled(False)
        self.p2LineEdit.setObjectName(_fromUtf8("p2LineEdit"))
        self.verticalLayout_8.addWidget(self.p2LineEdit)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.chooseP2Btn = QtGui.QPushButton(self.groupBox)
        self.chooseP2Btn.setObjectName(_fromUtf8("chooseP2Btn"))
        self.horizontalLayout_7.addWidget(self.chooseP2Btn)
        self.createNewP2Btn = QtGui.QPushButton(self.groupBox)
        self.createNewP2Btn.setObjectName(_fromUtf8("createNewP2Btn"))
        self.horizontalLayout_7.addWidget(self.createNewP2Btn)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_10.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.p3LineEdit = QtGui.QLineEdit(self.groupBox)
        self.p3LineEdit.setEnabled(False)
        self.p3LineEdit.setObjectName(_fromUtf8("p3LineEdit"))
        self.verticalLayout_7.addWidget(self.p3LineEdit)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.chooseP3Btn = QtGui.QPushButton(self.groupBox)
        self.chooseP3Btn.setObjectName(_fromUtf8("chooseP3Btn"))
        self.horizontalLayout_6.addWidget(self.chooseP3Btn)
        self.createNewP3Btn = QtGui.QPushButton(self.groupBox)
        self.createNewP3Btn.setObjectName(_fromUtf8("createNewP3Btn"))
        self.horizontalLayout_6.addWidget(self.createNewP3Btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.p4LineEdit = QtGui.QLineEdit(self.groupBox)
        self.p4LineEdit.setEnabled(False)
        self.p4LineEdit.setObjectName(_fromUtf8("p4LineEdit"))
        self.verticalLayout_6.addWidget(self.p4LineEdit)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.chooseP4Btn = QtGui.QPushButton(self.groupBox)
        self.chooseP4Btn.setObjectName(_fromUtf8("chooseP4Btn"))
        self.horizontalLayout_5.addWidget(self.chooseP4Btn)
        self.createNewP4Btn = QtGui.QPushButton(self.groupBox)
        self.createNewP4Btn.setObjectName(_fromUtf8("createNewP4Btn"))
        self.horizontalLayout_5.addWidget(self.createNewP4Btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.latestPerformanceTimeLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.latestPerformanceTimeLabel.setObjectName(_fromUtf8("latestPerformanceTimeLabel"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.latestPerformanceTimeLabel)
        self.latestPerformanceTimeTimeEdit = QtGui.QTimeEdit(AddGroupParticipantDialog)
        self.latestPerformanceTimeTimeEdit.setTime(QtCore.QTime(15, 0, 0))
        self.latestPerformanceTimeTimeEdit.setObjectName(_fromUtf8("latestPerformanceTimeTimeEdit"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.latestPerformanceTimeTimeEdit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 3)

        self.retranslateUi(AddGroupParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGroupParticipantDialog)
        AddGroupParticipantDialog.setTabOrder(self.groupNameLineEdit, self.groupSizeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.groupSizeLineEdit, self.schoolGradeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.schoolGradeLineEdit, self.averageAgeLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.averageAgeLineEdit, self.chooseContactBtn)
        AddGroupParticipantDialog.setTabOrder(self.chooseContactBtn, self.createContactBtn)
        AddGroupParticipantDialog.setTabOrder(self.createContactBtn, self.chooseP1Btn)
        AddGroupParticipantDialog.setTabOrder(self.chooseP1Btn, self.createNewP1Btn)
        AddGroupParticipantDialog.setTabOrder(self.createNewP1Btn, self.chooseP2Btn)
        AddGroupParticipantDialog.setTabOrder(self.chooseP2Btn, self.createNewP2Btn)
        AddGroupParticipantDialog.setTabOrder(self.createNewP2Btn, self.chooseP3Btn)
        AddGroupParticipantDialog.setTabOrder(self.chooseP3Btn, self.createNewP3Btn)
        AddGroupParticipantDialog.setTabOrder(self.createNewP3Btn, self.chooseP4Btn)
        AddGroupParticipantDialog.setTabOrder(self.chooseP4Btn, self.createNewP4Btn)
        AddGroupParticipantDialog.setTabOrder(self.createNewP4Btn, self.addParticipantBtn)
        AddGroupParticipantDialog.setTabOrder(self.addParticipantBtn, self.cancelBtn)
        AddGroupParticipantDialog.setTabOrder(self.cancelBtn, self.p3LineEdit)
        AddGroupParticipantDialog.setTabOrder(self.p3LineEdit, self.p1LineEdit)
        AddGroupParticipantDialog.setTabOrder(self.p1LineEdit, self.contactPersonLineEdit)
        AddGroupParticipantDialog.setTabOrder(self.contactPersonLineEdit, self.p2LineEdit)
        AddGroupParticipantDialog.setTabOrder(self.p2LineEdit, self.p4LineEdit)

    def retranslateUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setWindowTitle(_translate("AddGroupParticipantDialog", "Add Group Participant", None))
        self.addParticipantBtn.setText(_translate("AddGroupParticipantDialog", "A&dd Participant", None))
        self.cancelBtn.setText(_translate("AddGroupParticipantDialog", "&Cancel", None))
        self.groupNameLabel.setText(_translate("AddGroupParticipantDialog", "Group Name", None))
        self.groupSizeLabel.setText(_translate("AddGroupParticipantDialog", "Number of Participants", None))
        self.schoolGradeLabel.setText(_translate("AddGroupParticipantDialog", "School Grade", None))
        self.averageAgeLabel.setText(_translate("AddGroupParticipantDialog", "Average Age", None))
        self.contactPersonLabel.setText(_translate("AddGroupParticipantDialog", "Contact Person", None))
        self.chooseContactBtn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createContactBtn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.earliestPerformanceTimeLabel.setText(_translate("AddGroupParticipantDialog", "Earliest Performance Time", None))
        self.groupBox.setTitle(_translate("AddGroupParticipantDialog", "Participants (if 4 or fewer)", None))
        self.chooseP1Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP1Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP2Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP2Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP3Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP3Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP4Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP4Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.latestPerformanceTimeLabel.setText(_translate("AddGroupParticipantDialog", "Latest Performance Time", None))

