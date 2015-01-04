# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pieceWidget.ui'
#
# Created: Sat Jan  3 16:06:37 2015
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

class Ui_PieceWidget(object):
    def setupUi(self, PieceWidget):
        PieceWidget.setObjectName(_fromUtf8("PieceWidget"))
        PieceWidget.resize(404, 167)
        self.formLayout = QtGui.QFormLayout(PieceWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.titleLabel = QtGui.QLabel(PieceWidget)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtGui.QLineEdit(PieceWidget)
        self.titleLineEdit.setObjectName(_fromUtf8("titleLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.titleLineEdit)
        self.composerLabel = QtGui.QLabel(PieceWidget)
        self.composerLabel.setObjectName(_fromUtf8("composerLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.composerLabel)
        self.composerLineEdit = QtGui.QLineEdit(PieceWidget)
        self.composerLineEdit.setObjectName(_fromUtf8("composerLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.composerLineEdit)
        self.opusLabel = QtGui.QLabel(PieceWidget)
        self.opusLabel.setObjectName(_fromUtf8("opusLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.opusLabel)
        self.opusNoLineEdit = QtGui.QLineEdit(PieceWidget)
        self.opusNoLineEdit.setObjectName(_fromUtf8("opusNoLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.opusNoLineEdit)
        self.movementLabel = QtGui.QLabel(PieceWidget)
        self.movementLabel.setObjectName(_fromUtf8("movementLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.movementLabel)
        self.movementLineEdit = QtGui.QLineEdit(PieceWidget)
        self.movementLineEdit.setObjectName(_fromUtf8("movementLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.movementLineEdit)
        self.performanceTimeLabel = QtGui.QLabel(PieceWidget)
        self.performanceTimeLabel.setObjectName(_fromUtf8("performanceTimeLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.performanceTimeLabel)
        self.performanceTimeEdit = QtGui.QTimeEdit(PieceWidget)
        self.performanceTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(1, 59, 59)))
        self.performanceTimeEdit.setObjectName(_fromUtf8("performanceTimeEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.performanceTimeEdit)

        self.retranslateUi(PieceWidget)
        QtCore.QMetaObject.connectSlotsByName(PieceWidget)

    def retranslateUi(self, PieceWidget):
        PieceWidget.setWindowTitle(_translate("PieceWidget", "Form", None))
        self.titleLabel.setText(_translate("PieceWidget", "Title", None))
        self.composerLabel.setText(_translate("PieceWidget", "Composer/Arranger", None))
        self.opusLabel.setText(_translate("PieceWidget", "Opus No.", None))
        self.movementLabel.setText(_translate("PieceWidget", "Movement", None))
        self.performanceTimeLabel.setText(_translate("PieceWidget", "Performance Time (mm:ss)", None))
        self.performanceTimeEdit.setDisplayFormat(_translate("PieceWidget", "mm:ss", None))

