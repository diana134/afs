# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_scheduleDialog.ui'
#
# Created: Sun Oct 19 15:06:11 2014
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

class Ui_ScheduleDialog(object):
    def setupUi(self, ScheduleDialog):
        ScheduleDialog.setObjectName(_fromUtf8("ScheduleDialog"))
        ScheduleDialog.resize(833, 423)
        self.verticalLayout_3 = QtGui.QVBoxLayout(ScheduleDialog)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(ScheduleDialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.scheduleTableWidget = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.scheduleTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.scheduleTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.scheduleTableWidget.setObjectName(_fromUtf8("scheduleTableWidget"))
        self.scheduleTableWidget.setColumnCount(0)
        self.scheduleTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.scheduleTableWidget)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.scheduleLeftBtn = QtGui.QToolButton(self.verticalLayoutWidget)
        self.scheduleLeftBtn.setArrowType(QtCore.Qt.LeftArrow)
        self.scheduleLeftBtn.setObjectName(_fromUtf8("scheduleLeftBtn"))
        self.gridLayout_2.addWidget(self.scheduleLeftBtn, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.scheduleUpBtn = QtGui.QToolButton(self.verticalLayoutWidget)
        self.scheduleUpBtn.setArrowType(QtCore.Qt.UpArrow)
        self.scheduleUpBtn.setObjectName(_fromUtf8("scheduleUpBtn"))
        self.gridLayout_2.addWidget(self.scheduleUpBtn, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 4, 1, 1)
        self.scheduleDownBtn = QtGui.QToolButton(self.verticalLayoutWidget)
        self.scheduleDownBtn.setArrowType(QtCore.Qt.DownArrow)
        self.scheduleDownBtn.setObjectName(_fromUtf8("scheduleDownBtn"))
        self.gridLayout_2.addWidget(self.scheduleDownBtn, 2, 2, 1, 1)
        self.scheduleRightBtn = QtGui.QToolButton(self.verticalLayoutWidget)
        self.scheduleRightBtn.setArrowType(QtCore.Qt.RightArrow)
        self.scheduleRightBtn.setObjectName(_fromUtf8("scheduleRightBtn"))
        self.gridLayout_2.addWidget(self.scheduleRightBtn, 1, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.entriesTableWidget = QtGui.QTableWidget(self.verticalLayoutWidget_2)
        self.entriesTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.entriesTableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.entriesTableWidget.setObjectName(_fromUtf8("entriesTableWidget"))
        self.entriesTableWidget.setColumnCount(0)
        self.entriesTableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.entriesTableWidget)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 6, 1, 1)
        self.entriesUpBtn = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.entriesUpBtn.setArrowType(QtCore.Qt.UpArrow)
        self.entriesUpBtn.setObjectName(_fromUtf8("entriesUpBtn"))
        self.gridLayout.addWidget(self.entriesUpBtn, 1, 5, 1, 1)
        self.entriesDownBtn = QtGui.QToolButton(self.verticalLayoutWidget_2)
        self.entriesDownBtn.setArrowType(QtCore.Qt.DownArrow)
        self.entriesDownBtn.setObjectName(_fromUtf8("entriesDownBtn"))
        self.gridLayout.addWidget(self.entriesDownBtn, 2, 5, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.splitter)
        self.buttonBox = QtGui.QDialogButtonBox(ScheduleDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(ScheduleDialog)
        QtCore.QMetaObject.connectSlotsByName(ScheduleDialog)

    def retranslateUi(self, ScheduleDialog):
        ScheduleDialog.setWindowTitle(_translate("ScheduleDialog", "Form", None))
        self.label.setText(_translate("ScheduleDialog", "Schedule", None))
        self.scheduleLeftBtn.setText(_translate("ScheduleDialog", "...", None))
        self.scheduleUpBtn.setText(_translate("ScheduleDialog", "...", None))
        self.scheduleDownBtn.setText(_translate("ScheduleDialog", "...", None))
        self.scheduleRightBtn.setText(_translate("ScheduleDialog", "...", None))
        self.label_2.setText(_translate("ScheduleDialog", "Entries", None))
        self.entriesUpBtn.setText(_translate("ScheduleDialog", "...", None))
        self.entriesDownBtn.setText(_translate("ScheduleDialog", "...", None))

