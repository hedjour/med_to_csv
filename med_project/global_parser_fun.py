#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""Module used by the two selector"""

from typing import Dict, List
from numpy import nan

def global_selector(lst_dic:List[Dict], infos_opt:Dict) -> List[Dict]:
    """
    Function that splits values following the 'cut' option and 
    applies the 'eval' option of the config file
    """
    out_lst = []
    path_file = infos_opt["path_file"]
    for dicexperience in lst_dic :
        if "eval" in infos_opt.keys() :
            for key, val in infos_opt["eval"].items() :
                dicexperience[key] = eval(val) #TODO need to be remplaced by ast.litteral_eval
        if "cut" in infos_opt.keys() :
            for lst_tmp in infos_opt["cut"]:
                keys=lst_tmp[0]
                sep=lst_tmp[1]
                sep_names = lst_tmp[2:]
                res_sep=[i.rsplit(sep) for i in dicexperience[keys]]
                #Add splitted elements
                dicexperience[sep_names[0]] = [i[0] for i in res_sep]
                dicexperience[sep_names[1]] = [i[1] if len(i)!= 1 else nan for i in res_sep]
        out_lst.append(dicexperience.copy())
    return out_lst

def listdic_equalizer(list_dic:List[Dict]) -> List[Dict]:
# Search for the longest list
    lst_out=[]
    for dic_selected in list_dic:
        n_listmax = max([len(i) if isinstance(i, list) else 1 for i in dic_selected.values()])
        # Align keys on the longest list
        for key, val in dic_selected.items():
            if not isinstance(val, list):
                dic_selected[key] = [val] * n_listmax
            elif len(val) != n_listmax:
                dic_selected[key] = val + [nan] * (n_listmax - len(val))
            else:
                pass
        lst_out.append(dic_selected.copy())
    return lst_out