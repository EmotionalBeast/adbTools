# coding: utf-8
#author: Jhin Yao

import os

class adbtool(object):
	PMC = "adb shell getprop ro.product.model"
	INSP = "adb install "
	UNINSP = "adb uninstall "

	@classmethod
	def getPhoneModel(self):
		phoneModel = os.popen(PMC).read()
		return phoneModel

	@classmethod
	def installApp(self, path):
		installCommand = INSP + path
		info = os.popen(installCommand).read()
		return info
		
	@classmethod
	def uninstallApp(self, packageName):
		uninstallCommand = UNINSP + packageName
		info = os.popen(uninstallCommand).read()
		return info
  

