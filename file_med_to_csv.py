#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module qui lit les fichiers d'expériences Med Associates pour être utilisé par main.py

Fichiers lus:
-------------
            \n
            data med/*\n
"""
import argparse
import yaml
import pandas as pd
from os import path as ptah, listdir
from typing import Dict, List
from labelled_file import lab_selector, parse_labelled
from column_file import col_selector, parse_col

def read_path(path: str, opt_dic:Dict) -> pd.DataFrame:
    """Fonction qui lit le fichier texte subject en format labelisé ou une cln et retourne un dict 
    ou une liste de dic"""
    infos_lab = opt_dic["infos_lab"] if "infos_lab" in opt_dic.keys() else None
    infos_col = opt_dic["infos_col"] if "infos_col" in opt_dic.keys() else None
    # TODO Add a summary of parameters to print to user
    print(f"infos_lab : {infos_lab} \n infos_col = {infos_col} ")
    # charge(opt_path)
    if ptah.isdir(path):
        lst_res, lab = read_folder(path, infos_col)
    elif ptah.isfile(path):
        lst_res , lab = read_file(path, infos_col)
    else :
        raise RuntimeError("""Votre chemin n'est ni un fichier ni un directory oO
                           You must be a biologist only there can be this kind of stuff""")
    if lab:
        sel_res = lab_selector(lst_res, infos_lab, path)
    else:
        sel_res = col_selector(lst_res, infos_col, path)
    out_lst = []
    out_lst = out_lst + [pd.DataFrame(i)for i in sel_res]
    return pd.concat(out_lst)

def read_folder(path_folder: str, infos_col:Dict = None) -> List[Dict]:
    "Fonction qui lance la lecture de chaque fichier texte du dossier"
    listd = listdir(f"{path_folder}/")
    listd = [i for i in listd if "ubject" in i]
    lenfolder = len(listd)
    list_return = []
    for number_file in range(lenfolder):
        try:
            print(f"File: {number_file+1}/{lenfolder}, \"Animal {listd[number_file].split()[1]}\"")
        except IndexError as error:
            raise "The file name must ending by subject 'animal name'" from error
        list_return.append( read_file(f"{path_folder}/{listd[number_file]}", infos_col)[0])
        lab = read_file(f"{path_folder}/{listd[number_file]}", infos_col)[1]
    return list_return, lab

def read_file(path_file:str, infos_col:Dict = None) -> List[Dict]:
        # On lit le fichier
    file = open(path_file, "r")
    list_ligns = file.readlines()
    list_ligns = [i[:-1] for i in list_ligns[:]] #on vire les retours à la ligne.
    file.close()
    if list_ligns[0][0].lower() in "abcdefghijklmnopqrstuvwxyz":
        #File labelled
        res = parse_labelled(list_ligns)
        lab = True
    else :
        #File 1 column
        if infos_col == None :
            raise RuntimeError("""Paramétrage Incorrect I have found 1col file
                               And have no information about how read it""")
        res = parse_col(list_ligns, infos_col)
        lab = False
    res = [res] if isinstance(res, Dict) else res
    return res, lab

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("path", type=str,
                        help="""Path to the group directory which contains data files from :
                                - Medassociate
                                - Imetronic""")
    parser.add_argument("option", type=str,
                        help= """Path to option config file.""")
    parser.add_argument("file", type=str,
                        help= """Path output of the csv file""")

    args = parser.parse_args()
    #On charge les paramètre utilisateur
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    # On lit le path
    df_res = read_path(args.path, opt_dic)
    df_res.to_csv(args.file, index=False)