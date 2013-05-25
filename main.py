'''
Created on May 22, 2013

@author: rasmadeus
'''
from view.view import View
from PyQt4 import QtGui
import sys
import sip
from encodings import ascii

def main():
    copyKiller = QtGui.QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(copyKiller.exec_())

if __name__ == '__main__':
    main()