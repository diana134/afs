# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseTeacherDialog.ui'
#
# Created: Sun Dec  7 17:46:58 2014
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

class Ui_ChooseTeacherDialog(object):
    def setupUi(self, ChooseTeacherDialog):
        ChooseTeacherDialog.setObjectName(_fromUtf8("ChooseTeacherDialog"))
        ChooseTeacherDialog.resize(875, 398)
        self.verticalLayout = QtGui.QVBoxLayout(ChooseTeacherDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEdit = QtGui.QLineEdit(ChooseTeacherDialog)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(ChooseTeacherDialog)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.teacherTableView = QtGui.QTableView(ChooseTeacherDialog)
        self.teacherTableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.teacherTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.teacherTableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.teacherTableView.setObjectName(_fromUtf8("teacherTableView"))
        self.verticalLayout.addWidget(self.teacherTableView)
        self.btnBox = QtGui.QDialogButtonBox(ChooseTeacherDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ChooseTeacherDialog)
        QtCore.QMetaObject.connectSlotsByName(ChooseTeacherDialog)

    def retranslateUi(self, ChooseTeacherDialog):
        ChooseTeacherDialog.setWindowTitle(_translate("ChooseTeacherDialog", "Dialog", None))
        self.pushButton.setText(_translate("ChooseTeacherDialog", "PushButton", None))

