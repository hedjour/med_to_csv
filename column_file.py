#! /usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Dict, List
from datetime import datetime
from numpy import nan
from global_parser_fun import global_selector

def parse_col(list_ligns:List, info : Dict) -> Dict:
    dic_scallar={}
    # Fichier une colonne
    dic_scallar["start_date"] =datetime.strptime(f"""{'-'.join([list_ligns[i]
                                                 for i in [2,0,1]])}""", "%y-%m-%d")
    dic_scallar["start_time"] = f"""{':'.join([list_ligns[i] for i in [10,11,12]])}"""
    for key, val in info.items():
        if key in "cuteval":
            pass
        elif not isinstance(val, list):
            dic_scallar[key] = list_ligns[val]
        elif len(val) == 2:
            dic_scallar[key] = list_ligns[val[0]:val[1]] if val[1] != "end" \
                else list_ligns[val[0]:] 
        else:
            raise SyntaxError(f"This value is not correctly defined : {val}")
    return dic_scallar


def col_selector(lst_dic, infos, path_file:str=None) :
    lst_out=[]
    for dic_selected in lst_dic :
        # On cherche la taille de la liste la plus grande
        n_listmax = max([len(i) if isinstance(i, list) else 1 for i in dic_selected.values()])
        # On alligne les key sur la taille de la liste la plus grande
        for key, val in dic_selected.items():
            if not isinstance(val, list):
                dic_selected[key] = [val] * n_listmax
            elif len(val) != n_listmax:
                dic_selected[key] = val.append([nan] * (n_listmax - len(val)))
            else:
                pass
        # We evaluate the keys eval and cut
        dic_selected = global_selector(dic_selected, infos, path_file)
        lst_out.append(dic_selected.copy())
    # end of for on dic list
    return lst_out
