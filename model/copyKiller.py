import hashlib
import shutil
import os

class CopyKiller(object):
    isRun = False
    
    def lockCheckFiles(self):
        self.isRun = False   
        
    def unlockCheckFiles(self):
        self.isRun = True 
        
    def isLock(self):
        return self.isRun
    
    def getMd5(self, pathToFile):
        with open(pathToFile, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()  

    hashFiles = []

    def clean(self):
        self.hashFiles[:] = []
        
    def checkFile(self, pathToFile, garbageDir):
        md5 = self.getMd5(pathToFile)
        if md5 in self.hashFiles:
            shutil.move(pathToFile, garbageDir)
        else:
            self.hashFiles.append(md5)

    def checkFiles(self, srcDir, garbageDir):
        if not self.isRun:
            return
        listDir = []
        try:
            listDir = os.listdir(srcDir)
        except:
            return
        for path in listDir:
            pathToFile = os.path.join(srcDir, path)
            if pathToFile is not garbageDir:
                if os.path.isfile(pathToFile):
                    self.checkFile(pathToFile, garbageDir)
                elif os.path.isdir(pathToFile):
                    self.checkFiles(pathToFile, garbageDir)