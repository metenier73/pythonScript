import os
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    rep0 = input("Outils du disque, réseau où sécurité continué ? o|n:")
    while rep0 == "o":
        rep0 = input("Outils du disque, réseau où sécurité continué ? o|n:")
        if rep0 == "o":
            choix = input("Outils du disque, réseau où sécurité ? 1|2|3 :")
            if choix == "1":
                print_Di(name)
            elif choix == "2":
                print_R(name)
            elif choix == "3":
                print_S(name)
        elif rep0 == "n":
            sys.exit()

def print_Di(name):
    disc0 = input ("Observation disque, Analyse disque, restauration ? 1|2|3 :")
    if disc0 == "1":
        disc = input("Observateur d'événements 1, Propriétés système 2, Registre 3 ? 1|2|3 :")
        if disc == "1":
            os.system("Eventvwr.msc")
        elif disc == "2":
            os.system("sysdm.cpl")
        elif disc == "3":
            os.system("Regedit.exe")

    elif disc0 == "2":
        disc = input("Check Disk 1, Check NTFS 2,Defragment 3 ? 1|2|3:")
        if disc == "1":
            os.system("CHKDSK")
        elif disc == "2":
            os.system("CHKNTFS c:")
        elif disc == "3":
            os.system("DEFRAG")

    elif disc0 == "3":
        disc = input("Restauration 1, Partition 2 ? 1|2 :")
        if disc == "1":
            os.system("strui.exe")
        elif disc == "2":
            os.system("DISKPART")

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
    print_Di("Outils du disque : ")
    print_R("Outils du réseau :")
    print_S("Outils sécurité ")
