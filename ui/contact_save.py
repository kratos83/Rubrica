# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/add_contact.ui'
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
        Dialog.resize(395, 308)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/system-users.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.insert_contact = QtGui.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.insert_contact.setIcon(icon1)
        self.insert_contact.setObjectName(_fromUtf8("insert_contact"))
        self.gridLayout.addWidget(self.insert_contact, 1, 1, 1, 1)
        self.esci = QtGui.QPushButton(Dialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/dialog-close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.esci.setIcon(icon2)
        self.esci.setObjectName(_fromUtf8("esci"))
        self.gridLayout.addWidget(self.esci, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.email = QtGui.QLineEdit(self.groupBox)
        self.email.setObjectName(_fromUtf8("email"))
        self.gridLayout_2.addWidget(self.email, 3, 1, 1, 1)
        self.name = QtGui.QLineEdit(self.groupBox)
        self.name.setObjectName(_fromUtf8("name"))
        self.gridLayout_2.addWidget(self.name, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.surname = QtGui.QLineEdit(self.groupBox)
        self.surname.setObjectName(_fromUtf8("surname"))
        self.gridLayout_2.addWidget(self.surname, 1, 1, 1, 1)
        self.phone = QtGui.QLineEdit(self.groupBox)
        self.phone.setObjectName(_fromUtf8("phone"))
        self.gridLayout_2.addWidget(self.phone, 4, 1, 1, 1)
        self.address = QtGui.QLineEdit(self.groupBox)
        self.address.setObjectName(_fromUtf8("address"))
        self.gridLayout_2.addWidget(self.address, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.mobile = QtGui.QLineEdit(self.groupBox)
        self.mobile.setObjectName(_fromUtf8("mobile"))
        self.gridLayout_2.addWidget(self.mobile, 5, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.name, self.surname)
        Dialog.setTabOrder(self.surname, self.address)
        Dialog.setTabOrder(self.address, self.email)
        Dialog.setTabOrder(self.email, self.phone)
        Dialog.setTabOrder(self.phone, self.mobile)
        Dialog.setTabOrder(self.mobile, self.insert_contact)
        Dialog.setTabOrder(self.insert_contact, self.esci)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Insert contact", None))
        self.insert_contact.setText(_translate("Dialog", "Insert", None))
        self.esci.setText(_translate("Dialog", "Close", None))
        self.groupBox.setTitle(_translate("Dialog", "Save new contact", None))
        self.label_4.setText(_translate("Dialog", "Email", None))
        self.label.setText(_translate("Dialog", "Name*", None))
        self.label_3.setText(_translate("Dialog", "Address", None))
        self.label_5.setText(_translate("Dialog", "Phone", None))
        self.label_2.setText(_translate("Dialog", "Surname*", None))
        self.label_6.setText(_translate("Dialog", "Mobile*", None))

import rubrica_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

