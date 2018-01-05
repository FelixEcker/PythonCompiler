#!usr/bin/env python
#-*- coding: utf -8 -*-

import os
import py_compile
import json
import logging
from pathlib import Path
from colorama import *
from timeit import default_timer as timer

init()

def CompileProject():
    name = input("Projekt> ")

    if os.path.isfile("projects/"+name+".json"):
        with open("projects/" + name + ".json") as projectJSON:
            projectdata = json.load(projectJSON)
            src = Path(projectdata["src"])

            print (src)#

            _src = str(src)

            fileNumber = 0

            logging.basicConfig(filename=_src+"/compiled/compile.log", level=logging.DEBUG) 

            deleteLogContents(_src)

            if True:
                logging.info("Kompilieren Wurde gestartet...")
                timerStart = timer()
                for path in src.rglob("*.py"):
                    if path.is_file():
                        fileNumber += 1
                        fileNumber = str(fileNumber)
                        _path = str(path)
                        print ("Wird Kompiliert: "+_path+"; Name: comp"+fileNumber+".pyc;")
                        logging.info("Wird Kompiliert: "+_path)
                        py_compile.compile(path, projectdata["compdump"]+"/comp"+fileNumber+".pyc")
                        logging.info("Fertig! Datei: comp"+fileNumber+".pyc;")
                        fileNumber = int(fileNumber)
                timerEnd = timer()
                Time = str(timerStart - timerEnd) + " seconds"
                logging.info("Kompileren Abgeschlossen! Time taken: "+Time)
                print (Fore.GREEN + "Projekt wurde Erfolgreich Kompiliert! Time taken: "+ Time + Fore.RESET)
            else:
                print (Fore.RED+"Projektordner konnte nicht gefunden werden!" + Fore.RESET)
    else:
        print(Fore.RED + "Projket Konfiguaration konnte nicht gefunden werden!" + Fore.RESET)


def compileSingle():
    path = input("Pfad zur einzelen .py datei> ")

    timerStart = timer()
    py_compile.compile(path, path+"c")
    
    timerEnd = timer()

    Time = str(timerStart - timerEnd) + " seconds"
    
    print (Fore.GREEN + "Datei wurde Erfolgreich Kompiliert! Time taken: "+ Time + Fore.RESET)


def deleteLogContents(src):
    with open(src+"/compiled/compile.log", "w"):
        pass