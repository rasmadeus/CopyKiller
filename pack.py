'''
Created on May 25, 2013

@author: rasmadeus
'''
from cx_Freeze import setup, Executable   

import sys

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(
    script='main.py',
    base = base
)

setup(   
    name = "CopyKiller",   
    version = "1.0",   
    console = "False",
    description = "Remove the same files",   
    executables = [exe]
) 