# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addParticipantDialog.ui'
#
# Created: Wed Feb  3 20:48:26 2016
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

class Ui_AddParticipantDialog(object):
    def setupUi(self, AddParticipantDialog):
        AddParticipantDialog.setObjectName(_fromUtf8("AddParticipantDialog"))
        AddParticipantDialog.resize(1371, 429)
        self.gridLayout = QtGui.QGridLayout(AddParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox_2 = QtGui.QGroupBox(AddParticipantDialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupNameLabel = QtGui.QLabel(self.groupBox_2)
        self.groupNameLabel.setObjectName(_fromUtf8("groupNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.groupNameLabel)
        self.groupNameLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.groupNameLineEdit.setObjectName(_fromUtf8("groupNameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.groupNameLineEdit)
        self.groupSizeLabel = QtGui.QLabel(self.groupBox_2)
        self.groupSizeLabel.setObjectName(_fromUtf8("groupSizeLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.groupSizeLabel)
        self.numberParticipantsLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.numberParticipantsLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.numberParticipantsLineEdit.setObjectName(_fromUtf8("numberParticipantsLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.numberParticipantsLineEdit)
        self.averageAgeLabel = QtGui.QLabel(self.groupBox_2)
        self.averageAgeLabel.setObjectName(_fromUtf8("averageAgeLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.averageAgeLabel)
        self.averageAgeLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.averageAgeLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.averageAgeLineEdit.setObjectName(_fromUtf8("averageAgeLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.averageAgeLineEdit)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.calculateAverageAgeBtn = QtGui.QPushButton(self.groupBox_2)
        self.calculateAverageAgeBtn.setObjectName(_fromUtf8("calculateAverageAgeBtn"))
        self.horizontalLayout_3.addWidget(self.calculateAverageAgeBtn)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.timeConstraintsGroupBox = QtGui.QGroupBox(self.groupBox_2)
        self.timeConstraintsGroupBox.setFlat(False)
        self.timeConstraintsGroupBox.setCheckable(True)
        self.timeConstraintsGroupBox.setChecked(False)
        self.timeConstraintsGroupBox.setObjectName(_fromUtf8("timeConstraintsGroupBox"))
        self.formLayout_3 = QtGui.QFormLayout(self.timeConstraintsGroupBox)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.earliestPerformanceTimeLabel_2 = QtGui.QLabel(self.timeConstraintsGroupBox)
        self.earliestPerformanceTimeLabel_2.setObjectName(_fromUtf8("earliestPerformanceTimeLabel_2"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.earliestPerformanceTimeLabel_2)
        self.earliestPerformanceTimeTimeEdit = QtGui.QTimeEdit(self.timeConstraintsGroupBox)
        self.earliestPerformanceTimeTimeEdit.setTime(QtCore.QTime(9, 0, 0))
        self.earliestPerformanceTimeTimeEdit.setObjectName(_fromUtf8("earliestPerformanceTimeTimeEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.earliestPerformanceTimeTimeEdit)
        self.latestPerformanceTimeLabel_2 = QtGui.QLabel(self.timeConstraintsGroupBox)
        self.latestPerformanceTimeLabel_2.setObjectName(_fromUtf8("latestPerformanceTimeLabel_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.latestPerformanceTimeLabel_2)
        self.latestPerformanceTimeTimeEdit = QtGui.QTimeEdit(self.timeConstraintsGroupBox)
        self.latestPerformanceTimeTimeEdit.setTime(QtCore.QTime(15, 0, 0))
        self.latestPerformanceTimeTimeEdit.setObjectName(_fromUtf8("latestPerformanceTimeTimeEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.latestPerformanceTimeTimeEdit)
        self.formLayout.setWidget(5, QtGui.QFormLayout.SpanningRole, self.timeConstraintsGroupBox)
        self.participantsTextEdit = QtGui.QTextEdit(self.groupBox_2)
        self.participantsTextEdit.setObjectName(_fromUtf8("participantsTextEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.participantsTextEdit)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(AddParticipantDialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.firstNameLabel = QtGui.QLabel(self.groupBox)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtGui.QLineEdit(self.groupBox)
        self.firstNameLineEdit.setObjectName(_fromUtf8("firstNameLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtGui.QLabel(self.groupBox)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtGui.QLineEdit(self.groupBox)
        self.lastNameLineEdit.setObjectName(_fromUtf8("lastNameLineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.dateOfBirthLabel = QtGui.QLabel(self.groupBox)
        self.dateOfBirthLabel.setObjectName(_fromUtf8("dateOfBirthLabel"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.dateOfBirthDateEdit = QtGui.QDateEdit(self.groupBox)
        self.dateOfBirthDateEdit.setAutoFillBackground(False)
        self.dateOfBirthDateEdit.setDate(QtCore.QDate(1996, 1, 1))
        self.dateOfBirthDateEdit.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.dateOfBirthDateEdit.setCalendarPopup(True)
        self.dateOfBirthDateEdit.setObjectName(_fromUtf8("dateOfBirthDateEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.dateOfBirthDateEdit)
        self.ageLabel = QtGui.QLabel(self.groupBox)
        self.ageLabel.setObjectName(_fromUtf8("ageLabel"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.ageLabel)
        self.ageSpinBox = QtGui.QSpinBox(self.groupBox)
        self.ageSpinBox.setMinimum(8)
        self.ageSpinBox.setObjectName(_fromUtf8("ageSpinBox"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.ageSpinBox)
        self.parentLabel = QtGui.QLabel(self.groupBox)
        self.parentLabel.setObjectName(_fromUtf8("parentLabel"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.parentLabel)
        self.parentLineEdit = QtGui.QLineEdit(self.groupBox)
        self.parentLineEdit.setObjectName(_fromUtf8("parentLineEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.parentLineEdit)
        self.homePhoneLabel = QtGui.QLabel(self.groupBox)
        self.homePhoneLabel.setObjectName(_fromUtf8("homePhoneLabel"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.homePhoneLabel)
        self.homePhoneLineEdit = QtGui.QLineEdit(self.groupBox)
        self.homePhoneLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.homePhoneLineEdit.setObjectName(_fromUtf8("homePhoneLineEdit"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.homePhoneLineEdit)
        self.cellPhoneLabel = QtGui.QLabel(self.groupBox)
        self.cellPhoneLabel.setObjectName(_fromUtf8("cellPhoneLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.cellPhoneLabel)
        self.cellPhoneLineEdit = QtGui.QLineEdit(self.groupBox)
        self.cellPhoneLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cellPhoneLineEdit.setObjectName(_fromUtf8("cellPhoneLineEdit"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.cellPhoneLineEdit)
        self.emailLabel = QtGui.QLabel(self.groupBox)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(self.groupBox)
        self.emailLineEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.addressLabel = QtGui.QLabel(self.groupBox)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QLineEdit(self.groupBox)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtGui.QLabel(self.groupBox)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtGui.QLineEdit(self.groupBox)
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.formLayout_2.setWidget(9, QtGui.QFormLayout.FieldRole, self.cityLineEdit)
        self.postalCodeLabel = QtGui.QLabel(self.groupBox)
        self.postalCodeLabel.setObjectName(_fromUtf8("postalCodeLabel"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.LabelRole, self.postalCodeLabel)
        self.postalCodeLineEdit = QtGui.QLineEdit(self.groupBox)
        self.postalCodeLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.postalCodeLineEdit.setObjectName(_fromUtf8("postalCodeLineEdit"))
        self.formLayout_2.setWidget(10, QtGui.QFormLayout.FieldRole, self.postalCodeLineEdit)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(AddParticipantDialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.schoolAttendingLabel = QtGui.QLabel(self.groupBox_3)
        self.schoolAttendingLabel.setObjectName(_fromUtf8("schoolAttendingLabel"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.schoolAttendingLabel)
        self.schoolAttendingLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.schoolAttendingLineEdit.setObjectName(_fromUtf8("schoolAttendingLineEdit"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.schoolAttendingLineEdit)
        self.schoolGradeLabel = QtGui.QLabel(self.groupBox_3)
        self.schoolGradeLabel.setObjectName(_fromUtf8("schoolGradeLabel"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.schoolGradeLabel)
        self.schoolGradeLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.schoolGradeLineEdit.setObjectName(_fromUtf8("schoolGradeLineEdit"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.schoolGradeLineEdit)
        self.contactPersonLabel = QtGui.QLabel(self.groupBox_3)
        self.contactPersonLabel.setObjectName(_fromUtf8("contactPersonLabel"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.contactPersonLabel)
        self.contactPersonLineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.contactPersonLineEdit.setEnabled(False)
        self.contactPersonLineEdit.setObjectName(_fromUtf8("contactPersonLineEdit"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.contactPersonLineEdit)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.clearContactBtn = QtGui.QPushButton(self.groupBox_3)
        self.clearContactBtn.setObjectName(_fromUtf8("clearContactBtn"))
        self.horizontalLayout_10.addWidget(self.clearContactBtn)
        self.chooseContactBtn = QtGui.QPushButton(self.groupBox_3)
        self.chooseContactBtn.setObjectName(_fromUtf8("chooseContactBtn"))
        self.horizontalLayout_10.addWidget(self.chooseContactBtn)
        self.createContactBtn = QtGui.QPushButton(self.groupBox_3)
        self.createContactBtn.setObjectName(_fromUtf8("createContactBtn"))
        self.horizontalLayout_10.addWidget(self.createContactBtn)
        self.formLayout_5.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(167, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelBtn = QtGui.QPushButton(AddParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.horizontalLayout.addWidget(self.cancelBtn)
        self.addParticipantBtn = QtGui.QPushButton(AddParticipantDialog)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.horizontalLayout.addWidget(self.addParticipantBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 1, 1)

        self.retranslateUi(AddParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(AddParticipantDialog)
        AddParticipantDialog.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        AddParticipantDialog.setTabOrder(self.lastNameLineEdit, self.dateOfBirthDateEdit)
        AddParticipantDialog.setTabOrder(self.dateOfBirthDateEdit, self.ageSpinBox)
        AddParticipantDialog.setTabOrder(self.ageSpinBox, self.parentLineEdit)
        AddParticipantDialog.setTabOrder(self.parentLineEdit, self.homePhoneLineEdit)
        AddParticipantDialog.setTabOrder(self.homePhoneLineEdit, self.cellPhoneLineEdit)
        AddParticipantDialog.setTabOrder(self.cellPhoneLineEdit, self.emailLineEdit)
        AddParticipantDialog.setTabOrder(self.emailLineEdit, self.addressLineEdit)
        AddParticipantDialog.setTabOrder(self.addressLineEdit, self.cityLineEdit)
        AddParticipantDialog.setTabOrder(self.cityLineEdit, self.postalCodeLineEdit)
        AddParticipantDialog.setTabOrder(self.postalCodeLineEdit, self.schoolAttendingLineEdit)
        AddParticipantDialog.setTabOrder(self.schoolAttendingLineEdit, self.schoolGradeLineEdit)
        AddParticipantDialog.setTabOrder(self.schoolGradeLineEdit, self.clearContactBtn)
        AddParticipantDialog.setTabOrder(self.clearContactBtn, self.chooseContactBtn)
        AddParticipantDialog.setTabOrder(self.chooseContactBtn, self.createContactBtn)
        AddParticipantDialog.setTabOrder(self.createContactBtn, self.groupNameLineEdit)
        AddParticipantDialog.setTabOrder(self.groupNameLineEdit, self.numberParticipantsLineEdit)
        AddParticipantDialog.setTabOrder(self.numberParticipantsLineEdit, self.averageAgeLineEdit)
        AddParticipantDialog.setTabOrder(self.averageAgeLineEdit, self.calculateAverageAgeBtn)
        AddParticipantDialog.setTabOrder(self.calculateAverageAgeBtn, self.timeConstraintsGroupBox)
        AddParticipantDialog.setTabOrder(self.timeConstraintsGroupBox, self.earliestPerformanceTimeTimeEdit)
        AddParticipantDialog.setTabOrder(self.earliestPerformanceTimeTimeEdit, self.latestPerformanceTimeTimeEdit)
        AddParticipantDialog.setTabOrder(self.latestPerformanceTimeTimeEdit, self.participantsTextEdit)
        AddParticipantDialog.setTabOrder(self.participantsTextEdit, self.addParticipantBtn)
        AddParticipantDialog.setTabOrder(self.addParticipantBtn, self.cancelBtn)
        AddParticipantDialog.setTabOrder(self.cancelBtn, self.contactPersonLineEdit)

    def retranslateUi(self, AddParticipantDialog):
        AddParticipantDialog.setWindowTitle(_translate("AddParticipantDialog", "Dialog", None))
        self.groupBox_2.setTitle(_translate("AddParticipantDialog", "Group/Duo/Trio/Etc.", None))
        self.groupNameLabel.setText(_translate("AddParticipantDialog", "Group Name", None))
        self.groupSizeLabel.setText(_translate("AddParticipantDialog", "Number of Participants", None))
        self.averageAgeLabel.setText(_translate("AddParticipantDialog", "Average Age", None))
        self.calculateAverageAgeBtn.setText(_translate("AddParticipantDialog", "Calculate Average Age", None))
        self.timeConstraintsGroupBox.setTitle(_translate("AddParticipantDialog", "Time Constraints", None))
        self.earliestPerformanceTimeLabel_2.setText(_translate("AddParticipantDialog", "Earliest Performance Time", None))
        self.latestPerformanceTimeLabel_2.setText(_translate("AddParticipantDialog", "Latest Performance Time", None))
        self.label.setText(_translate("AddParticipantDialog", "Participant Names", None))
        self.groupBox.setTitle(_translate("AddParticipantDialog", "Solo", None))
        self.firstNameLabel.setText(_translate("AddParticipantDialog", "First Name", None))
        self.lastNameLabel.setText(_translate("AddParticipantDialog", "Last Name", None))
        self.dateOfBirthLabel.setText(_translate("AddParticipantDialog", "Date of Birth", None))
        self.dateOfBirthDateEdit.setDisplayFormat(_translate("AddParticipantDialog", "d-M-yyyy", None))
        self.ageLabel.setText(_translate("AddParticipantDialog", "Age as of Jan. 1 ", None))
        self.parentLabel.setText(_translate("AddParticipantDialog", "Parent", None))
        self.homePhoneLabel.setText(_translate("AddParticipantDialog", "Home Phone", None))
        self.cellPhoneLabel.setText(_translate("AddParticipantDialog", "Cell Phone", None))
        self.emailLabel.setText(_translate("AddParticipantDialog", "Email", None))
        self.addressLabel.setText(_translate("AddParticipantDialog", "Address", None))
        self.cityLabel.setText(_translate("AddParticipantDialog", "City", None))
        self.postalCodeLabel.setText(_translate("AddParticipantDialog", "Postal Code", None))
        self.groupBox_3.setTitle(_translate("AddParticipantDialog", "Both", None))
        self.schoolAttendingLabel.setText(_translate("AddParticipantDialog", "School Currently Attending", None))
        self.schoolGradeLabel.setText(_translate("AddParticipantDialog", "School Grade", None))
        self.contactPersonLabel.setText(_translate("AddParticipantDialog", "Teacher", None))
        self.clearContactBtn.setText(_translate("AddParticipantDialog", "Clear", None))
        self.chooseContactBtn.setText(_translate("AddParticipantDialog", "Choose...", None))
        self.createContactBtn.setText(_translate("AddParticipantDialog", "Create New...", None))
        self.cancelBtn.setText(_translate("AddParticipantDialog", "&Cancel", None))
        self.addParticipantBtn.setText(_translate("AddParticipantDialog", "A&dd Participant", None))

