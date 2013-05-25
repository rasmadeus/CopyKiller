'''
Created on May 22, 2013

@author: rasmadeus
'''

from glob import glob
from py2deb import Py2deb

p = Py2deb("copykiller")
p.author="K.Kulikov"
p.mail="rasmadeus@gmail.com"
p.description = "Remove the same files"
p.license = "gpl"
p.section = "utils"
p.arch = "all"
p.depends = "python, python-qt4"
p.icon = ""
p["/usr/bin/CopyKiller"] = ["main.py","view/__init__.py", "view/resources.py","view/view.py","view/view.ui","model/__init__.py","model/copyKiller.py","model/copyKillerThread.py","garbage.png"]
p["/usr/share/applications"] = ["copyKiller.desktop"]
p.generate("1.0")