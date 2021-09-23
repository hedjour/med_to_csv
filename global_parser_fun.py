#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Module used by the two selector"""

from os import pathconf
from typing import Dict, List
from numpy import nan

def global_selector(dicexperience:Dict, infos:Dict, infos_opt:Dict)->Dict:
    path_file = infos_opt["path_file"]
    if infos_opt["no_zero_ending_array"] :
        for key, val in dicexperience.items():
            if isinstance(val, List) :
                while val[-1] in "0" and len(val) > 1:
                    val = val[:-1]
    if "eval" in infos_opt.keys() :
        for key, val in infos_opt["eval"].items() :
            dicexperience[key] = eval(val)
    if "cut" in infos_opt.keys() :
        for lst_tmp in infos_opt["cut"]:
            keys=lst_tmp[0]
            sep=lst_tmp[1]
            sep_names = lst_tmp[2:]
            res_sep=[i.rsplit(sep) for i in dicexperience[keys]]
            #Ajout des elements splité
            dicexperience[sep_names[0]] = [i[0] for i in res_sep]
            dicexperience[sep_names[1]] = [i[1] if len(i)!= 1 else nan for i in res_sep]
    return dicexperience