'''
Created on May 19, 2013

@author: rasmadeus
'''
import  threading
from copyKiller import CopyKiller

class CopyKillerThread(threading.Thread):

    srcDir = ''
    garbageDir = ''
    copyKiller = CopyKiller()
    view = None

    def __init__(self, view):
        threading.Thread.__init__(self)
        self.view = view
        
    def run(self):
        self.copyKiller.unlockCheckFiles()
        self.copyKiller.clean()
        self.copyKiller.checkFiles(self.srcDir, self.garbageDir)
        self.stop()
        self.view.setEnabledIcon(True)
    
    def stop(self):
        self.copyKiller.lockCheckFiles()