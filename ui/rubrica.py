# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/rubrica.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(229, 331)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/system-users.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.about_contact = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_contact.setIcon(icon1)
        self.about_contact.setObjectName(_fromUtf8("about_contact"))
        self.gridLayout_2.addWidget(self.about_contact, 5, 0, 1, 1)
        self.remove_contatct = QtGui.QPushButton(self.groupBox)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_contatct.setIcon(icon2)
        self.remove_contatct.setObjectName(_fromUtf8("remove_contatct"))
        self.gridLayout_2.addWidget(self.remove_contatct, 2, 0, 1, 1)
        self.find_contact = QtGui.QPushButton(self.groupBox)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edit-find.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_contact.setIcon(icon3)
        self.find_contact.setObjectName(_fromUtf8("find_contact"))
        self.gridLayout_2.addWidget(self.find_contact, 4, 0, 1, 1)
        self.update_contatc = QtGui.QPushButton(self.groupBox)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/system-software-update.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_contatc.setIcon(icon4)
        self.update_contatc.setObjectName(_fromUtf8("update_contatc"))
        self.gridLayout_2.addWidget(self.update_contatc, 3, 0, 1, 1)
        self.addContact = QtGui.QPushButton(self.groupBox)
        self.addContact.setIcon(icon)
        self.addContact.setObjectName(_fromUtf8("addContact"))
        self.gridLayout_2.addWidget(self.addContact, 1, 0, 1, 1)
        self.view_contact = QtGui.QPushButton(self.groupBox)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_contact.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_contact.setIcon(icon5)
        self.view_contact.setObjectName(_fromUtf8("view_contact"))
        self.gridLayout_2.addWidget(self.view_contact, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 229, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionInsert = QtGui.QAction(MainWindow)
        self.actionInsert.setIcon(icon)
        self.actionInsert.setObjectName(_fromUtf8("actionInsert"))
        self.actionRemove = QtGui.QAction(MainWindow)
        self.actionRemove.setIcon(icon2)
        self.actionRemove.setObjectName(_fromUtf8("actionRemove"))
        self.actionUpdate = QtGui.QAction(MainWindow)
        self.actionUpdate.setIcon(icon4)
        self.actionUpdate.setObjectName(_fromUtf8("actionUpdate"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(icon1)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionFind_contact = QtGui.QAction(MainWindow)
        self.actionFind_contact.setIcon(icon3)
        self.actionFind_contact.setObjectName(_fromUtf8("actionFind_contact"))
        self.actionView_contact = QtGui.QAction(MainWindow)
        self.actionView_contact.setIcon(icon5)
        self.actionView_contact.setObjectName(_fromUtf8("actionView_contact"))
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionView_contact)
        self.menuEdit.addAction(self.actionInsert)
        self.menuEdit.addAction(self.actionRemove)
        self.menuEdit.addAction(self.actionUpdate)
        self.menuEdit.addAction(self.actionFind_contact)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Address book", None))
        self.about_contact.setText(_translate("MainWindow", "About", None))
        self.remove_contatct.setText(_translate("MainWindow", "Remove contact", None))
        self.find_contact.setText(_translate("MainWindow", "Find contact", None))
        self.update_contatc.setText(_translate("MainWindow", "Update contact", None))
        self.addContact.setText(_translate("MainWindow", "Add contact", None))
        self.view_contact.setText(_translate("MainWindow", "View contact", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionInsert.setText(_translate("MainWindow", "Add contact", None))
        self.actionRemove.setText(_translate("MainWindow", "Remove contact", None))
        self.actionUpdate.setText(_translate("MainWindow", "Update contact", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionFind_contact.setText(_translate("MainWindow", "Find contact", None))
        self.actionView_contact.setText(_translate("MainWindow", "View contact", None))

import rubrica_rc
