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
    name = input("Project> ")

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
                logging.info("Started compiling...")
                timerStart = timer()
                for path in src.rglob("*.py"):
                    if path.is_file():
                        fileNumber += 1
                        fileNumber = str(fileNumber)
                        _path = str(path)
                        print ("Compiling: "+_path+"; Name: comp"+fileNumber+".pyc;")
                        logging.info("Compiling: "+_path)
                        py_compile.compile(path, projectdata["compdump"]+"/comp"+fileNumber+".pyc")
                        logging.info("Done! File: comp"+fileNumber+".pyc;")
                        fileNumber = int(fileNumber)
                timerEnd = timer()
                Time = str(timerStart - timerEnd) + " seconds"
                logging.info("Compiling Done! Time taken: "+Time)
                print (Fore.GREEN + "Project succesfull compiled! Time taken: "+ Time + Fore.RESET)
            else:
                print (Fore.RED+"Projectdirectory could not be found!" + Fore.RESET)
    else:
        print(Fore.RED + "Project configuration file could not be found!" + Fore.RESET)


def compileSingle():
    path = input("Path to .py file> ")

    timerStart = timer()
    py_compile.compile(path, path+"c")
    
    timerEnd = timer()

    Time = str(timerStart - timerEnd) + " seconds"
    
    print (Fore.GREEN + "File succesfull compiled! Time taken: "+ Time + Fore.RESET)


def deleteLogContents(src):
    with open(src+"/compiled/compile.log", "w"):
        pass