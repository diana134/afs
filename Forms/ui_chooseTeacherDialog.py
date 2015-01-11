# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_chooseTeacherDialog.ui'
#
# Created: Sun Jan 11 13:48:45 2015
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
        ChooseTeacherDialog.resize(875, 397)
        self.verticalLayout = QtGui.QVBoxLayout(ChooseTeacherDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.teacherTableView = QtGui.QTableView(ChooseTeacherDialog)
        self.teacherTableView.setObjectName(_fromUtf8("teacherTableView"))
        self.verticalLayout.addWidget(self.teacherTableView)
        self.btnBox = QtGui.QDialogButtonBox(ChooseTeacherDialog)
        self.btnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnBox.setObjectName(_fromUtf8("btnBox"))
        self.verticalLayout.addWidget(self.btnBox)

        self.retranslateUi(ChooseTeacherDialog)
        QtCore.QMetaObject.connectSlotsByName(ChooseTeacherDialog)

    def retranslateUi(self, ChooseTeacherDialog):
        ChooseTeacherDialog.setWindowTitle(_translate("ChooseTeacherDialog", "Choose Teacher/Contact", None))

