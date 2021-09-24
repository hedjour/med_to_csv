#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
        MedAssociate_to_csv.
        This software read medassociate files to compile a csv file at first time for foodpunish
        experiment
"""
import argparse
from typing import Dict
from time import time
from os import listdir as ldir, path as ptah
import yaml
import pandas as pd
from file_med_to_csv import read_path

def main(path: str, output_file: str, opt_dic:Dict)->pd.DataFrame:
    """Takes path, dict from config file and output filename as parameter and returns a csv file"""
    try:
        tim_stamp = time()
        listd = [i for i in ldir(f"{path}") if i[0] != "."] #Listdir whithout dotfile
        listd = [i for i in listd if "PR" not in i]
        listd = [i for i in listd if "sh"  in i]
        nb_dirs = len(listd)
        output_lst=[]
        if len(listd) < 1 :
            raise SyntaxError("Be carreful your directory is empty")
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
                    output_lst = output_lst + [read_path(f"{path}/{listd[i]}", opt_dic)]
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("path", type=str,
                        help="""Path to the group directory which contains data files from :
                                - Medassociate
                                - Imetronic""")
    parser.add_argument("option", type=str, help= """Path to option config file.""")
    parser.add_argument("output", type=str,   help= """Path output of the csv file""")
    # parser.add_argument("-v","--verbose", type=str, help= """Verbose mode""")

    args = parser.parse_args()
    #load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    parser = argparse.ArgumentParser(prog="med_to_csv",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Auto is based on weight table to determine if animals are out.""")

    # print(f"path={args.path}, notes={args.notes}, sortie={args.sortie}, echo={args.verbose}")
    main(path=args.path, output_file = args.output, opt_dic=opt_dic)
