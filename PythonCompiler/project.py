#!usr/bin/env python
#-*- coding: utf-8 -*-

import json, os
from colorama import *
init()

#Funktion um ein neues Projekt zu erstellen
def newProject():
    name = input("name: ")
    src = input("src: ")
    mainmodule = input("main: ")
    
    with open("projects/"+name+".json", "xt") as jsonData:
        jsonData.write('''
{
    "src":"'''+src+'''",
    "compdump":"'''+src+'''/compiled",
    "mainmodule":"'''+mainmodule+'''"
}
        ''') #Parameter in neu erstellte JSON schreiben
        

#Funktion um ein Projekt zu Löschen
def deleteProject():
    name = input("name: ")
    submit = input("Willst du die projekt config '"+name+"' wirklich löschen? (y/n)")

    if submit == "y":
        print (Fore.RED+"Löschen von /projects/"+name+".json"+Fore.RESET)
        print (Fore.GREEN+"Abgeschlossen!"+Fore.RESET)
        os.remove("projects/"+name+".json")
    else:
        print ("Abgebrochen!")

def runProject():
    name = input("Projekt: ")
    
    with open("projects/"+name+".json") as data:
        jsondata = json.load(data)

        execfile = str(jsondata["src"]+"/"+jsondata["mainmodule"]+".py")

        os.system("python3 "+execfile)