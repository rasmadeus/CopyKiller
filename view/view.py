# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Thu May 16 20:59:30 2013
#      by: The PyQt User Interface Compiler (pyuic) 3.18.1
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtGui, uic, QtCore
import resources
from model.copyKillerThread import  CopyKillerThread

class View(QtGui.QDialog):
    
    copyKiller = None
    srcDir = ''
    garbageDir = ''
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        uic.loadUi('view/view.ui', self)
        self.createConnections()        
       
    def closeEvent(self, event):
        if self.copyKiller is not None:
            self.stop()
        QtGui.QDialog.closeEvent(self,event)
       
    def createConnections(self):
        self.connect(self.startStopAction, QtCore.SIGNAL('clicked()'), self.startStop)
        self.connect(self.sourceAction, QtCore.SIGNAL('clicked()'), self.setSrcDir)
        self.connect(self.garbageAction, QtCore.SIGNAL('clicked()'), self.setGarbageDir)   
       
    def start(self):
        if self.srcDir is '' or self.garbageDir is '':
            return
        self.setEnabledIcon(False)
        self.copyKiller = CopyKillerThread(self)
        self.copyKiller.srcDir = self.srcDir
        self.copyKiller.setGarbageDir = self.garbageDir
        self.copyKiller.start()        
    
    def stop(self):
        self.copyKiller.stop()
        if self.copyKiller.isAlive():
            self.copyKiller.join()
        self.setEnabledIcon(True)
        del self.copyKiller        
    
    def setEnabledIcon(self, isTrue):
        self.sourceAction.setEnabled(isTrue)
        self.garbageAction.setEnabled(isTrue)
        self.startStopAction.setIcon(QtGui.QIcon(':/images/start.png' if isTrue else ':/images/stop.png'))
    
    def startStop(self):
        if self.copyKiller is None:
            self.start()
        else:
            self.stop()            
    
    def setSrcDir(self):
        self.srcDir = str(QtGui.QFileDialog.getExistingDirectory(self, 'Set source dir...'))
        
    
    def setGarbageDir(self):
        self.garbageDir = str(QtGui.QFileDialog.getExistingDirectory(self, 'Set garbage dir...'))   
        