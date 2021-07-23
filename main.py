#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
TODO FIXME REPRENDRE CE FICHIER DE FAÇON GLOBALE
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

    - Chargez ce programme avec votre IDE sur Windows, Linux, ou Mac, puis exécutez-le

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
from os import listdir as ldir
# ?Doit on importer que les fonctions dont on a besoin ?
import file_session_ic as IC
import file_session_im as IM
import imetronic as IMET
import animals_weight as AW
import medassociates as MED
import hotpopfield as HF
import experiment as EXP


def main(path: str = None, notes: str = None, sortie: str = None, echo = True, number_excel: int = None, con: Connection = None):
    # TODO Demander l'id d'experience
    tim_stamp = time()
    if path == None:
        path = input(
            "Quel est le chemin qui amène au dossier? (ex:\"/home/user/fill_bdd_phenoworld/Groupe-1/\") ")
    if path != "":
        grp = path.replace("/", "")[-1]
    else:
        grp = __file__[-9]
    print(grp)
    if not(grp in "1234567890"):
        grp=int(input("Quel est le numéro du groupe? "))
    if con == None:
        engine = create_engine(bdd_links, echo=(False if echo=="False" else True))
        con = engine.connect()
    print("connecté! on commence à travailler" if echo else "")
    id_xp = EXP.ask_exp_id(con)
    if sortie == None:
        sortie = input("Y a t-il eu une session où les animaux ne sont pas sortis ? ")
    sortie = sortie.replace(" ", "").lower() in "ouiyes"
    if notes == None:
        notes = input("Y a t-il une session avec des notes ? ")
    notes = notes.replace(" ", "").lower() in "ouiyes"
    
    ################################      Info_animals     ################################
    try:
        dfanimals = AW.main_weight(f"{path}", id_xp, con=con)
        dfanimals.rename(columns={"ID":"animal_id"},inplace=True)
    except FileNotFoundError:
        print("ATTENTION! PAS DE Fichier Excel DÉTÉCTÉ!")

    ######################################    MED    ######################################
    try:
        listd = ldir(f"{path}/med_associate")
        listd = [i for i in listd if i[0] != "."]
        nb_files = len(listd)
        for i in range(nb_files):
            dtsp = time()-tim_stamp
            tim_stamp = time()
            chn = f"""\n\nMED : {listd[i]} dossier {i}/{nb_files-1}    {"-"*i}{"."*(nb_files-i-1)}
            Temps restant estimé : {int(dtsp*(nb_files-i))//60}:{int(dtsp*(nb_files-i))%60} """
            print(chn+"\n"*5)
            listd2 = ldir(f"{path}/med_associate/{listd[i]}")
            listd2 = [i for i in listd2 if i[0] != "."]
            nb_files2 = len(listd2)
            for j in range(nb_files2):
                dtsp = time()-tim_stamp
                tim_stamp = time()
                test="""\n\nMED : {} dossier {}/{}    {}{}
{} :  dossier {}/{}    {}{}
Temps restant estimé : {}:{}{}""".format(listd[i],i,nb_files-1,"-"*i,"."*(nb_files-i-1),listd[i],
                    j,nb_files2-1,"-"*j,"."*(nb_files2-j-1),int(dtsp*((nb_files2*nb_files)-i))//60,
                    int(dtsp*((nb_files2*nb_files)-i))%60,"\n"*2)
                print(test)
                try:
                    MED.read_folder(f"{path}/med_associate/{listd[i]}/{listd2[j]}",dfanimals,con,0)
                except Exception as err:
                    rep = input(
                        f"Un problème est survenu pendant le traitement des données: \n{err}\n \nVoulez-vous quand même continuer?")
                    if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                        raise RuntimeError(
                            f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {err}")
    except FileNotFoundError as e:
        print(f"ATTENTION! PAS DE DOSSIER MED DÉTÉCTÉ!({e})")

    ######################################    IMET    ######################################
    try:
        IMET.imetronic_insert(f"{path}/imetronic", dfanimals, con)
        ld = ldir(path)
        if number_excel == None:
            number_excel = input(
                f"""Quel fichier excel correspond au groupe {grp}?{[f"{i}:{ld[i]}" for i in range(
                    len(ld))]}""")
        number_excel = int(number_excel)
    except FileNotFoundError:
        print("ATTENTION! PAS DE DOSSIER IMET DÉTÉCTÉ!")

    #############################     HotPlate / Openfield    #############################
    opfi = f"""{path}/{[file for file in ldir(f"{path}/openfield/") if file.endswith("XLS")][0]}"""
    xlsx_file = f"""{path}/{[file for file in ldir(path) if file.endswith("xlsx")][0]}"""
    HF.main(path_openfile= opfi, path_excel= xlsx_file, dfanimals=dfanimals, con=con)

    ######################################     IM    ######################################
    try:
        listd = ldir(f"{path}/IM")
        listd = [i for i in listd if i[0] != "."]
        nb_files = len(listd)
        dfanimalscopyIM = dfanimals[["RFID", "animal_name", "groupe", "animal_id"]]
        dfanimalscopyIM = dfanimalscopyIM.rename({"animal_name":"name","animal_id":"id"}) #!DELETE THIS Later
        for i in range(nb_files):
            dtsp = time()-tim_stamp
            tim_stamp = time()
            chn = f"""\n\nIM : {listd[i]} dossier {i}/{nb_files-1}    {"-"*i} {"."*(nb_files-i-1)}
            Temps restant estimé : {int(dtsp*(nb_files-i))//60}:{int(dtsp*(nb_files-i))%60} """
            print(chn+"\n"*5)
            try:
                if IC.notempty_phw_file(f"{path}/IM/{listd[i]}/AntennaReader/Antenna.txt"):
                    dfanimalscopyIM = IM.readfoldersessionIM(
                        f"{path}/IM/{listd[i]}/", con, grp, dfanimalscopyIM, chn, sortie, notes)
            except Exception as err:
                rep = input(
                    f"Un problème est survenu pendant le traitement des données: \n{err}\n \nVoulez-vous quand même continuer?")
                if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                    raise RuntimeError(
                        f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {err}")
    except FileNotFoundError:
        print("ATTENTION! PAS DE DOSSIER IM DÉTÉCTÉ!")

    ######################################    IC    ######################################
    try:
        listd = ldir(f"{path}/IC")
        listd = [i for i in listd if i[0] != "."]
        nb_files = len(listd)
        sessionsIC_infos = IC.get_sessions_ic_info(f"{path}/{listd[number_excel]}", con)
        for i in range(nb_files):
            dtsp = time()-tim_stamp
            tim_stamp = time()
            chn = f"""\n\nIC : {listd[i]} dossier {i}/{nb_files-1}    {"-"*i} {"."*(nb_files-i-1)}
            Temps restant estimé : {int(dtsp*(nb_files-i))//60}:{int(dtsp*(nb_files-i))%60} """
            print(chn+"\n"*5)
            try:
                if IC.notempty_phw_file(f"{path}/IC/{listd[i]}/IntelliCage/Visits.txt"):
                    #! NEED to be test
                    IC.read_folder_session_ic(sessions_infos=sessionsIC_infos, con=con,
                            path=f"{path}/IC/{listd[i]}/", dfanimals=dfanimals, chn=chn)
            except Exception as err:
                rep = input(
                    f"Un problème est survenu pendant le traitement des données: \n{err}\n \nVoulez-vous quand même continuer?")
                if not(rep.replace(" ", "").lower() in ["oui", "yes", "o", "y"]):
                    raise RuntimeError(
                        f"Vous avez choisi d'arreter l'éxécution après l'erreur suivante:\n {err}")
    except FileNotFoundError:
        print("ATTENTION! PAS DE DOSSIER IC DÉTÉCTÉ!")
    engine.dispose()


if __name__ == "__main__":
    main(*argv[1:])
