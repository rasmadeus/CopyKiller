'''
Created on May 16, 2013

@author: rasmadeus
'''
import unittest
import os
import shutil
from model.copyKiller import CopyKiller

class Test(unittest.TestCase):

    def testListDirs(self):
        copyKiller = CopyKiller()
        self.assertEqual(copyKiller.getMd5('source/2.txt'), copyKiller.getMd5('source/3.txt'), "The same files")
        self.assertFalse(copyKiller.getMd5('source/2.txt') is copyKiller.getMd5('source/1.txt'), "The different files")
     
    def testCheckFiles(self):
        if os.path.exists('garbage'):
            shutil.rmtree('garbage')
        os.mkdir('garbage')
        if os.path.exists('testSrc'):
            shutil.rmtree('testSrc')
        shutil.copytree('source', 'testSrc')
        
        copyKiller = CopyKiller()
        copyKiller.unlockCheckFiles()
        copyKiller.checkFiles('testSrc', 'garbage')
        garbageFiles = os.listdir('garbage')
        testFiles = os.listdir('testSrc')
        print garbageFiles
        print testFiles
        self.assertTrue('2.txt' in garbageFiles, "Garbage dir")
        self.assertTrue('1.txt' in testFiles and '3.txt' in testFiles, 'TestDir')
     
                   
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testListDirs']
    unittest.main()