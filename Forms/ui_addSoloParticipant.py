# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addSoloParticipant.ui'
#
# Created: Mon Aug 11 16:20:21 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_addSoloParticipantDialog(object):
    def setupUi(self, addSoloParticipantDialog):
        addSoloParticipantDialog.setObjectName(_fromUtf8("addSoloParticipantDialog"))
        addSoloParticipantDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        addSoloParticipantDialog.resize(400, 332)
        self.gridLayout = QtGui.QGridLayout(addSoloParticipantDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.addParticipantBtn = QtGui.QPushButton(addSoloParticipantDialog)
        self.addParticipantBtn.setObjectName(_fromUtf8("addParticipantBtn"))
        self.gridLayout.addWidget(self.addParticipantBtn, 2, 1, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.firstNameLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.firstNameLineEdit.setObjectName(_fromUtf8("firstNameLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.lastNameLineEdit.setObjectName(_fromUtf8("lastNameLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.addressLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cityLineEdit)
        self.postalCodeLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.postalCodeLabel.setObjectName(_fromUtf8("postalCodeLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.postalCodeLabel)
        self.postalCodeLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.postalCodeLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.postalCodeLineEdit.setObjectName(_fromUtf8("postalCodeLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.postalCodeLineEdit)
        self.homePhoneLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.homePhoneLabel.setObjectName(_fromUtf8("homePhoneLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.homePhoneLabel)
        self.homePhoneLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.homePhoneLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.homePhoneLineEdit.setObjectName(_fromUtf8("homePhoneLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.homePhoneLineEdit)
        self.cellPhoneLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.cellPhoneLabel.setObjectName(_fromUtf8("cellPhoneLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.cellPhoneLabel)
        self.cellPhoneLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.cellPhoneLineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.cellPhoneLineEdit.setObjectName(_fromUtf8("cellPhoneLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.cellPhoneLineEdit)
        self.emailLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(addSoloParticipantDialog)
        self.emailLineEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.dateOfBirthLabel = QtGui.QLabel(addSoloParticipantDialog)
        self.dateOfBirthLabel.setObjectName(_fromUtf8("dateOfBirthLabel"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.dateOfBirthLabel)
        self.dateOfBirthDateEdit = QtGui.QDateEdit(addSoloParticipantDialog)
        self.dateOfBirthDateEdit.setAutoFillBackground(False)
        self.dateOfBirthDateEdit.setDate(QtCore.QDate(1900, 1, 1))
        self.dateOfBirthDateEdit.setMinimumDate(QtCore.QDate(1900, 1, 1))
        self.dateOfBirthDateEdit.setObjectName(_fromUtf8("dateOfBirthDateEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.dateOfBirthDateEdit)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)
        self.cancelBtn = QtGui.QPushButton(addSoloParticipantDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 2, 0, 1, 1)

        self.retranslateUi(addSoloParticipantDialog)
        QtCore.QMetaObject.connectSlotsByName(addSoloParticipantDialog)

    def retranslateUi(self, addSoloParticipantDialog):
        addSoloParticipantDialog.setWindowTitle(QtGui.QApplication.translate("addSoloParticipantDialog", "Add Solo Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.addParticipantBtn.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Add &Participant", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.addressLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.cityLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.postalCodeLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Postal Code", None, QtGui.QApplication.UnicodeUTF8))
        self.homePhoneLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Home Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.cellPhoneLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Cell Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.dateOfBirthLabel.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "Date of Birth", None, QtGui.QApplication.UnicodeUTF8))
        self.dateOfBirthDateEdit.setDisplayFormat(QtGui.QApplication.translate("addSoloParticipantDialog", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("addSoloParticipantDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

