# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_contact.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(551, 334)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/edit-delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.esci = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/dialog-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.esci.setIcon(icon1)
        self.esci.setObjectName("esci")
        self.gridLayout.addWidget(self.esci, 1, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.delete_2 = QtWidgets.QPushButton(Dialog)
        self.delete_2.setIcon(icon)
        self.delete_2.setObjectName("delete_2")
        self.gridLayout.addWidget(self.delete_2, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Delete contact"))
        self.esci.setText(_translate("Dialog", "Close"))
        self.delete_2.setText(_translate("Dialog", "Delete"))

import rubrica_rc
