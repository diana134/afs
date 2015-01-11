# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_participantWidget.ui'
#
# Created: Sat Jan 10 23:01:34 2015
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

class Ui_ParticipantWidget(object):
    def setupUi(self, ParticipantWidget):
        ParticipantWidget.setObjectName(_fromUtf8("ParticipantWidget"))
        ParticipantWidget.resize(403, 77)
        self.verticalLayout = QtGui.QVBoxLayout(ParticipantWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.participantLineEdit = QtGui.QLineEdit(ParticipantWidget)
        self.participantLineEdit.setEnabled(False)
        self.participantLineEdit.setObjectName(_fromUtf8("participantLineEdit"))
        self.verticalLayout.addWidget(self.participantLineEdit)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.chooseParticipantBtn = QtGui.QPushButton(ParticipantWidget)
        self.chooseParticipantBtn.setObjectName(_fromUtf8("chooseParticipantBtn"))
        self.horizontalLayout_8.addWidget(self.chooseParticipantBtn)
        self.createNewParticipantBtn = QtGui.QPushButton(ParticipantWidget)
        self.createNewParticipantBtn.setObjectName(_fromUtf8("createNewParticipantBtn"))
        self.horizontalLayout_8.addWidget(self.createNewParticipantBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.retranslateUi(ParticipantWidget)
        QtCore.QMetaObject.connectSlotsByName(ParticipantWidget)

    def retranslateUi(self, ParticipantWidget):
        ParticipantWidget.setWindowTitle(_translate("ParticipantWidget", "Form", None))
        self.chooseParticipantBtn.setText(_translate("ParticipantWidget", "Choose...", None))
        self.createNewParticipantBtn.setText(_translate("ParticipantWidget", "Create New...", None))

