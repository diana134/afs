# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_addTeacherDialog.ui'
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

class Ui_addTeacherDialog(object):
    def setupUi(self, addTeacherDialog):
        addTeacherDialog.setObjectName(_fromUtf8("addTeacherDialog"))
        addTeacherDialog.resize(400, 295)
        self.gridLayout = QtGui.QGridLayout(addTeacherDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelBtn = QtGui.QPushButton(addTeacherDialog)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gridLayout.addWidget(self.cancelBtn, 2, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(addTeacherDialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.firstNameLabel = QtGui.QLabel(addTeacherDialog)
        self.firstNameLabel.setObjectName(_fromUtf8("firstNameLabel"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.firstNameLabel)
        self.firstNameLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.firstNameLineEdit.setObjectName(_fromUtf8("firstNameLineEdit"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.firstNameLineEdit)
        self.lastNameLabel = QtGui.QLabel(addTeacherDialog)
        self.lastNameLabel.setObjectName(_fromUtf8("lastNameLabel"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.lastNameLabel)
        self.lastNameLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.lastNameLineEdit.setObjectName(_fromUtf8("lastNameLineEdit"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lastNameLineEdit)
        self.addressLabel = QtGui.QLabel(addTeacherDialog)
        self.addressLabel.setObjectName(_fromUtf8("addressLabel"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.addressLineEdit.setObjectName(_fromUtf8("addressLineEdit"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.addressLineEdit)
        self.cityLabel = QtGui.QLabel(addTeacherDialog)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.cityLabel)
        self.cityLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.cityLineEdit.setObjectName(_fromUtf8("cityLineEdit"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.cityLineEdit)
        self.postalCodeLabel = QtGui.QLabel(addTeacherDialog)
        self.postalCodeLabel.setObjectName(_fromUtf8("postalCodeLabel"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.postalCodeLabel)
        self.postalCodeLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.postalCodeLineEdit.setObjectName(_fromUtf8("postalCodeLineEdit"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.postalCodeLineEdit)
        self.daytimePhoneLabel = QtGui.QLabel(addTeacherDialog)
        self.daytimePhoneLabel.setObjectName(_fromUtf8("daytimePhoneLabel"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.daytimePhoneLabel)
        self.daytimePhoneLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.daytimePhoneLineEdit.setObjectName(_fromUtf8("daytimePhoneLineEdit"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.daytimePhoneLineEdit)
        self.eveningPhoneLabel = QtGui.QLabel(addTeacherDialog)
        self.eveningPhoneLabel.setObjectName(_fromUtf8("eveningPhoneLabel"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.LabelRole, self.eveningPhoneLabel)
        self.eveningPhoneLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.eveningPhoneLineEdit.setObjectName(_fromUtf8("eveningPhoneLineEdit"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.eveningPhoneLineEdit)
        self.emailLabel = QtGui.QLabel(addTeacherDialog)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.emailLabel)
        self.emailLineEdit = QtGui.QLineEdit(addTeacherDialog)
        self.emailLineEdit.setObjectName(_fromUtf8("emailLineEdit"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.emailLineEdit)
        self.gridLayout.addLayout(self.formLayout_3, 1, 0, 1, 3)

        self.retranslateUi(addTeacherDialog)
        QtCore.QMetaObject.connectSlotsByName(addTeacherDialog)

    def retranslateUi(self, addTeacherDialog):
        addTeacherDialog.setWindowTitle(QtGui.QApplication.translate("addTeacherDialog", "Add Teacher", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelBtn.setText(QtGui.QApplication.translate("addTeacherDialog", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("addTeacherDialog", "A&dd Teacher", None, QtGui.QApplication.UnicodeUTF8))
        self.firstNameLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lastNameLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.addressLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.cityLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "City", None, QtGui.QApplication.UnicodeUTF8))
        self.postalCodeLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Postal Code", None, QtGui.QApplication.UnicodeUTF8))
        self.daytimePhoneLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Daytime Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.eveningPhoneLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Evening Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.emailLabel.setText(QtGui.QApplication.translate("addTeacherDialog", "Email", None, QtGui.QApplication.UnicodeUTF8))

