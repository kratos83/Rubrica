import sys

#include QT5
from PyQt5 import QtGui, QtCore, QtNetwork, QtSql, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *

#Importo la ui 
import about 

class info (QDialog, about.Ui_Dialog):
    
                    def __init__(self,  parent=None):
                                QDialog.__init__(self, parent)
                                self.setupUi(self)

				#Esco dalla finestra di dialogo. Posso utilizzare 
	   			#anche la scorciatoia di tastiera per uscire
	   			#cliccando Ctrl+S
				self.esci.clicked.connect(self.close)
				self.esci.setShortcut('Ctrl+E')


