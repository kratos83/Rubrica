import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

#Importo la ui 
import find_contact

class findContact (QDialog, find_contact.Ui_Dialog):
    
                    def __init__(self,  parent=None):
                                QDialog.__init__(self, parent)
                                self.setupUi(self)

				self.model = QSqlRelationalTableModel()
				#Esco dalla finestra di dialogo. Posso utilizzare 
	   			#anche la scorciatoia di tastiera per uscire
	   			#cliccando Ctrl+S
				self.esci.clicked.connect(self.close)
				self.esci.setShortcut('Ctrl+E')
				#Avvio la ricerca
				self.find.clicked.connect(self.filtro)
				self.cerca_txt.textEdited.connect(self.cercaUtente)
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

		    def cercaUtente(self,QString):
			if self.combo_cerca.currentIndex() == 0:
				list_st = QStringList()
				query = QSqlQuery()
				query.prepare("select nome from rubrica")
				if query.exec_():
					while query.next():
						list_st << query.value(0)
				completer = QCompleter(list_st,self)
				completer.setCaseSensitivity(Qt.CaseInsensitive)
				self.cerca_txt.setCompleter(completer)
			elif self.combo_cerca.currentIndex() == 1:
				list_st = QStringList()
				query = QSqlQuery()
				query.prepare("select cognome from rubrica")
				if query.exec_():
					while query.next():
						list_st << query.value(0).toString()
				completer = QCompleter(list_st,self)
				completer.setCaseSensitivity(Qt.CaseInsensitive)
				self.cerca_txt.setCompleter(completer)

		    def filtro(self):
                        if self.cerca_txt.text() == "":
                                QMessageBox.critical(None,"Address book","Insert data...\n",QMessageBox.Ok)
                        elif self.combo_cerca.currentIndex() == 0:
                                self.model.setFilter(QString("nome = '"+str(self.cerca_txt.text())+"'").arg(self.cerca_txt.text()))
			elif self.combo_cerca.currentIndex() == 1:
                                self.model.setFilter(QString("cognome = '"+self.cerca_txt.text()+"'").arg(self.cerca_txt.text()))
