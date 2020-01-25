# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'find_contact.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(584, 359)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/edit-find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.esci = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/dialog-close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.esci.setIcon(icon1)
        self.esci.setObjectName("esci")
        self.gridLayout.addWidget(self.esci, 4, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(184, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.find = QtWidgets.QPushButton(Dialog)
        self.find.setIcon(icon)
        self.find.setObjectName("find")
        self.gridLayout.addWidget(self.find, 4, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.cerca_txt = QtWidgets.QLineEdit(self.groupBox_2)
        self.cerca_txt.setObjectName("cerca_txt")
        self.gridLayout_3.addWidget(self.cerca_txt, 1, 2, 1, 1)
        self.combo_cerca = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_cerca.setObjectName("combo_cerca")
        self.combo_cerca.addItem("")
        self.combo_cerca.addItem("")
        self.gridLayout_3.addWidget(self.combo_cerca, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.combo_cerca, self.cerca_txt)
        Dialog.setTabOrder(self.cerca_txt, self.find)
        Dialog.setTabOrder(self.find, self.esci)
        Dialog.setTabOrder(self.esci, self.tableView)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Find contact"))
        self.esci.setText(_translate("Dialog", "Close"))
        self.find.setText(_translate("Dialog", "Find"))
        self.label.setText(_translate("Dialog", "Find contact"))
        self.combo_cerca.setItemText(0, _translate("Dialog", "Search by name"))
        self.combo_cerca.setItemText(1, _translate("Dialog", "Search by surname"))
        self.label_2.setText(_translate("Dialog", "Select "))

import rubrica_rc
