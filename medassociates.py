#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module qui lit les fichiers d'expériences Med Associates pour être utilisé par main.py

Fichiers lus:
-------------
            \n
            data med/*\n
"""

from os import listdir
from sys import argv
from typing import Generator
from sqlalchemy.engine.base import Connection  # typage

import pandas as pd

def read_file(path_to_file: str = "testfile.Subject 1") -> dict:
    "Fonction qui lit le fichier texte subject"
    file = open(path_to_file, "r")
    list_ligns = file.readlines()
    file.close()
    list_letters = [i[:-1] for i in list_ligns[:]]
    dic_return = {}
    for i in range(4,13):
        dic_return[list_letters[i].split(":")[0]] = list_letters[i].rsplit(" ")[-1]
    num = 13
    while num < len(list_letters):
        line_letter = list_letters[num]
        list_line_letter = line_letter.split(" ")
        if len(line_letter) != 2:
            dic_return[list_line_letter[0][:-1]] = list_line_letter[-1]
        else:
            dic_return[list_line_letter[0][:-1]] = []
            num += 1
            while num < len(list_letters) and len(list_letters[num]) != 14:
                list_comp = list_letters[num].split(" ")
                list_comp = [i for i in list_comp if i != ""][1:]
                list_comp = [dic_return[list_line_letter[0][:-1]].append(i) for i in list_comp]
                num += 1
        num += 1
    return dic_return

def read_folder(path: str, dfanimals: pd.DataFrame, con: Connection , aa_relapse: int = 0) -> Generator[dict, None, None]:
    "Fonction qui lance la lecture de chaque fichier texte du dossier"
    listd = listdir(f"{path}/")
    listd = [i for i in listd if "ubject" in i]
    lenfolder = len(listd)
    for i in range(lenfolder):
        file = open(f"{path}/{listd[i]}", "r")
        a = file.readline()
        if not(a[0].lower() in "abcdefghijklmnopqrstuvwxyz"):
            list_lines = file.readlines()
            list_return = [listd[i].split(" ")[-1]] + [list_lines[i][:-1] for i in [69,70,73] + [i for i in range(79,len(list_lines))]]
        else:
            dicexperience = read_file(f"{path}/{listd[i]}")
            list_return = [listd[i].split(" ")[-1]] + [dicexperience["Start Date"],dicexperience["Start Time"]] + [dicexperience["Z"][i][:-1] for i in [0,1,4] + [i for i in range(10,len(dicexperience["Z"]))]]
        file.close()
        while list_return[-1] in "0.000" and len(list_return)>6:
            list_return = list_return[:-1]
        while list_return[3][-1] in "0." and len(list_return[3])>1:
            list_return[3] = list_return[3][:-1]
        list_return[3] = int(list_return[3])

        list_return[0]="Animal "+list_return[0]
        listevents = []
        listaa = []
        listname = []
        print(list_return)
        for s in ["0.0"]+list_return[6:]:
            s=s.split(".")[0]
            s=int(s)+int(list_return[2].split(":")[2])
            m=int(list_return[2].split(":")[1])
            h=int(list_return[2].split(":")[0])
            while s >= 3600:
                h += 1
                s -= 3600
            while s >= 60:
                m += 1
                s -= 60
                if m >= 60:
                    m -= 60
                    h += 1
            date=f"{list_return[1]} {h}:{m}:{s}"
            a = str(date).split(" ")
            b = a[0].split("/")
            date=f"20{b[2]}-{b[0]}-{b[1]} {a[1]}"
            listevents.append(date)
            listaa.append(aa_relapse)       #opti : sortir de la boucle, comme constante
            listname.append(list_return[0]) #opti : sortir de la boucle, comme constante
        df=pd.DataFrame(list(zip(listevents[0:],listaa[0:],listname[0:])),columns=["dateT","aa_relapse","animal_name"]).merge(dfanimals,on="animal_name").rename(columns={"ID":"animal_id"})
        df[["animal_id","dateT","aa_relapse"]][1:].to_sql("aa_kinetics",con=con, if_exists="append",index=False)
        # print(df,listevents)
        con.execute(f"""INSERT INTO aa_vars(animal_id, nb_inj, dateT, aa_relapse) VALUES ('{df.at[0,"animal_id"]}', '{list_return[3]}', '{listevents[0]}', '{aa_relapse}')""")

# for i in read_folder("/home/mat/Documents/python/fill_bdd_phenoworld/PhW_relapse_AA_coc/Groupe-5/med_associate/auto_add/020421"):
#     print(i)
# if __name__ == "__main__":
#     read_file(*argv[:-1])
