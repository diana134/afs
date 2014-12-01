# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pieceWidget.ui'
#
# Created: Sun Nov 30 22:09:34 2014
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
        PieceWidget.resize(404, 291)
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
        self.arrangerLabel = QtGui.QLabel(PieceWidget)
        self.arrangerLabel.setObjectName(_fromUtf8("arrangerLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.arrangerLabel)
        self.arrangerLineEdit = QtGui.QLineEdit(PieceWidget)
        self.arrangerLineEdit.setObjectName(_fromUtf8("arrangerLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.arrangerLineEdit)
        self.artistLabel = QtGui.QLabel(PieceWidget)
        self.artistLabel.setObjectName(_fromUtf8("artistLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.artistLabel)
        self.artistLineEdit = QtGui.QLineEdit(PieceWidget)
        self.artistLineEdit.setObjectName(_fromUtf8("artistLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.artistLineEdit)
        self.authorLabel = QtGui.QLabel(PieceWidget)
        self.authorLabel.setObjectName(_fromUtf8("authorLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtGui.QLineEdit(PieceWidget)
        self.authorLineEdit.setObjectName(_fromUtf8("authorLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.authorLineEdit)
        self.opusLabel = QtGui.QLabel(PieceWidget)
        self.opusLabel.setObjectName(_fromUtf8("opusLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.opusLabel)
        self.opusLineEdit = QtGui.QLineEdit(PieceWidget)
        self.opusLineEdit.setObjectName(_fromUtf8("opusLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.opusLineEdit)
        self.noLabel = QtGui.QLabel(PieceWidget)
        self.noLabel.setObjectName(_fromUtf8("noLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.noLabel)
        self.noLineEdit = QtGui.QLineEdit(PieceWidget)
        self.noLineEdit.setObjectName(_fromUtf8("noLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.noLineEdit)
        self.movementLabel = QtGui.QLabel(PieceWidget)
        self.movementLabel.setObjectName(_fromUtf8("movementLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.movementLabel)
        self.movementLineEdit = QtGui.QLineEdit(PieceWidget)
        self.movementLineEdit.setObjectName(_fromUtf8("movementLineEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.movementLineEdit)
        self.performanceTimeLabel = QtGui.QLabel(PieceWidget)
        self.performanceTimeLabel.setObjectName(_fromUtf8("performanceTimeLabel"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.performanceTimeLabel)
        self.performanceTimeEdit = QtGui.QTimeEdit(PieceWidget)
        self.performanceTimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(1, 59, 59)))
        self.performanceTimeEdit.setObjectName(_fromUtf8("performanceTimeEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.performanceTimeEdit)

        self.retranslateUi(PieceWidget)
        QtCore.QMetaObject.connectSlotsByName(PieceWidget)

    def retranslateUi(self, PieceWidget):
        PieceWidget.setWindowTitle(_translate("PieceWidget", "Form", None))
        self.titleLabel.setText(_translate("PieceWidget", "Title", None))
        self.composerLabel.setText(_translate("PieceWidget", "Composer", None))
        self.arrangerLabel.setText(_translate("PieceWidget", "Arranger", None))
        self.artistLabel.setText(_translate("PieceWidget", "Artist", None))
        self.authorLabel.setText(_translate("PieceWidget", "Author", None))
        self.opusLabel.setText(_translate("PieceWidget", "Opus", None))
        self.noLabel.setText(_translate("PieceWidget", "No.", None))
        self.movementLabel.setText(_translate("PieceWidget", "Movement", None))
        self.performanceTimeLabel.setText(_translate("PieceWidget", "Performance Time (mm:ss)", None))
        self.performanceTimeEdit.setDisplayFormat(_translate("PieceWidget", "mm:ss", None))

