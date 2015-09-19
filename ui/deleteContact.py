import sys

#include QT4
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#Importo la ui 
import delete_contact

class deleteContact (QtGui.QDialog, delete_contact.Ui_Dialog):
    
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
			self.tableView.horizontalHeader().setResizeMode(QHeaderView.Stretch)
			self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers);

		    def deleteAccount(self):
			#Elimino il dato
			query = QSqlQuery()
			query.exec_("select * from rubrica where id='"+self.model.data(self.model.index(self.tableView.selectionModel().currentIndex().row(),self.tableView.selectionModel().currentIndex().column()),Qt.DisplayRole).toString()+"'")
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
			query.prepare("delete from rubrica where id='"+self.model.data(self.model.index(self.tableView.selectionModel().currentIndex().row(),self.tableView.selectionModel().currentIndex().column()),Qt.DisplayRole).toString()+"'")

			if query.exec_():
				print "Delete successfully..."
			else:
				print str(query.lastError().text)
			self.lista()

