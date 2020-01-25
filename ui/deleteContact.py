import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

#Importo la ui 
import delete_contact

class deleteContact (QDialog, delete_contact.Ui_Dialog):
    
                    def __init__(self,  parent=None):
                                QDialog.__init__(self, parent)
                                self.setupUi(self)

				self.model = QSqlRelationalTableModel(self)

				#Esco dalla finestra di dialogo. Posso utilizzare 
	   			#anche la scorciatoia di tastiera per uscire
	   			#cliccando Ctrl+S
				self.esci.clicked.connect(self.close)
				self.esci.setShortcut('Ctrl+E')
				#Elimino i contatti all'interno della lista
				self.delete_2.clicked.connect(self.deleteAccount)
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
			self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers);

		    def deleteAccount(self):
			#Elimino il dato
			query = QSqlQuery()
			query.exec_("select * from rubrica where id='"+str(self.model.data(self.model.index(self.tableView.selectionModel().currentIndex().row(),self.tableView.selectionModel().currentIndex().column()),Qt.DisplayRole))+"'")
			#Visualizzo le informazioni
			box = QMessageBox(self)
			box.setWindowTitle("Address book")
			box.setInformativeText("Do you want to delete\n the selected record?")
			box.setStandardButtons( QMessageBox.Ok | QMessageBox.Cancel )
			box.setDefaultButton( QMessageBox.Ok )
			ret = box.exec_()
			if ret == QMessageBox.Ok:
				self.delAccount()
				box.close()
			else:
				box.close()

		    def delAccount(self):
			query = QSqlQuery()
			query.prepare("delete from rubrica where id='"+str(self.model.data(self.model.index(self.tableView.selectionModel().currentIndex().row(),self.tableView.selectionModel().currentIndex().column()),Qt.DisplayRole))+"'")

			if query.exec_():
				print "Delete successfully..."
			else:
				print query.lastError()
			self.lista()

