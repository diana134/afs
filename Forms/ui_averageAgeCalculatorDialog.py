# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_averageAgeCalculatorDialog.ui'
#
# Created: Sat Jan 30 00:54:51 2016
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

class Ui_AverageAgeCalculatorDialog(object):
    def setupUi(self, AverageAgeCalculatorDialog):
        AverageAgeCalculatorDialog.setObjectName(_fromUtf8("AverageAgeCalculatorDialog"))
        AverageAgeCalculatorDialog.resize(224, 322)
        self.verticalLayout = QtGui.QVBoxLayout(AverageAgeCalculatorDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(AverageAgeCalculatorDialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.birthdateDateEdit = QtGui.QDateEdit(AverageAgeCalculatorDialog)
        self.birthdateDateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.birthdateDateEdit.setCalendarPopup(True)
        self.birthdateDateEdit.setObjectName(_fromUtf8("birthdateDateEdit"))
        self.horizontalLayout_4.addWidget(self.birthdateDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addBirthdateBtn = QtGui.QPushButton(AverageAgeCalculatorDialog)
        self.addBirthdateBtn.setObjectName(_fromUtf8("addBirthdateBtn"))
        self.horizontalLayout.addWidget(self.addBirthdateBtn)
        self.deleteBirthdateBtn = QtGui.QPushButton(AverageAgeCalculatorDialog)
        self.deleteBirthdateBtn.setObjectName(_fromUtf8("deleteBirthdateBtn"))
        self.horizontalLayout.addWidget(self.deleteBirthdateBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.birthdateListWidget = QtGui.QListWidget(AverageAgeCalculatorDialog)
        self.birthdateListWidget.setObjectName(_fromUtf8("birthdateListWidget"))
        self.verticalLayout.addWidget(self.birthdateListWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(AverageAgeCalculatorDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.asOfDateEdit = QtGui.QDateEdit(AverageAgeCalculatorDialog)
        self.asOfDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 1, 1), QtCore.QTime(0, 0, 0)))
        self.asOfDateEdit.setDate(QtCore.QDate(2016, 1, 1))
        self.asOfDateEdit.setCalendarPopup(True)
        self.asOfDateEdit.setObjectName(_fromUtf8("asOfDateEdit"))
        self.horizontalLayout_3.addWidget(self.asOfDateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(AverageAgeCalculatorDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.averageAgeLineEdit = QtGui.QLineEdit(AverageAgeCalculatorDialog)
        self.averageAgeLineEdit.setEnabled(False)
        self.averageAgeLineEdit.setObjectName(_fromUtf8("averageAgeLineEdit"))
        self.horizontalLayout_2.addWidget(self.averageAgeLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnBox = QtGui.QDialogButtonBox(AverageAgeCalculatorDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(AverageAgeCalculatorDialog)
        QtCore.QMetaObject.connectSlotsByName(AverageAgeCalculatorDialog)

    def retranslateUi(self, AverageAgeCalculatorDialog):
        AverageAgeCalculatorDialog.setWindowTitle(_translate("AverageAgeCalculatorDialog", "Average Age Calculator", None))
        self.label_2.setText(_translate("AverageAgeCalculatorDialog", "Birthdate", None))
        self.addBirthdateBtn.setText(_translate("AverageAgeCalculatorDialog", "&Add Birthdate", None))
        self.deleteBirthdateBtn.setText(_translate("AverageAgeCalculatorDialog", "&Delete Birthdate", None))
        self.label_3.setText(_translate("AverageAgeCalculatorDialog", "As of:", None))
        self.asOfDateEdit.setDisplayFormat(_translate("AverageAgeCalculatorDialog", "d/M/yy", None))
        self.label.setText(_translate("AverageAgeCalculatorDialog", "Average Age:", None))

