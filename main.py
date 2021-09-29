import os
import sys

###Fonction Princiale ###
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    rep0 = input("Outils Ordinateur, Disque, Réseau où Sécurité voulez-vous continué ? o|n:")
    while rep0 == "o":
        choix = input("Outils Ordinateur, Disque, Réseau, Sécurité où n pour quitter ? 1|2|3|4 :")
        if rep0 == "o":
            if choix == "1":
                print_Ordi(name)
            elif choix == "2":
                print_Di(name)
            elif choix == "3":
                print_R(name)
            elif choix == "4":
                print_S(name)
            elif choix == "n":
                sys.exit()
        elif rep0 == "n":
            sys.exit()

#Commande ordinateur pour windows ###
###Evolution paramètrage automatique utilisateur add user + name ordinateur
def print_Ordi(name):
    ordi0 = input("Administration ordinateur 1, Configuration ordinateur 2 : 1|2 :")
    if ordi0 == "1":
        ordi = input("Ajouter compte 1, Propriété System 2,Analyse virus 3 ,Access Distance 4 ,Gestionnaire périphérique 5 ? 1|2|3|4|5:")
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

    if ordi0 == "2":
        ordi = input("Gestion Ordinateur 1, Sauvegarde 2, Restauration 3, Partition 4, Restauration avec un support externe 5, Créer un support de restauration 6 ? 1|2|3|4|5|6 :")
        if ordi =="1":
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

#Commande disque pour windows ##
###Evolution fider fichier journal event, nettoyer les cles registres###
def print_Di(name):
    disc0 = input("Observation disque, Analyse disque ? 1|2 :")
    if disc0 == "1":
        disc = input("Observateur d'événements 1, Registre 2, Service 3, Moniteur ressource 4, Gestionnaire disque ? 1|2|3|4|5 :")
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

    elif disc0 == "2":
        disc = input("Nettoyer disque 1, Réinitialiser 2, Defragment 3, Mise à jour 4 ? 1|2|3|4 :")
        if disc == "1":
            os.system("cleanMgr")
        elif disc == "2":
            os.system("systemreset.exe")
        elif disc == "3":
            os.system("dfrgui.exe")
        elif disc == "4":
            os.system("WUAUCLT")

##Commande réseaux pour windows ###
###Configuration automatique connexion réseau###
def print_R(name):

    lan = input("Configuration IP 1, Propriétés internet 2, Terminal 3, Connexion réseau 4 ? 1|2|3|4 :")
    if lan == "1":
        os.system('IPCONFIG')
    elif lan == "2":
        os.system('INETCPL.CPL')
    elif lan == "3":
        os.system('cmd.exe')
    elif lan == "4":
        os.system('NCPA.CPL')

###Commande sécurité pour windows ###
def print_S(name):

    secu = input("Pare-feu 1, Fonction avancées Pare-feu 2, Sécurité 3 ? 1|2|3 :")
    if secu == "1":
        os.system("FIREWALL.CPL")
    elif secu == "2":
        os.system("WF.MSC")
    elif secu == "3":
        os.system("wscui.cpl")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi("Bienvenue dans l'analyseur :")

