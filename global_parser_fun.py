#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Module used by the two selector"""

from os import pathconf
from typing import Dict
from numpy import nan

def global_selector(dicexperience:Dict, infos:Dict, path_file:str)->Dict:
    if "eval" in infos.keys() :
        for key, val in infos["eval"].items() :
            dicexperience[key] = eval(val)
    if "cut" in infos.keys() :
        for lst_tmp in infos["cut"]:
            keys=lst_tmp[0]
            sep=lst_tmp[1]
            sep_names = lst_tmp[2:]
            res_sep=[i.rsplit(sep) for i in dicexperience[keys]]
            #Ajout des elements splité
            dicexperience[sep_names[0]] = [i[0] for i in res_sep]
            dicexperience[sep_names[1]] = [i[1] if len(i)!= 1 else nan for i in res_sep]
    return dicexperience