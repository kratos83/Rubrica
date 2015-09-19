import sys

#include QT4
from PyQt4 import QtGui, QtCore, QtSql
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

#Importo la ui 
import contact_save

class addSaveContact (QtGui.QDialog, contact_save.Ui_Dialog):
    
                    def __init__(self,  parent=None):
                                QDialog.__init__(self, parent)
                                self.setupUi(self)

				#Esco dalla finestra di dialogo. Posso utilizzare 
	   			#anche la scorciatoia di tastiera per uscire
	   			#cliccando Ctrl+S
				self.esci.clicked.connect(self.close)
				self.esci.setShortcut('Ctrl+E')
				#-----------------------------------------------
				#Inserisco i dati
				#-----------------------------------------------
				self.insert_contact.clicked.connect(self.insertContatto)

		    #Inserisco i contatti
		    def insertContatto(self):
				if self.name.text() == '' or self.surname.text() == '' or self.mobile.text() == '':
					QMessageBox.critical(self,"Enter data",
					"Data not available...\n",
        				QMessageBox.Ok)
				else:
					query = QSqlQuery() 
					query_id = QSqlQuery()
					query_id.exec_("select count(id)+1 from rubrica")
					if query_id.next():
						idRubrica = query_id.value(0).toString()
					query.prepare("INSERT INTO rubrica "
						    "VALUES ('"+str(idRubrica)+"','"+self.name.text()+"','"+self.surname.text()+"','"+self.address.text()+"',"
						    "'"+self.email.text()+"','"+self.phone.text()+"','"+self.mobile.text()+"')")

					if query.exec_():
						QMessageBox.information(self,"Address book",
						"Insert data successfully...\n",
       						QMessageBox.Ok)
					else:
						QMessageBox.information(self,"Address book",
						"Error insert data...\n"+str(query.lastError().text),
       						QMessageBox.Ok)
					
