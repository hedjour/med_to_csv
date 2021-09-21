#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Variables
from os import listdir

#File one columns to test
path = "/home/jelongueville/Documents/Doctorants/Stevenson/Paper Food Punishment Procedure/foodpunish/Datas/G3/data brut/"
path_folder = f"{path}010221 s57/"
path_to_file = f"{path_folder}/{listdir(path_folder)[2]}"

#File labelled to test
path = "/home/jelongueville/Documents/Doctorants/Stevenson/Paper Food Punishment Procedure/foodpunish/Datas/G3/data brut/"
path_folder = f"{path}071220 s31/"
path_to_file = f"{path_folder}/{listdir(path_folder)[2]}"


#Fichier d'eric
path_file="/home/jelongueville/Documents/MPCdata/Setshift J1 Groupe A"
path = path_file

#Param1cln
import yaml
toto = './eric.yml'    
with open(toto, "r") as ymlfile:
    opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)

toto = './config.yml'    
with open(toto, "r") as ymlfile:
    opt_dic_2 = yaml.load(ymlfile, Loader=yaml.SafeLoader)
type(opt_dic["infos_col"]["subject"])