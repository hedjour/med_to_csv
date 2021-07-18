#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Module de lecture de données du PhénoWorld
------------------------------------------
Permet la lecture des dossiers :
    - IntelliMaze    (partie IM)
    - IntelliCage    (partie IC)
    - Imetronics     (partie IMET)
    - Medassociates  (partie MED)

Et la lecture de fichiers généraux, comme le fichier
excel des poids, des procédures PhW, et des dispositions de biberon.

Utilisation:
------------
Vous pouvez utiliser ce programme de différentes façons:
    - Lancez ce programme par un double clic sur Linux, puis suivez les instructions dans le
     terminal python qui s'ouvrira pour les inputs
    - Lancez ce programme en lignes de commandes dans un terminal sur Linux. Selon votre
     installation, vous pourriez utiliser la commande suivante:
     `$/usr/bin/python3 /home/mat/Documents/python/fill_bdd_phenoworld/main.py`
     suivie des paramètres.
        Les paramètres (optionnels) sont :
            - le chemin vers le dossier contenant les informations sur votre groupe de rats (de la
             forme Groupe-3 par exemple), par défaut "", soit l'emplacement actuel.
            - si "oui" ou "non" il y a besoin d'entrer des notes dans la base de données(le cas
             échéant, vous demandera à chaque session IM de les saisir)
            - si "oui" ou "non" une session s'est déroulée sans sortie des animaux(sera demandé de
             même à chaque session IM)
            - la position de votre fichier excel dans la liste des fichiers du dossier du groupe
             (sera demandé à la lecture de ce fichier, au début de l'exécution)
            - la connexion sqlalchemy si vous avez besoin de la définir dans un autre script

    - Chargez ce programme avec votre IDE sur Windows ou Linux, puis exécutez-le

Dépendances:
------------
Exécutez le script InstallDependencies.sh sur Linux; le script batch pour Windows viendra peut être plus tard.

"""
from time import time
import os
# from posixpath import realpath
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection
from param import bdd_links

import filesessionIC as IC
import filesessionIM as IM
import imetronic as IMET
import animals_weight as AW
import medassociates as MED

def main(path: str = None, notes: str = None, sortie: str = None, number_excel: int = None, con: Connection = None):
    a = time()
    if path == None:
        path = input(
            "Quel est le chemin qui amène au dossier? (ex:\"/home/user/fill_bdd_phenoworld/Groupe-1/\") ")
    if path != "":
        grp = path.replace("/", "")[-1]
    else:
        grp = __file__[-9]
    print(grp)
    if not(grp in ["1","2","3","4","5","6","7","8","9","0"]):
        grp=int(input("Quel est le numéro du groupe? "))
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

    ############################    MED    ######################################

    listd = os.listdir(f"{path}/med_associate")
    m = len(listd)
    for i in range(m):
        da = time()-a
        a = time()
        chn = "\n"*5+f"\n\nMED : dossier {i} sur {m-1}      {listd[i]}\n"+"-"*i+"."*(
            m-i-1)+f"         Temps restant estimé : {int(da*(m-i))//60} m  {int(da*(m-i))%60} s"+"\n"
        print(chn+"\n"*5)
        try:
            MED.read_folder(f"{path}/med_associate/{listd[i]}/")
        except Exception as e:
            rep = input(
                f"Un problème est survenu pendant le traitement des données: \n{e}\n \nVoulez-vous quand même continuer?")
            if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                raise RuntimeError(
                    f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {e}")

    ############################    IMET    ######################################

    # On lit le fichier animals et charge les animaux en bdd ainsi que leur poids
    dfanimals = AW.main_weight(f"{path}", con=con)
    # Import de toutes les données Imetronics :
    IMET.imetronic_insert(f"{path}/AA_PhW_G4", dfanimals, con)
    ld = os.listdir(path)
    if number_excel == None:
        number_excel = input(
            f"""Quel fichier excel correspond au groupe {grp}?{[f"{i}:{ld[i]}" for i in range(
                len(ld))]}""")
    number_excel = int(number_excel)
    sessionsIC_infos = IC.getSessionsIC_info(f"{path}/{ld[number_excel]}", con)

    ############################    IM    ######################################

    listd = os.listdir(f"{path}/IM")
    m = len(listd)
    dfanimalscopyIM = dfanimals[["RFID", "name", "groupe", "id"]]
    for i in range(m):
        da = time()-a
        a = time()
        chn = "\n"*5+f"\n\nIM : dossier {i} sur {m-1}      {listd[i]}\n"+"-"*i+"."*(
            m-i-1)+f"         Temps restant estimé : {int(da*(m-i))//60} m  {int(da*(m-i))%60} s"+"\n"
        print(chn+"\n"*5)
        try:
            if IC.check_file_txt(f"{path}/IM/{listd[i]}/AntennaReader/Antenna.txt"):
                dfanimalscopyIM = IM.readfoldersessionIM(
                    f"{path}/IM/{listd[i]}/", con, grp, dfanimalscopyIM, chn, sortie, notes)
        except Exception as e:
            rep = input(
                f"Un problème est survenu pendant le traitement des données: \n{e}\n \nVoulez-vous quand même continuer?")
            if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                raise RuntimeError(
                    f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {e}")

    ############################    IC    ######################################

    listd = os.listdir(f"{path}/IC")
    m = len(listd)
    for i in range(m):
        da = time()-a
        a = time()
        chn = "\n"*5+f"\n\nIM : dossier {i} sur {m-1}      {listd[i]}\n"+"-"*i+"."*(
            m-i-1)+f"         Temps restant estimé : {int(da*(m-i))//60} m  {int(da*(m-i))%60} s"+"\n"
        print(chn+"\n"*5)
        try:
            if IC.check_file_txt(f"{path}/IM/{listd[i]}/AntennaReader/Antenna.txt"):
                dfanimalscopyIM = IM.readfoldersessionIM(
                    f"{path}/IM/{listd[i]}/", con, grp, dfanimalscopyIM, chn, sortie, notes)
        except Exception as e:
            rep = input(
                f"Un problème est survenu pendant le traitement des données: \n{e}\n \nVoulez-vous quand même continuer?")
            if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                raise RuntimeError(
                    f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {e}")
    engine.dispose()

if __name__ == "__main__":
    main(*argv[1:])
