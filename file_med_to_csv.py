#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module that reads files from Med Associates experiments to be used in expe_med_to_csv.py

Files read:
-------------
            \n
            data med/*\n
"""
import argparse
from pprint import pprint
from typing import Dict, List
from os import path as ptah, listdir
import yaml
import pandas as pd
from labelled_file import lab_selector, parse_labelled
from column_file import col_selector, parse_col
from global_parser_fun import global_selector

def read_path(path: str, opt_dic:Dict) -> pd.DataFrame:
    """Reads subject text files labelled or not and returns a dict or a list of dict"""
    infos_lab = opt_dic["infos_lab"] if "infos_lab" in opt_dic.keys() else None
    infos_col = opt_dic["infos_col"] if "infos_col" in opt_dic.keys() else None
    infos_opt = opt_dic["options"] if "options" in opt_dic.keys() else {"remove_zero_ending":False}
    infos_opt["path_file"] = path
    print("\n Labelled options :")
    pprint(infos_lab)
    print("\n 1 col options:")
    pprint(infos_col)
    print("\nGlobal options:")
    pprint(infos_opt)
    # charge(opt_path)
    if ptah.isdir(path):
        lst_res, lab = read_folder(path, infos_col, infos_opt["remove_zero_ending"])
    elif ptah.isfile(path):
        lst_res , lab = read_file(path, infos_col, infos_opt["remove_zero_ending"])
    else :
        raise RuntimeError("""Your path is neither a file or a directory oO
                           You must be a biologist only there can be this kind of stuff""")
    if lab:
        sel_res = lab_selector(lst_res, infos_lab, infos_opt["remove_zero_ending"])
    else:
        sel_res = col_selector(lst_res)
    sel_res = global_selector(sel_res, infos_opt)
    out_lst = []
    out_lst = out_lst + [pd.DataFrame(i)for i in sel_res]
    return pd.concat(out_lst)

def read_folder(path_folder: str, infos_col:Dict = None,
                remove_zero_ending:bool=False )-> List[Dict]:
    """Calls read_file for each text file in the directory"""
    listd = listdir(f"{path_folder}/")
    listd = [i for i in listd if "ubject" in i]
    lenfolder = len(listd)
    list_return = []
    for number_file in range(lenfolder):
        try:
            print(f"File: {number_file+1}/{lenfolder}, \"Animal {listd[number_file].split()[1]}\"")
            list_return = list_return + read_file(f"{path_folder}/{listd[number_file]}",
                                                  infos_col, remove_zero_ending)[0]
            lab = read_file(f"{path_folder}/{listd[number_file]}", infos_col, remove_zero_ending)[1]
        except IndexError as error:
            raise "The file name must ending by subject 'animal name'" from error
    return list_return, lab

def read_file(path_file:str, infos_col:Dict = None, remove_zero_ending:bool= False) -> List[Dict]:
    """Reads one file and returns a list of dict """
    with open(path_file, "r") as file:
        list_ligns = file.readlines()
        list_ligns = [i[:-1] for i in list_ligns[:]]
    if list_ligns[0][0].lower() in "abcdefghijklmnopqrstuvwxyz":
        #Labelled file
        res = parse_labelled(list_ligns)
        lab = True
    else :
        #File 1 column
        if infos_col is None :
            raise RuntimeError("""Paramétrage Incorrect I have found 1col file
                               And have no information about how read it""")
        res = parse_col(list_ligns, infos_col, remove_zero_ending)
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
    #Load user parameters
    with open(args.option, "r") as ymlfile:
        opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)
    # Reading the path
    df_res = read_path(args.path, opt_dic)
    df_res.to_csv(args.file, index=False)
