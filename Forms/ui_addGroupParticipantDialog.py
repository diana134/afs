# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addGroupParticipantDialog.ui'
#
# Created: Mon Aug 11 16:23:55 2014
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
        AddGroupParticipantDialog.resize(400, 331)
        self.gridLayout = QtGui.QGridLayout(AddGroupParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
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
        self.averageAgeLineEdit.setObjectName(_fromUtf8("averageAgeLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.averageAgeLineEdit)
        self.groupBox = QtGui.QGroupBox(AddGroupParticipantDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.name1Label = QtGui.QLabel(self.groupBox)
        self.name1Label.setObjectName(_fromUtf8("name1Label"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.name1Label)
        self.name1LineEdit = QtGui.QLineEdit(self.groupBox)
        self.name1LineEdit.setObjectName(_fromUtf8("name1LineEdit"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.name1LineEdit)
        self.name2Label = QtGui.QLabel(self.groupBox)
        self.name2Label.setObjectName(_fromUtf8("name2Label"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.LabelRole, self.name2Label)
        self.name2LineEdit = QtGui.QLineEdit(self.groupBox)
        self.name2LineEdit.setObjectName(_fromUtf8("name2LineEdit"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.FieldRole, self.name2LineEdit)
        self.name3Label = QtGui.QLabel(self.groupBox)
        self.name3Label.setObjectName(_fromUtf8("name3Label"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.name3Label)
        self.name3LineEdit = QtGui.QLineEdit(self.groupBox)
        self.name3LineEdit.setObjectName(_fromUtf8("name3LineEdit"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.name3LineEdit)
        self.name4Label = QtGui.QLabel(self.groupBox)
        self.name4Label.setObjectName(_fromUtf8("name4Label"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.name4Label)
        self.name4LineEdit = QtGui.QLineEdit(self.groupBox)
        self.name4LineEdit.setObjectName(_fromUtf8("name4LineEdit"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.name4LineEdit)
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 2)
        self.cancelBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 1, 0, 1, 1)
        self.addParticipantBtn = QtGui.QPushButton(AddGroupParticipantDialog)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.gridLayout.addWidget(self.addParticipantBtn, 1, 1, 1, 1)

        self.retranslateUi(AddGroupParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(AddGroupParticipantDialog)

    def retranslateUi(self, AddGroupParticipantDialog):
        AddGroupParticipantDialog.setWindowTitle(QtGui.QApplication.translate("AddGroupParticipantDialog", "Add Group Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.groupNameLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Group Name", None, QtGui.QApplication.UnicodeUTF8))
        self.groupSizeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Group Size", None, QtGui.QApplication.UnicodeUTF8))
        self.schoolGradeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "School Grade", None, QtGui.QApplication.UnicodeUTF8))
        self.averageAgeLabel.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Average Age", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AddGroupParticipantDialog", "Participant Names (if 4 or fewer)", None, QtGui.QApplication.UnicodeUTF8))
        self.name1Label.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Name 1", None, QtGui.QApplication.UnicodeUTF8))
        self.name2Label.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Name 2", None, QtGui.QApplication.UnicodeUTF8))
        self.name3Label.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Name 3", None, QtGui.QApplication.UnicodeUTF8))
        self.name4Label.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Name 4", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.addParticipantBtn.setText(QtGui.QApplication.translate("AddGroupParticipantDialog", "Add &Participant", None, QtGui.QApplication.UnicodeUTF8))

