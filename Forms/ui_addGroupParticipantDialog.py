# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addGroupParticipantDialog.ui'
#
# Created: Thu Nov 20 11:37:09 2014
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
        AddGroupParticipantDialog.resize(402, 480)
        self.gridLayout = QtGui.QGridLayout(AddGroupParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.cancelBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 1, 1, 1, 1)
        self.addParticipantBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.addParticipantBtn.setDefault(True)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.gridLayout.addWidget(self.addParticipantBtn, 1, 2, 1, 1)
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
        self.chooseP4Btn = QtGui.QPushButton(self.groupBox)
        self.chooseP4Btn.setObjectName(_fromUtf8("chooseP4Btn"))
        self.horizontalLayout_5.addWidget(self.chooseP4Btn)
        self.createNewP4Btn = QtGui.QPushButton(self.groupBox)
        self.createNewP4Btn.setObjectName(_fromUtf8("createNewP4Btn"))
        self.horizontalLayout_5.addWidget(self.createNewP4Btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 3)

        self.retranslateUi(AddGroupParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGroupParticipantDialog)

    def retranslateUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setWindowTitle(_translate("AddGroupParticipantDialog", "Add Group Participant", None))
        self.cancelBtn.setText(_translate("AddGroupParticipantDialog", "&Cancel", None))
        self.addParticipantBtn.setText(_translate("AddGroupParticipantDialog", "A&dd Participant", None))
        self.groupNameLabel.setText(_translate("AddGroupParticipantDialog", "Group Name", None))
        self.groupSizeLabel.setText(_translate("AddGroupParticipantDialog", "Group Size", None))
        self.schoolGradeLabel.setText(_translate("AddGroupParticipantDialog", "School Grade", None))
        self.averageAgeLabel.setText(_translate("AddGroupParticipantDialog", "Average Age", None))
        self.groupBox.setTitle(_translate("AddGroupParticipantDialog", "Participants (if 4 or fewer)", None))
        self.chooseP1Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP1Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP2Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP2Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP3Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP3Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))
        self.chooseP4Btn.setText(_translate("AddGroupParticipantDialog", "Choose...", None))
        self.createNewP4Btn.setText(_translate("AddGroupParticipantDialog", "Create New...", None))

