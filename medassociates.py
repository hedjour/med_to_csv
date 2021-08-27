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
from typing import Generator
from sqlalchemy.engine.base import Connection  # typage
import pandas as pd
from warnings import warn

def read_file(path_to_file: str = "testfile.Subject 1") -> dict:
    "Fonction qui lit le fichier texte subject"
    file = open(path_to_file, "r")
    list_ligns = file.readlines()
    file.close()
    list_letters = [i[:-1] for i in list_ligns[:]]
    dic_return = {}
    for i in range(4, 13):
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

def read_folder(path_folder: str, dfanimals: pd.DataFrame, con: Connection,
                aa_relapse: int = 0) -> Generator[dict, None, None]:
    "Fonction qui lance la lecture de chaque fichier texte du dossier"
    listd = listdir(f"{path_folder}/")
    listd = [i for i in listd if "ubject" in i]
    lenfolder = len(listd)
    for number_file in range(lenfolder):
        try:
            print(f"File: {number_file}/{lenfolder}, \"Animal {listd[number_file].split()[1]}\"")
        except IndexError :
            raise "The file name must ending by subject 'animal name'"
        if f"Animal {listd[number_file].split()[1]}" in dfanimals["animal_name"].values :
            file = open(f"{path_folder}/{listd[number_file]}", "r")
            list_lines = file.readlines()
            if not list_lines[0][0].lower() in "abcdefghijklmnopqrstuvwxyz":
                list_return = [listd[number_file].split(" ")[-1]] +\
                            [f"{'/'.join([list_lines[i][:-1] for i in [0,1,2]])}",
                            f"{':'.join([list_lines[i][:-1] for i in [10,11,12]])}"]+\
                            [list_lines[i][:-1] for i in [70, 71, 74] +\
                            [i for i in range(80, len(list_lines))]]
            else:
                dicexperience = read_file(f"{path_folder}/{listd[number_file]}")
                list_return = [listd[number_file].split(" ")[-1]] +\
                            [dicexperience["Start Date"], dicexperience["Start Time"]] +\
                            [dicexperience["Z"][i][:-1] for i in [0, 1, 4] +\
                            [i for i in range(10, len(dicexperience["Z"]))]]
            file.close()
            while list_return[-1] in "0.000" and len(list_return) > 6:
                list_return = list_return[:-1]
            while list_return[3][-1] in "0." and len(list_return[3]) > 1:
                list_return[3] = list_return[3][:-1]
            list_return[3] = int(list_return[3])
            list_return[0] = "Animal "+list_return[0]
            listevents = []
            for secondes in ["0.0"] + list_return[6:]:
                secondes = secondes.split(".")[0]
                secondes = int(secondes)+int(list_return[2].split(":")[2])
                minutes = int(list_return[2].split(":")[1])
                heures = int(list_return[2].split(":")[0])
                while secondes >= 3600:
                    heures += 1
                    secondes -= 3600
                while secondes >= 60:
                    minutes += 1
                    secondes -= 60
                    if minutes >= 60:
                        minutes -= 60
                        heures += 1
                date = f"{list_return[1]} {heures}:{minutes}:{secondes}"
                date1 = str(date).split(" ")
                date2 = date1[0].split("/")
                date = f"20{date2[2]}-{date2[0]}-{date2[1]} {date1[1]}"
                listevents.append(date)
            df_return = pd.DataFrame(listevents[0:], columns=["dateT"])
            df_return["aa_relapse"] = aa_relapse
            df_return["animal_name"] = list_return[0]
            df_return = df_return.merge(dfanimals, on="animal_name")
            df_return[["animal_id", "dateT", "aa_relapse"]][1:
                ].to_sql("aa_kinetics", con=con, if_exists="append",index=False)
            con.execute(f"""INSERT INTO aa_vars(animal_id, nb_inj, dateT, aa_relapse) VALUES ('{df_return.at[0,
                        "animal_id"]}', '{list_return[3]}', '{listevents[0]}', '{aa_relapse}')""")
        else: #subject not in dfanimals
            warn(f"The {listd[number_file]} is not an animal present in df animals")

