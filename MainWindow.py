# coding: utf-8
#author: Jhin Yao

import adbtool
from MainWindowUi import Ui_MainWindow
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox)


class MyMainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MyMainWindow, self).__init__()
		self.setupUi(self)

	def install(self):
		pass

	def refresh(self):
		pass

	def uninstall(self):
		pass




