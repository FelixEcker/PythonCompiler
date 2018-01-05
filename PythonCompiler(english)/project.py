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
    submit = input("Are you sure that you want delete '"+name+"' (y/n)")

    if submit == "y":
        print (Fore.RED+"Deleting of /projects/"+name+".json"+Fore.RESET)
        print (Fore.GREEN+"DONE!"+Fore.RESET)
        os.remove("projects/"+name+".json")
    else:
        print ("Canceld!")

def runProject():
    name = input("Project: ")
    
    with open("projects/"+name+".json") as data:
        jsondata = json.load(data)

        execfile = str(jsondata["src"]+"/"+jsondata["mainmodule"]+".py")

        os.system("python3 "+execfile)