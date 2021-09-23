#! /usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Dict, Generator, List
from datetime import datetime
from string import ascii_uppercase as LETTERS
from numpy import nan


def parse_labelled(list_ligns:List)-> Dict or List(Dict):
    """Function to parse labelled file with 1 subject or more to dictionnary or list
    of dictionnary in each dictionnary each Key is a label of the file"""
    list_res = [] #Liste des dicanimals
    dic_subject = {}
    first_animal=True
    #Parse Medassociate data all labelled type files
    num = 0
    while num < len(list_ligns):
        row = list_ligns[num]
        row_split = row.rsplit(" ")
        #Première ligne du fichier inutile
        if "File" in row or row == "" : 
            pass
        elif "Start Date" in row :
            if not first_animal : #On gère le cas plus d'un subject
                list_res.append(dic_subject.copy())#.copy pour être sur de ne pas écraser les valeurs dans la liste
                dic_subject = {}
            else:
                first_animal = False
            dic_subject[row.split(":")[0]] = row_split[-1]
        else :
            #On gère les scallars infos from file
            if row.split(":")[0][0] in LETTERS and len(row.split(":")[0][0].split()) != 0:
                #premiers mots soit pas une lettre et que le premier char ne soit pas un espace
                if len(row) == 2: #Debut d'un array
                    dic_subject[row_split[0][:-1]] = []
                    key_array = row_split[0][:-1]
                else:
                    if f"""{row.split(":")[0]}:""" in [f"{i}:" for i in LETTERS]:
                        dic_subject[row.split(":")[0]] = row.split(":")[-1] 
                    else:
                        dic_subject[row.split(":")[0]] = row.split(": ")[-1]
            else:
                #Lecture du array
                while num < len(list_ligns) and len(list_ligns[num]) not in (0,2):
                    #Cas list_letters = a new array
                    list_comp = list_ligns[num].split(" ")
                    list_comp = [i for i in list_comp if i != ""][1:]
                    list_comp = [dic_subject[key_array].append(i) for i in list_comp]
                    #Gestion de la sortie du array on remonte d'une ligne
                    num =  num + 1
                num = num - 1 if num < len(list_ligns) and len(list_ligns[num]) == 2 else num
            # Fin du else File / MED Values / Scalarray
        num += 1
        # Fin du for row
    return dic_subject if len(list_res)<2 else list_res


def lab_selector(lst_dic:List[Dict], infos:dict) -> List[Dict]:
    lst_out=[]
    for dic_file in lst_dic :
        dic_selected={}
        for key, val in infos.items():
            # print(f"make_dic_select key | val : {key} | {val} ")
            if key in "cuteval":
                pass
            elif not isinstance(val, list):
                dic_selected[key] = dic_file[val]
            elif len(val) == 2:
                dic_selected[key] = dic_file[val[0]][val[1]]
            elif len(val) == 3:
                dic_selected[key] = dic_file[val[0]][val[1]:val[2]] if val[2] != "end" \
                    else dic_file[val[0]][val[1]:]
            else:
                raise SyntaxError(f"This value is not correctly defined : {val}")
        # On cherche la taille de la liste la plus grande
        n_listmax = max([len(i) if isinstance(i, list) else 1 for i in dic_selected.values()])
        #Gestion de la date 
        dic_selected["start_date"] = datetime.strptime(dic_file["Start Date"], "%m/%d/%y")
        dic_selected["start_time"] = dic_file["Start Time"]
        # On alligne les key sur la taille de la liste la plus grande
        for key, val in dic_selected.items():
            if not isinstance(val, list):
                dic_selected[key] = [val] * n_listmax
            elif len(val) != n_listmax:
                dic_selected[key] = val + [nan] * (n_listmax - len(val))
            else:
                pass
        lst_out.append(dic_selected.copy())
    # end of for on dic list
    return lst_out
