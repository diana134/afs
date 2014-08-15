# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addGroupParticipantDialog.ui'
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

class Ui_AddGroupParticipantDialog(object):
    def setupUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setObjectName(_fromUtf8("AddGroupParticipantDialog"))
        AddGroupParticipantDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddGroupParticipantDialog.resize(358, 202)
        self.gridLayout = QtGui.QGridLayout(AddGroupParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addParticipantBtn = QtGui.QPushButton(AddGroupParticipantDialog)
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
        self.participantsLabel = QtGui.QLabel(AddGroupParticipantDialog)
        self.participantsLabel.setObjectName(_fromUtf8("participantsLabel"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.participantsLabel)
        self.participantsLineEdit = QtGui.QLineEdit(AddGroupParticipantDialog)
        self.participantsLineEdit.setReadOnly(False)
        self.participantsLineEdit.setObjectName(_fromUtf8("participantsLineEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.participantsLineEdit)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 3)

        self.retranslateUi(AddGroupParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGroupParticipantDialog)

    def retranslateUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setWindowTitle(QtGui.QApplication.translate("AddGroupParticipantDialog", "Add Group Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.addParticipantBtn.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "A&dd Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupNameLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Group Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupSizeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Group Size", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolGradeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "School Grade", None, QtGui.QApplication.UnicodeUTF8))
        self.averageAgeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Average Age", None, QtGui.QApplication.UnicodeUTF8))
        self.participantsLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Participants", None, QtGui.QApplication.UnicodeUTF8))
        self.participantsLineEdit.setPlaceholderText(QtGui.QApplication.translate("AddGroupParticipantDialog", "only if 4 or fewer; commas (,) between names", None, QtGui.QApplication.UnicodeUTF8))

