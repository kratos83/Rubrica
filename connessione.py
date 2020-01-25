import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *


#-------------------------------------------------------
# Creo la connessione al database SQLite e la relativa
# tabella
#-------------------------------------------------------
def creaConnessione():
	#Imposto la connessione al db sqlite
	db = QSqlDatabase.addDatabase('QSQLITE')
	#Imposto il database con il nome rubrica.db
	db.setDatabaseName('rubrica.db')
	#Se il dabatase non si apre allora lancia un 
	#messaggio di errore
	if not db.open():
		QMessageBox.critical(None,"Cannot open database",
		"Unable to estabilish a database connection...\n",
        QMessageBox.Ok)
		return False
	else:
		db.open()
	#Creo la tabella desiderata
	query = QSqlQuery()
	query.exec_("create table rubrica("
		    "id int primary key,"
		    "nome varchar(100),"
		    "cognome varchar(100),"
		    "indirizzo varchar(100),"
		    "mail varchar(100),"
		    "tel_casa varchar(100),"
		    "cellulare varchar(100))")
	return True
	
