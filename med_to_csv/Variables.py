#! /usr/bin/python3
# -*- coding: utf-8 -*-
#Variables
from os import listdir
import yaml

#File one columns to test
path = "/home/jelongueville/Documents/Doctorants/Stevenson/Paper Food Punishment Procedure/foodpunish/Datas/G3/data brut/"
path_folder = f"{path}010221 s57/"
path_file = f"{path_folder}/{listdir(path_folder)[2]}"

#File labelled to test
path = "/home/jelongueville/Documents/Doctorants/Stevenson/Paper Food Punishment Procedure/foodpunish/Datas/G3/data brut/"
path_folder = f"{path}071220 s31/"
path_file = f"{path_folder}/{listdir(path_folder)[2]}"
#Param1cln
toto = './med_to_csv/config.yml'
with open(toto, "r") as ymlfile:
    opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)

#Fichier d'eric
path_file="/home/jelongueville/Documents/MPCdata/Setshift J1 Groupe A"
path = path_file
toto = './eric.yml'    
with open(toto, "r") as ymlfile:
    opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)

# test stevenson
toto = '../../Doctorants/Stevenson/Cholesterol/config.yml'
with open(toto, "r") as ymlfile:
    opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)

path = "../../Doctorants/Stevenson/Cholesterol/G2\ 2021/"
path_folder = f"{path}{listdir(path)[0]}/"
path_to_file = f"{path_folder}/{listdir(path_folder)[2]}"

path_folder = "./Datas_Test/"
path = path_folder
path_to_file = f"{path_folder}/{listdir(path_folder)[0]}"
toto = f"{path_folder}/{listdir(path_folder)[1]}"
with open(toto, "r") as ymlfile:
    opt_dic = yaml.load(ymlfile, Loader=yaml.SafeLoader)