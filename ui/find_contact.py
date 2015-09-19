# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/find_contact.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(584, 359)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.esci = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.esci.setIcon(icon1)
        self.esci.setObjectName(_fromUtf8("esci"))
        self.gridLayout.addWidget(self.esci, 4, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tableView = QtGui.QTableView(self.groupBox)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 5)
        spacerItem = QtGui.QSpacerItem(184, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.find = QtGui.QPushButton(Dialog)
        self.find.setIcon(icon)
        self.find.setObjectName(_fromUtf8("find"))
        self.gridLayout.addWidget(self.find, 4, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.cerca_txt = QtGui.QLineEdit(self.groupBox_2)
        self.cerca_txt.setObjectName(_fromUtf8("cerca_txt"))
        self.gridLayout_3.addWidget(self.cerca_txt, 1, 2, 1, 1)
        self.combo_cerca = QtGui.QComboBox(self.groupBox_2)
        self.combo_cerca.setObjectName(_fromUtf8("combo_cerca"))
        self.combo_cerca.addItem(_fromUtf8(""))
        self.combo_cerca.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.combo_cerca, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.combo_cerca, self.cerca_txt)
        Dialog.setTabOrder(self.cerca_txt, self.find)
        Dialog.setTabOrder(self.find, self.esci)
        Dialog.setTabOrder(self.esci, self.tableView)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Find contact", None))
        self.esci.setText(_translate("Dialog", "Close", None))
        self.find.setText(_translate("Dialog", "Find", None))
        self.label.setText(_translate("Dialog", "Find contact", None))
        self.combo_cerca.setItemText(0, _translate("Dialog", "Search by name", None))
        self.combo_cerca.setItemText(1, _translate("Dialog", "Search by surname", None))
        self.label_2.setText(_translate("Dialog", "Select ", None))

import rubrica_rc
