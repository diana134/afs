# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created: Mon Jun 30 15:25:36 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1342, 755)
        MainWindow.setAnimated(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1341, 751))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 641))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.entries_listView = QtGui.QListView(self.verticalLayoutWidget)
        self.entries_listView.setObjectName(_fromUtf8("entries_listView"))
        self.verticalLayout_2.addWidget(self.entries_listView)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(280, 10, 1051, 701))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 511, 251))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtGui.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_5)
        self.lineEdit_6 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_6)
        self.lineEdit_7 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_7)
        self.lineEdit_8 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_8)
        self.dateEdit = QtGui.QDateEdit(self.formLayoutWidget)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.dateEdit)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayoutWidget_3 = QtGui.QWidget(self.groupBox_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 511, 321))
        self.formLayoutWidget_3.setObjectName(_fromUtf8("formLayoutWidget_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_17 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_17)
        self.comboBox = QtGui.QComboBox(self.formLayoutWidget_3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_18 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_17 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_17)
        self.label_19 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_18 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_18)
        self.label_23 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_23)
        self.lineEdit_19 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_19)
        self.label_20 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_20 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_20)
        self.label_22 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_22)
        self.lineEdit_22 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.lineEdit_22)
        self.label_24 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_24)
        self.lineEdit_23 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_23.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.lineEdit_23)
        self.label_25 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_24 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.formLayout_3.setWidget(10, QtGui.QFormLayout.FieldRole, self.lineEdit_24)
        self.label_26 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_25 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.formLayout_3.setWidget(11, QtGui.QFormLayout.FieldRole, self.lineEdit_25)
        self.label_27 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_16 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_16.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.formLayout_3.setWidget(9, QtGui.QFormLayout.FieldRole, self.lineEdit_16)
        self.label_21 = QtGui.QLabel(self.formLayoutWidget_3)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_21)
        self.lineEdit_21 = QtGui.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_21)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.gridLayoutWidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayoutWidget_2 = QtGui.QWidget(self.groupBox_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 501, 221))
        self.formLayoutWidget_2.setObjectName(_fromUtf8("formLayoutWidget_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_10 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_9 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_10 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_11 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.label_13 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_13)
        self.lineEdit_12 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit_12)
        self.label_14 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_13 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_13.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_13)
        self.label_15 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_14 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_14.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_14)
        self.label_16 = QtGui.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_16)
        self.lineEdit_15 = QtGui.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_15.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_15)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Arts Festival Scheduler", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Entries", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "name to search here", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Add Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Edit Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Participant Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Postal Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Home Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Cell Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Birth Date (yy/mm/dd)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Selection Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Discipline", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "Piano", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Vocal", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Speech", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Instrumental", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Dance", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "Choral", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "Band", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Class Number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Class Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Style/Instrument", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Composer/Arranger/Artist/Author", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("MainWindow", "Opus", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "Movement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Performance Time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("MainWindow", "No.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Participant Level/Grade", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Teacher Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Town", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Postal Code", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Daytime Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Evening Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Entries", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Schedule", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("MainWindow", "Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))

