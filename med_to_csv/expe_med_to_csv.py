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
from med_to_csv.file_med_to_csv import read_path

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
            chn = f"""\n\nMED : {listd[i]} Folder {i}/{nb_dirs-1}    {"-"*i}{"."*(nb_dirs-i-1)}
            Estimating Time Remaining  : {int(dtsp*(nb_dirs-i))//60}:{int(dtsp*(nb_dirs-i))%60} """
            print(chn+"\n"*1)
            if ptah.isdir(f"{path}/{listd[i]}") :
                try:
                    #+ and not .append to concatenate list and not make list of list of list of dic
                    # list_data = list_data + read_path(f"{path}/{listd[i]}", opt_dic)
                    output_lst = output_lst + [read_path(f"{path}/{listd[i]}", opt)]
                    output_df = pd.concat(output_lst)
                except Exception as err:
                    rep = input(
                        f"""A problem has occured while processing the data :
                        {err}\n \nContinue anyways?""")
                    if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                        raise RuntimeError(
                            f"""You have chosen to stop the execution after the following error:
                            {err}""") from err
            elif ptah.isfile(f"{path}/{listd[i]}") :
                output_df = read_path(f"{path}/", opt)
                break
            else :
                print(f"""The file {listd[i]} won't be analyzed""")
    except FileNotFoundError as e:
        print(f"WARNING! NO MED DIRECTORY DETECTED({e})")
    if output_file is not None :
        output_df.to_csv(output_file, sep=";", index=False)
    return output_df
