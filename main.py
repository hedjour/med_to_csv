#! /usr/bin/python3
# -*- coding: utf-8 -*-
from time import time
import os
from posixpath import realpath
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection
from param import bdd_links
import filesessionIC as IC
import filesessionIM as IM
import imetronics as IMET
import animals_weight as AW
"""
TODO Organiser  
"""
def main(path: str = None, notes: str = None, sortie: str = None, n: int = None, con: Connection = None):

    a = time()
    if path == None:
        path = input(
            "Quel est le chemin qui amène au dossier? (ex:\"/home/user/fill_bdd_phenoworld/Groupe-1/\") ")
    if path != "":
        grp = path.replace("/", "")[-1]
    else:
        grp = __file__[-9]
    if con == None:
        engine = create_engine(bdd_links, echo=True)
        con = engine.connect()
    if sortie == None:
        sortie = input(
            "Y a t-il eu une session où les animaux ne sont pas sortis ? ")
    sortie = sortie.replace(" ", "").lower() in ["oui", "yes", "o", "y"]
    if notes == None:
        notes = input("Y a t-il une session avec des notes ? ")
    notes = notes.replace(" ", "").lower() in ["oui", "yes", "o", "y"]
    
    #On lit le fichier animals et charge les animaux en bdd ainsi que leur poids
    dfanimals=AW.main_weight(f"{path}",con=con)
    #Import de toutes les données Imetronics :
    dfimet = IMET.group_import(f"{path}/AA_PhW_G4", con, f"G{int(grp)+1}", dfanimals)
    [].sort
    ld = os.listdir(path)
    if n == None:
        n = input(
            f"""Quel fichier excel correcpond au groupe {grp}?{[f"{i}:{ld[i]}" for i in range(len(ld))]}""")
    n = int(n)
    sessionsIC_infos = IC.getSessionsIC_info(f"{path}/{ld[n]}", con)
    listd = os.listdir(f"{path}/IM")
    m = len(listd)
    dfanimalscopyIM=dfanimals[["RFID","name","groupe","id"]]
    for i in range(m):
        da=time()-a
        a=time()
        chn="\n"*5+f"\n\nIM : dossier {i} sur {m-1}      {listd[i]}\n"+"-"*i+"."*(m-i-1)+f"         Temps restant estimé : {int(da*(m-i))//60} m  {int(da*(m-i))%60} s"+"\n"
        print(chn+"\n"*5)
        try:
            if IC.check_file_txt(f"{path}/IM/{listd[i]}/AntennaReader/Antenna.txt"):
                dfanimalscopyIM = IM.readfoldersessionIM(f"{path}/IM/{listd[i]}/",con,grp,dfanimalscopyIM,chn,sortie,notes)
        except Exception as e:
            rep=input(f"Un problème est survenu pendant le traitement des données: \n{e}\n \nVoulez-vous quand même continuer?")
            if not(rep.replace(" ","").lower() in ["oui","yes","o","y"]):
                raise RuntimeError(f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {e}")
    listd = os.listdir(f"{path}/IC")
    m = len(listd)
    for i in range(m):
        da = time()-a
        a = time()
        chn = "\n"*5+f"\n\nIC : dossier {i} sur {m-1}      {listd[i]}\n"+"-"*i+"."*(
            m-i-1)+f"         Temps restant estimé : {int(da*(m-i))//60} m  {int(da*(m-i))%60} s"+"\n"
        print(chn+"\n"*5)
        try:
            if IC.check_file_txt(f"{path}/IC/{listd[i]}/IntelliCage/Visits.txt"):
                IC.readfoldersessionIC(
                    sessionsIC_infos, f"{path}/IC/{listd[i]}/", con, 1, dfanimals, chn)
        except Exception as e:
            rep = input(
                f"Un problème est survenu pendant le traitement des données: \n{e}\n \nVoulez-vous quand même continuer?")
            if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                raise RuntimeError(
                    f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {e}")
    engine.dispose()


main(*argv[1:])
