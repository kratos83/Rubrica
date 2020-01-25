import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

#Importo la ui 
import update_contact

class addUpdateContact (QDialog, update_contact.Ui_Dialog):
    
                    def __init__(self,  parent=None):
                                QDialog.__init__(self, parent)
                                self.setupUi(self)

				self.model = QSqlRelationalTableModel(self)
				#Esco dalla finestra di dialogo. Posso utilizzare 
	   			#anche la scorciatoia di tastiera per uscire
	   			#cliccando Ctrl+S
				self.esci.clicked.connect(self.close)
				self.esci.setShortcut('Ctrl+E')
				#Visualizzo la lista
				self.lista()

		    def lista(self):
			#Imposto la tabella all'interno della vista
			self.model.setTable('rubrica')
			self.model.select()

			#Imposto gli header da visualizzare
			self.model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
        		self.model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
        		self.model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
			self.model.setHeaderData(3, QtCore.Qt.Horizontal, "Address")
        		self.model.setHeaderData(4, QtCore.Qt.Horizontal, "Email")
        		self.model.setHeaderData(5, QtCore.Qt.Horizontal, "Phone")
			self.model.setHeaderData(6, QtCore.Qt.Horizontal, "Mobile")

			#Visualizzo i dati all'interno della tabella
			self.tableView.setModel(self.model)
			self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)			
