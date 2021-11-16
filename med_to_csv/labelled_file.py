#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module that parse labelled file
"""
from typing import Dict, List
from datetime import datetime
from re import compile as recompile
from string import ascii_uppercase as LETTERS


def parse_labelled(list_ligns:List)-> Dict or List(Dict):
    """
    Function that parse labelled file with 1 subject or more to a dictionary or to a list
    of dictionaries where each key is a label of the file
    """
    list_res = [] #List of animal dict
    dic_subject = {}
    first_animal=True
    #Parse Medassociate data all labelled types of files
    num = 0
    while num < len(list_ligns):
        row = list_ligns[num]
        row_split = row.rsplit(" ")
        #Useless first row
        if "File" in row or row == "" :
            pass
        elif "Start Date" in row :
            if not first_animal : #We manage the case of more than one subject
                list_res.append(dic_subject.copy())#To make sure values don't overwrite
                dic_subject = {}
            else:
                first_animal = False
            dic_subject[row.split(":")[0]] = row_split[-1]
        else :
            #Manage scalars infos from file
            if row.split(":")[0][0] in LETTERS and len(row.split(":")[0][0].split()) != 0:
                #first words not a letter and first char not space
                if len(row) == 2: #beginning of an array
                    dic_subject[row_split[0][:-1]] = []
                    key_array = row_split[0][:-1]
                else:
                    if f"""{row.split(":")[0]}:""" in [f"{i}:" for i in LETTERS]:
                        dic_subject[row.split(":")[0]] = row.split(":")[-1]
                    else:
                        dic_subject[row.split(":")[0]] = row.split(": ")[-1]
            else:
                #Reading of an array
                while num < len(list_ligns) and len(list_ligns[num]) not in (0,2):
                    #Case list_letters = a new array
                    list_comp = list_ligns[num].split(" ")
                    list_comp = [i for i in list_comp if i != ""][1:]
                    list_comp = [dic_subject[key_array].append(i) for i in list_comp]
                    #Manage the exit of an array, go up one line
                    num =  num + 1
                num = num - 1 if num < len(list_ligns) and len(list_ligns[num]) == 2 else num
            #End of else File / MED Values / Scalarray
        num += 1
        # End of for row
    return dic_subject if len(list_res)<2 else list_res


def lab_selector(lst_dic:List[Dict], infos:dict, remove_zero_ending:bool) -> List[Dict]:
    """function that returns a list of dictionaries containing lists of equal size """
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
                tmp_lst = dic_file[val[0]][val[1]:val[2]] if val[2] != "end" \
                    else dic_file[val[0]][val[1]:]
                if remove_zero_ending :
                    while bool(recompile(r"0.0+").match(tmp_lst[-1])) and len(tmp_lst) > 1:
                        tmp_lst = tmp_lst[:-1]
                dic_selected[key] = tmp_lst
            else:
                raise SyntaxError(f"This value is not correctly defined : {val}")
        #Manage the date
        dic_selected["start_date"] = datetime.strptime(dic_file["Start Date"], "%m/%d/%y")
        dic_selected["start_time"] = dic_file["Start Time"]
        lst_out.append(dic_selected.copy())
    # end of for on dic list
    return lst_out
