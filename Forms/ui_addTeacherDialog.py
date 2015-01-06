# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addTeacherDialog.ui'
#
# Created: Mon Jan  5 21:47:20 2015
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

class Ui_AddTeacherDialog(object):
    def setupUi(self, AddTeacherDialog):
        AddTeacherDialog.setObjectName(_fromUtf8("AddTeacherDialog"))
        AddTeacherDialog.resize(400, 295)
        self.gridLayout = QtGui.QGridLayout(AddTeacherDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelBtn = QtGui.QPushButton(AddTeacherDialog)
        self.cancelBtn.setAutoDefault(False)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 2, 1, 1, 1)
        self.addTeacherBtn = QtGui.QPushButton(AddTeacherDialog)
        self.addTeacherBtn.setAutoDefault(False)
        self.addTeacherBtn.setDefault(True)
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
        AddTeacherDialog.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        AddTeacherDialog.setTabOrder(self.lastNameLineEdit, self.addressLineEdit)
        AddTeacherDialog.setTabOrder(self.addressLineEdit, self.cityLineEdit)
        AddTeacherDialog.setTabOrder(self.cityLineEdit, self.postalCodeLineEdit)
        AddTeacherDialog.setTabOrder(self.postalCodeLineEdit, self.daytimePhoneLineEdit)
        AddTeacherDialog.setTabOrder(self.daytimePhoneLineEdit, self.eveningPhoneLineEdit)
        AddTeacherDialog.setTabOrder(self.eveningPhoneLineEdit, self.emailLineEdit)
        AddTeacherDialog.setTabOrder(self.emailLineEdit, self.addTeacherBtn)
        AddTeacherDialog.setTabOrder(self.addTeacherBtn, self.cancelBtn)

    def retranslateUi(self, AddTeacherDialog):
        AddTeacherDialog.setWindowTitle(_translate("AddTeacherDialog", "Add Teacher", None))
        self.cancelBtn.setText(_translate("AddTeacherDialog", "&Cancel", None))
        self.addTeacherBtn.setText(_translate("AddTeacherDialog", "A&dd Teacher", None))
        self.firstNameLabel.setText(_translate("AddTeacherDialog", "First Name", None))
        self.lastNameLabel.setText(_translate("AddTeacherDialog", "Last Name", None))
        self.addressLabel.setText(_translate("AddTeacherDialog", "Address", None))
        self.cityLabel.setText(_translate("AddTeacherDialog", "City", None))
        self.postalCodeLabel.setText(_translate("AddTeacherDialog", "Postal Code", None))
        self.daytimePhoneLabel.setText(_translate("AddTeacherDialog", "Daytime Phone", None))
        self.eveningPhoneLabel.setText(_translate("AddTeacherDialog", "Evening Phone", None))
        self.emailLabel.setText(_translate("AddTeacherDialog", "Email", None))

