# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addTeacherDialog.ui'
#
# Created: Mon Aug 18 17:05:49 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddTeacherDialog(object):
    def setupUi(self, AddTeacherDialog):
        AddTeacherDialog.setObjectName(_fromUtf8("AddTeacherDialog"))
        AddTeacherDialog.resize(400, 295)
        self.gridLayout = QtGui.QGridLayout(AddTeacherDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelBtn = QtGui.QPushButton(AddTeacherDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 2, 1, 1, 1)
        self.addTeacherBtn = QtGui.QPushButton(AddTeacherDialog)
        self.addTeacherBtn.setObjectName(_fromUtf8("addTeacherBtn"))
        self.gridLayout.addWidget(self.addTeacherBtn, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.firstNameLabel = QtGui.QLabel(AddTeacherDialog)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.firstNameLineEdit.setObjectName(_fromUtf8("firstNameLineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtGui.QLabel(AddTeacherDialog)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.lastNameLineEdit.setObjectName(_fromUtf8("lastNameLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.addressLabel = QtGui.QLabel(AddTeacherDialog)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtGui.QLabel(AddTeacherDialog)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.cityLineEdit)
        self.postalCodeLabel = QtGui.QLabel(AddTeacherDialog)
        self.postalCodeLabel.setObjectName(_fromUtf8("postalCodeLabel"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.postalCodeLabel)
        self.postalCodeLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.postalCodeLineEdit.setObjectName(_fromUtf8("postalCodeLineEdit"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.postalCodeLineEdit)
        self.daytimePhoneLabel = QtGui.QLabel(AddTeacherDialog)
        self.daytimePhoneLabel.setObjectName(_fromUtf8("daytimePhoneLabel"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.daytimePhoneLabel)
        self.daytimePhoneLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.daytimePhoneLineEdit.setObjectName(_fromUtf8("daytimePhoneLineEdit"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.daytimePhoneLineEdit)
        self.eveningPhoneLabel = QtGui.QLabel(AddTeacherDialog)
        self.eveningPhoneLabel.setObjectName(_fromUtf8("eveningPhoneLabel"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.eveningPhoneLabel)
        self.eveningPhoneLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.eveningPhoneLineEdit.setObjectName(_fromUtf8("eveningPhoneLineEdit"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.eveningPhoneLineEdit)
        self.emailLabel = QtGui.QLabel(AddTeacherDialog)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(AddTeacherDialog)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 3)

        self.retranslateUi(AddTeacherDialog)
        QtCore.QMetaObject.connectSlotsByName(AddTeacherDialog)

    def retranslateUi(self, AddTeacherDialog):
        AddTeacherDialog.setWindowTitle(QtGui.QApplication.translate("AddTeacherDialog", "Add Teacher", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("AddTeacherDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.addTeacherBtn.setText(QtGui.QApplication.translate("AddTeacherDialog", "A&dd Teacher", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.addressLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.cityLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.postalCodeLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Postal Code", None, QtGui.QApplication.UnicodeUTF8))
        self.daytimePhoneLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Daytime Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.eveningPhoneLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Evening Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("AddTeacherDialog", "Email", None, QtGui.QApplication.UnicodeUTF8))

