#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
        MedAssociate_to_csv.
        This software read medassociate files to compile a csv file at first time for foodpunish
        experiment
"""
from typing import Dict
from time import time
from os import listdir as ldir, path as ptah
import pandas as pd
import re
from med_project.file_med_to_csv import read_path

def main(path: str, output_file: str, opt:Dict)->pd.DataFrame:
    """Takes path, dict from config file and output filename as parameter and returns a csv file"""
    try:
        tim_stamp = time()
        listd = [i for i in ldir(f"{path}") if i[0] != "."] #Listdir whithout dotfile
        if "options" in opt.keys() and "filter" in opt["options"].keys() :
            listd = list(filter(re.compile(opt["options"]["filter"]).search, listd))
        nb_dirs = len(listd)
        output_lst=[]
        if len(listd) < 1 :
            raise SyntaxError("Be careful your directory is empty")
        for i in range(nb_dirs):
            dtsp = time()-tim_stamp
            tim_stamp = time()
            chn = f"""\n\nMED : {listd[i]} dossier {i}/{nb_dirs-1}    {"-"*i}{"."*(nb_dirs-i-1)}
            Temps restant estimé : {int(dtsp*(nb_dirs-i))//60}:{int(dtsp*(nb_dirs-i))%60} """
            print(chn+"\n"*1)
            if ptah.isdir(f"{path}/{listd[i]}") :
                try:
                    #+ and not .append to concatenate list and not make list of list of list of dic
                    # list_data = list_data + read_path(f"{path}/{listd[i]}", opt_dic)
                    output_lst = output_lst + [read_path(f"{path}/{listd[i]}", opt)]
                    output_df = pd.concat(output_lst)
                except Exception as err:
                    rep = input(
                        f"""Un problème est survenu pendant le traitement des données:
                        {err}\n \nVoulez-vous quand même continuer?""")
                    if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                        raise RuntimeError(
                            f"""Vous avez choisi d'arreter l'éxécution après l'erreur suivante:
                            {err}""") from err
            else :
                print(f"""Le fichier {listd[i]} n'est pas analysé.""")
    except FileNotFoundError as e:
        print(f"ATTENTION! PAS DE DOSSIER MED DÉTÉCTÉ!({e})")
    if output_file is not None :
        output_df.to_csv(output_file, sep=";", index=False)
    return output_df
