#!usr/bin/env python
#-*- coding: utf-8 -*-

""" TODO:
- Compiler Logik schreiben <--- FERTIG!
- Command mainloop schreiben <-- FERTIG!
- Projekt Config ersteller Erstellen <-- FERTIG!
- Ausführer schreiben <-- FERTIG!
"""


import os
import py_compile
import time
from pathlib import Path
import bools
import project
import compiler
from colorama import *

os.system("clear")

print ("Felix's Python Compiler 0.1.0, (C) 2018")
print()

# Command Input Funktion
def cmdin():
    global cmd
    cmd = input("] ")

cmdin()

while bools.running:
    if cmd == "np" or cmd == "newproject":
        project.newProject()
        cmdin()
    elif cmd == "cp" or cmd == "compileproject":
        compiler.CompileProject()
        cmdin()
    elif cmd == "runp" or cmd == "runproject":
        project.runProject()
        cmdin()
    elif cmd == "compile" or cmd == "c":
        compiler.compileSingle()
        cmdin()
    elif cmd == "dp" or cmd == "deleteproject":
        project.deleteProject()
        cmdin()
    elif cmd == "quit":
        print (Fore.GREEN + "Aufwiedersehn!"+Fore.RESET)
        time.sleep(1.2)
        os.system("clear")
        bools.running = False
    else:
        print (Fore.RED+"Fehler: Command not Found: "+cmd+Fore.RESET)
        cmdin()

exit()
