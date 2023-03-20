#!C:\Users\dkowa\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
from datetime import datetime
import os

def zbierzdaneobiegudokumentow():
    print ("Podaj dane ścieżki\n")
    sprawa = input ("Sprawa: ")
    dokument = input ("Dokument: ")
    iddokumentu=sprawa+"("+dokument+")"
    return(sprawa,dokument,iddokumentu)

def nowasciezka():
    print("Podaj dane nowej Karty weryfikacji")

def importujdanesciezki():
    return()

#main
os.system("cls")
nowasciezka()
dane_sciezki=zbierzdaneobiegudokumentow()
print (datetime.now().strftime('%d.%m.%Y %H:%M'))
dzien=datetime.now().strftime('%d')
print ("Sprawa: ",dane_sciezki[0])
print ("Dokument: ",dane_sciezki[1])
print ("Identfikator dokumentu:",dane_sciezki[2])
print ("Dzisiaj jest",dzien,"dzień miesiąca")