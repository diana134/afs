# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addEntryDialog.ui'
#
# Created: Sun Nov 30 17:55:37 2014
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

class Ui_AddEntryDialog(object):
    def setupUi(self, AddEntryDialog):
        AddEntryDialog.setObjectName(_fromUtf8("AddEntryDialog"))
        AddEntryDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        AddEntryDialog.resize(546, 508)
        self.gridLayout = QtGui.QGridLayout(AddEntryDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addEntryBtn = QtGui.QPushButton(AddEntryDialog)
        self.addEntryBtn.setAutoDefault(False)
        self.addEntryBtn.setDefault(True)
        self.addEntryBtn.setObjectName(_fromUtf8("addEntryBtn"))
        self.gridLayout.addWidget(self.addEntryBtn, 3, 3, 1, 1)
        self.cancelBtn = QtGui.QPushButton(AddEntryDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 3, 2, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.participantLabel = QtGui.QLabel(AddEntryDialog)
        self.participantLabel.setObjectName(_fromUtf8("participantLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.participantLabel)
        self.participantLineEdit = QtGui.QLineEdit(AddEntryDialog)
        self.participantLineEdit.setEnabled(False)
        self.participantLineEdit.setObjectName(_fromUtf8("participantLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.participantLineEdit)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.chooseParticipantBtn = QtGui.QPushButton(AddEntryDialog)
        self.chooseParticipantBtn.setEnabled(True)
        self.chooseParticipantBtn.setObjectName(_fromUtf8("chooseParticipantBtn"))
        self.gridLayout_2.addWidget(self.chooseParticipantBtn, 0, 0, 1, 1)
        self.createNewSoloParticipantBtn = QtGui.QPushButton(AddEntryDialog)
        self.createNewSoloParticipantBtn.setObjectName(_fromUtf8("createNewSoloParticipantBtn"))
        self.gridLayout_2.addWidget(self.createNewSoloParticipantBtn, 0, 1, 1, 1)
        self.createNewGroupParticipantBtn = QtGui.QPushButton(AddEntryDialog)
        self.createNewGroupParticipantBtn.setObjectName(_fromUtf8("createNewGroupParticipantBtn"))
        self.gridLayout_2.addWidget(self.createNewGroupParticipantBtn, 0, 2, 1, 1)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.gridLayout_2)
        self.teacherLabel = QtGui.QLabel(AddEntryDialog)
        self.teacherLabel.setObjectName(_fromUtf8("teacherLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.teacherLabel)
        self.teacherLineEdit = QtGui.QLineEdit(AddEntryDialog)
        self.teacherLineEdit.setEnabled(False)
        self.teacherLineEdit.setObjectName(_fromUtf8("teacherLineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.teacherLineEdit)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.chooseTeacherBtn = QtGui.QPushButton(AddEntryDialog)
        self.chooseTeacherBtn.setEnabled(True)
        self.chooseTeacherBtn.setObjectName(_fromUtf8("chooseTeacherBtn"))
        self.gridLayout_3.addWidget(self.chooseTeacherBtn, 0, 0, 1, 1)
        self.createNewTeacherBtn = QtGui.QPushButton(AddEntryDialog)
        self.createNewTeacherBtn.setObjectName(_fromUtf8("createNewTeacherBtn"))
        self.gridLayout_3.addWidget(self.createNewTeacherBtn, 0, 1, 1, 1)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.gridLayout_3)
        self.disciplineLabel = QtGui.QLabel(AddEntryDialog)
        self.disciplineLabel.setObjectName(_fromUtf8("disciplineLabel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.disciplineLabel)
        self.disciplineComboBox = QtGui.QComboBox(AddEntryDialog)
        self.disciplineComboBox.setObjectName(_fromUtf8("disciplineComboBox"))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.disciplineComboBox.addItem(_fromUtf8(""))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.disciplineComboBox)
        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 4)
        self.addPieceBtn = QtGui.QPushButton(AddEntryDialog)
        self.addPieceBtn.setObjectName(_fromUtf8("addPieceBtn"))
        self.gridLayout.addWidget(self.addPieceBtn, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(AddEntryDialog)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidgetPage1 = QtGui.QWidget()
        self.tabWidgetPage1.setObjectName(_fromUtf8("tabWidgetPage1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tabWidgetPage1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = PieceWidget(self.tabWidgetPage1)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout.addWidget(self.widget)
        self.tabWidget.addTab(self.tabWidgetPage1, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 4)

        self.retranslateUi(AddEntryDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AddEntryDialog)

    def retranslateUi(self, AddEntryDialog):
        AddEntryDialog.setWindowTitle(_translate("AddEntryDialog", "Add Entry", None))
        self.addEntryBtn.setText(_translate("AddEntryDialog", "A&dd Entry", None))
        self.cancelBtn.setText(_translate("AddEntryDialog", "&Cancel", None))
        self.participantLabel.setText(_translate("AddEntryDialog", "Participant", None))
        self.chooseParticipantBtn.setToolTip(_translate("AddEntryDialog", "TODO", None))
        self.chooseParticipantBtn.setText(_translate("AddEntryDialog", "Choose...", None))
        self.createNewSoloParticipantBtn.setText(_translate("AddEntryDialog", "Create New &Solo...", None))
        self.createNewGroupParticipantBtn.setText(_translate("AddEntryDialog", "Create New &Group...", None))
        self.teacherLabel.setText(_translate("AddEntryDialog", "Teacher", None))
        self.chooseTeacherBtn.setText(_translate("AddEntryDialog", "Choose...", None))
        self.createNewTeacherBtn.setText(_translate("AddEntryDialog", "Create New...", None))
        self.disciplineLabel.setText(_translate("AddEntryDialog", "Discipline", None))
        self.disciplineComboBox.setItemText(0, _translate("AddEntryDialog", "Dance", None))
        self.disciplineComboBox.setItemText(1, _translate("AddEntryDialog", "Piano", None))
        self.disciplineComboBox.setItemText(2, _translate("AddEntryDialog", "Choral", None))
        self.disciplineComboBox.setItemText(3, _translate("AddEntryDialog", "Vocal", None))
        self.disciplineComboBox.setItemText(4, _translate("AddEntryDialog", "Instrumental", None))
        self.disciplineComboBox.setItemText(5, _translate("AddEntryDialog", "Band", None))
        self.disciplineComboBox.setItemText(6, _translate("AddEntryDialog", "Speech", None))
        self.addPieceBtn.setText(_translate("AddEntryDialog", "Add &Piece", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("AddEntryDialog", "Piece 1", None))

from pieceWidget import PieceWidget
