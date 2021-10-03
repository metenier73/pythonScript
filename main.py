#!/usr/bin/env python
# coding: utf-8
import os
import sys


# Fonction Princiale ###
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    try:
        rep0 = input(str("""
        Outils ordinateur 1 
        Disque 2 
        Réseau 3 
        Sécurité 4 
        où Quitter 5 ? 1|2|3|4|5 :"""))
        repo = int(rep0)
        while True:
            if rep0 == "1":
                print_Ordi()
            elif rep0 == "2":
                print_Di()
            elif rep0 == "3":
                print_R()
            elif rep0 == "4":
                print_S()
            elif rep0 == "5":
                sys.exit()
            elif rep0 > "5":
                print("nombre trop grand")
                rep0 = input("""
                Outils ordinateur 1
                Disque 2 
                Réseau 3 
                Sécurité 4 
                où Quitter 5 ? 1|2|3|4|5 :""")
            elif rep0 < "1":
                print("nombre trop petit")
                rep0 = input("""
                        Outils ordinateur 1
                        Disque 2
                        Réseau 3 
                        Sécurité 4 
                        où Quitter 5 ? 1|2|3|4|5 :""")
    except ValueError:
        print("Error : Vous devez entrer un nombre")
    print_hi(name)


# Commande ordinateur pour windows ###
# Evolution paramètrage automatique utilisateur add user + name ordinateur
def print_Ordi():
    try:
        ordi0 = input(str("""
        Administration ordinateur 1, Configuration ordinateur 2
        où Quitter 3 : 1|2|3 :"""))
        ordi = int(ordi0)
        if ordi0 == "1":
            ordi = input(str("""    
            Ajouter compte 1 
            Propriété System 2
            Analyse virus 3 
            Access Distance 4 
            Gestionnaire périphérique 5 
            où Quitter 6 ? 1|2|3|4|5|6:"""))
            if ordi == "1":
                os.system("netplwiz")
            elif ordi == "2":
                os.system("sysdm.cpl")
            elif ordi == "3":
                os.system("mrt")
            elif ordi == "4":
                os.system("mstsc")
            elif ordi == "5":
                os.system("hdwwiz.cpl")
            if ordi == "6":
                sys.exit()
        elif ordi0 == "2":
            ordi = input(str(
                """Gestion Ordinateur 1
                Sauvegarde 2
                Restauration 3
                Partition 4
                Restauration avec un support externe 5
                Créer un support de restauration 6 
                où Quitter 7 ? 1|2|3|4|5|6|7 :"""))
            if ordi == "1":
                os.system("CompMgmtLauncher.exe")
            elif ordi == "2":
                os.system("sdclt.exe")
            elif ordi == "3":
                os.system("RSTRUI")
            elif ordi == "4":
                os.system("DISKPART")
            elif ordi == "5":
                os.system("recdisc")
            elif ordi == "6":
                os.system("RecoveryDrive.exe")
            if ordi == "7":
                sys.exit()
        elif ordi0 == "3":
            sys.exit()
        elif ordi0 > "5":
            print("nombre trop grand")
            ordi0 = input(int("""
                    Administration ordinateur 1, Configuration ordinateur 2
                    où Quitter 3 : 1|2|3 :"""))
        elif ordi0 < "1":
            print("nombre trop petit")
            ordi0 = input(int("""
                        Administration ordinateur 1, Configuration ordinateur 2, 
                        ou Quitter 3 : 1|2|3 :"""))
    except ValueError:
        print("Error : Vous devez entrer un nombre")


# Commande disque pour windows ##
# Evolution fider fichier journal event, nettoyer les cles registres###
def print_Di():
    try:
        disc0 = input(str("Observation disque 1, Analyse disque 2 où Quitter 3 ? 1|2|3 :"))
        disc = int(disc0)
        if disc0 == "1":
            disc = input(str("""
            Observateur d'événements 1
            Registre 2
            Service 3
            Moniteur ressource 4
            Gestionnaire disque 5 
            où Quitter 6 ? 1|2|3|4|5 :"""))
            if disc == "1":
                os.system("Eventvwr.msc")
            elif disc == "2":
                os.system("Regedit.exe")
            elif disc == "3":
                os.system("services.msc")
            elif disc == "4":
                os.system("resmon")
            elif disc == "5":
                os.system("DISKMGMT.MSC")
            elif disc == "6":
                sys.exit()
        elif disc0 == "2":
            disc = input(
                str("""
            Nettoyer disque 1 
            Réinitialiser 2 
            Defragment 3 
            Mise à jour 4 
            où Quitter 5 ? 1|2|3|4|5 :"""))
            if disc == "1":
                os.system("cleanMgr")
            elif disc == "2":
                os.system("systemreset.exe")
            elif disc == "3":
                os.system("dfrgui.exe")
            elif disc == "4":
                os.system("WUAUCLT")
            elif disc == "5":
                sys.exit()
        elif disc0 == "3":
            sys.exit()
        elif disc0 > "5":
            print("nombre trop grand")
            disc0 = input(int("""
                Observation disque 1, Analyse disque 2 "
                "où Quitter 3 ? 1|2|3 :"""))
        elif disc0 < "1":
            print("nombre trop petit")
            disc0 = input(int("""
                Observation disque 1, Analyse disque 2 où Quitter 3 ? 1|2|3 :"""))
    except ValueError:
        print("Error : Vous devez entrer un nombre")


# Commande réseaux pour windows
# Configuration automatique connexion réseau
def print_R():
    try:
        lan0 = input(
            str("""
        Configuration IP 1
        Propriétés internet 2 
        Terminal 3 
        Connexion réseau 4 
        où Quitter 5 ? 1|2|3|4|5 :"""))
        lan = int(lan0)
        if lan0 == "1":
            os.system('IPCONFIG')
        elif lan0 == "2":
            os.system('INETCPL.CPL')
        elif lan0 == "3":
            os.system('cmd.exe')
        elif lan0 == "4":
            os.system('NCPA.CPL')
        elif lan0 == "5":
            sys.exit()
        elif lan0 > "5":
            print("nombre trop grand")
            lan0 = input(int("""
            Configuration IP 1
            Propriétés internet 2 
            Terminal 3 
            Connexion réseau 4 ? 
            où Quitter 5 ? 1|2|3|4|5 :"""))

        elif lan0 < "1":
            print("nombre trop petit")
            lan0 = input(int("""
                Configuration IP 1
                Propriétés internet 2 
                Terminal 3 
                Connexion réseau 4 ? 
                où Quitter 5 ? 1|2|3|4|5 :"""))

    except ValueError:
        print("Error : Vous devez entrer un nombre")


# Commande sécurité pour windows
def print_S():
    try:
        secu0 = input(str("""
        Pare-feu 1, Fonction avancées Pare-feu 2, Sécurité 3 où Quitter 4 ? 1|2|3|4 :"""))
        secu = int(secu0)
        if secu0 == "1":
            os.system("FIREWALL.CPL")
        elif secu0 == "2":
            os.system("WF.MSC")
        elif secu0 == "3":
            os.system("wscui.cpl")
        elif secu0 == "4":
            sys.exit()
        elif secu0 > "5":
            print("nombre trop grand")
            secu0 = input(int("""
            Pare-feu 1, Fonction avancées Pare-feu 2, Sécurité 3 ? 1|2|3 :"""))
        elif secu0 < "1":
            print("nombre trop petit")
            secu0 = input(int("""
            Pare-feu 1, Fonction avancées Pare-feu 2, Sécurité 3 ? 1|2|3 :"""))
    except ValueError:
        print("Error : Vous devez entrer un nombre")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Bienvenue dans l'analyseur :")
