#Importo i file python
import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

#Importo la ui 
from ui import rubrica, info, lista_contatti,addSaveContact,deleteContact,addUpdateContact,findContact
from ui.info import info as Info
from ui.lista_contatti import lista_contatti as vistaContatto
from ui.addSaveContact import addSaveContact as saveContatto
from ui.deleteContact import deleteContact as delContatto
from ui.addUpdateContact import addUpdateContact as updateContatto
from ui.findContact import findContact as findContatto
#Importo la connessione al database
import connessione
#Importo il tempo
import time

class main (QMainWindow, rubrica.Ui_MainWindow):
    
                    def __init__(self,  parent=None):
                                super(main, self).__init__(parent)
                                self.setupUi(self)

				#Esco dalla main
				self.actionExit.triggered.connect(QCoreApplication.instance().quit)
                                #---------------------------------------------------
                                #Apro la finestra di dialogo about
				#---------------------------------------------------
                                self.about_contact.clicked.connect(self.openAbout)
				self.actionAbout.triggered.connect(self.openAbout)
                                #---------------------------------------------------
				#Apro la finestra di dialogo per la visualizzazione
				#dei contatti
				#---------------------------------------------------
				self.view_contact.clicked.connect(self.openViewContact)
				self.actionView_contact.triggered.connect(self.openViewContact)
				#---------------------------------------------------
				#Apro la finestra di dialogo per l'inserimento
				#dei contatti
				#---------------------------------------------------
				self.addContact.clicked.connect(self.openSaveContact)
				self.actionInsert.triggered.connect(self.openSaveContact)
				#---------------------------------------------------
				#Apro la finestra di dialogo per l'eliminazione
				#dei contatti
				#---------------------------------------------------
				self.remove_contatct.clicked.connect(self.openDelContact)
				self.actionRemove.triggered.connect(self.openDelContact)
				#---------------------------------------------------
				#Apro la finestra di dialogo per l'aggiornamento
				#dei contatti
				#---------------------------------------------------
                                self.update_contatc.clicked.connect(self.openUpdateContatto)
				self.actionUpdate.triggered.connect(self.openUpdateContatto)
				#---------------------------------------------------
				#Apro la finestra di dialogo per la ricerca
				#dei contatti
				#---------------------------------------------------
                                self.find_contact.clicked.connect(self.openFindContatto)
				self.actionFind_contact.triggered.connect(self.openFindContatto)

                    def openAbout(self):
                                self.info = QDialog()
                                self.info = Info()
                                self.info.exec_()
			
		    def openViewContact(self):
				self.lista_contatti = QDialog()
				self.lista_contatti = vistaContatto()
				self.lista_contatti.exec_()

		    def openSaveContact(self):
				self.add_contact = QDialog()
				self.add_contact = saveContatto()
				self.add_contact.exec_()

		    def openDelContact(self):
				self.deleteContact = QDialog()
				self.deleteContact = delContatto()
				self.deleteContact.exec_()

		    def openUpdateContatto(self):
				self.addUpdateContact = QDialog()
				self.addUpdateContact = updateContatto()
				self.addUpdateContact.exec_()
		
		    def openFindContatto(self):
				self.findContact = QDialog()
				self.findContact = findContatto()
				self.findContact.exec_()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	#app.setStyle(QStyleFactory.create("Oxygen"));
	if not connessione.creaConnessione():
	   sys.exit(1)

	form = main()
	sG = QApplication.desktop().screenGeometry()
	x = (sG.width()-form.width()) / 2
	y = (sG.height()-form.height()) / 2
	form.move(x,y)
	form.show()
	app.exec_()
