#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module qui lit les fichiers d'expériences Med Associates pour être utilisé par main.py

Fichiers lus:
-------------
            \n
            IM/session/RunningWheel/Registration.txt        pour la db wheels     \n
            IM/session/AntennaReader/Antenna.txt            pour la db antenna_read     \n
            IM/session/Animals/Animals.animals              pour la db animals     \n

Attention!
----------
Ne pas exécuter ce fichier seul, la connexion n'y est pas définie,
récupérez le modèle de main pour l'ouvrir et la fermer.
"""
from sys import argv
import main

def read_file(path_to_file: str = "testfile.Subject 1"):
    "Fonction qui lit le fichier texte subject"
    file = open(path_to_file, "r")
    list_ligns = file.readlines()
    file.close()
    print("".join(list_ligns))
    list_letters = [i[:-1] for i in list_ligns[13:]]
    dic_letters = {}
    num = 0
    while num < len(list_letters):
        line_letter = list_letters[num]
        print(f"#{line_letter}#")
        list_line_letter = line_letter.split(" ")
        if len(line_letter) == 14:
            dic_letters[list_line_letter[0][:-1]] = list_line_letter[-1]
        else:
            dic_letters[list_line_letter[0][:-1]] = []
            num += 1
            while num < len(list_letters) and len(list_letters[num]) != 14:
                list_comp = list_letters[num].split(" ")
                list_comp = [i for i in list_comp if i != ""][1:]
                list_comp = [dic_letters[list_line_letter[0][:-1]].append(i) for i in list_comp]
                num += 1
        num += 1
    print(dic_letters)

if __name__=="__main__":
    read_file(*argv[:-1])
