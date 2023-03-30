#!C:\Users\dkowa\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: utf-8 -*-
from datetime import datetime
import os


def header():
    os.system('cls')
    print("+-------------------------------------------------------------+")
    print("|IVC - (Pomocnik sporządzania karty weryfikacji wskaźników)   |")
    print("+-------------------------------------------------------------+")
    print("|Oprogramowanie do tworzenia i ewidencjonowania ścieżek audytu|")
    print("+-------------------------------------------------------------+")
    print("|Dzisiaj jest: ", datetime.now().strftime('%d.%m.%Y'), "                                   |")
    print("+-------------------------------------------------------------+")
    return


def zbierzdaneobiegudokumentow():
    print("\n")
    sprawa = input("Sprawa: ")
    dokument = input("Dokument: ")
    return (sprawa, dokument)


def importujdaneprojektu():
    return


def wprowadzdaneprojektu():
    zbierzdaneobiegudokumentow()
    return


def nowyprojekt():
    header()
    czyimport = input("Czy zaimportować dane z pliku? (T/N)")
    if czyimport.upper() == "T":
        print("Wprowadz sygnatury dokumentu\n----------------------------");
        importujdaneprojektu()
    if czyimport.upper() == "N": wprowadzdaneprojektu()
    return


def listaprojektow():
    return


def nowasciezka():
    header()
    print("Podaj dane nowej Karty weryfikacji")
    zbierzdaneobiegudokumentow()


def importujdanesciezki():
    return


def menuglowne():
    # wyświetlanie menu
    print("[N]owy projekt | [I]stniejący projekt")

    # obsługa menu
    opcja = input("Wybierz opcję i naciśnij Enter")
    if opcja.upper() == "N": nowyprojekt()
    if opcja.upper() == "I":
        listaprojektow()
    else:
        start()
    return


def start():
    header()
    menuglowne()

    return


# main

start()