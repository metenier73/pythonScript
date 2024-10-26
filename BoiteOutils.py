import os
import sys
import tkinter as tk
from tkinter import messagebox

# Function mappings for each action
def run_command(command):
    os.system(command)

def on_quit():
    if messagebox.askokcancel("Quitter", "Voulez-vous vraiment quitter ?"):
        root.destroy()

# Command functions
def ordinateur_tools():
    tools_window = tk.Toplevel(root)
    tools_window.title("Outils Ordinateur")
    
    tk.Button(tools_window, text="Ajouter un compte", command=lambda: run_command("netplwiz")).pack(pady=5)
    tk.Button(tools_window, text="Propriétés Système", command=lambda: run_command("sysdm.cpl")).pack(pady=5)
    tk.Button(tools_window, text="Analyse Virus", command=lambda: run_command("mrt")).pack(pady=5)
    tk.Button(tools_window, text="Gestionnaire Périphériques", command=lambda: run_command("hdwwiz.cpl")).pack(pady=5)
    tk.Button(tools_window, text="Mise à jour",command=lambda: run_command("wuauclt.exe")).pack(pady=5)
	
def disque_tools():
    tools_window = tk.Toplevel(root)
    tools_window.title("Outils Disque")

    tk.Button(tools_window, text="Gestionnaire Disque", command=lambda: run_command("DISKMGMT.MSC")).pack(pady=5)
    tk.Button(tools_window, text="Défragmentation", command=lambda: run_command("dfrgui.exe")).pack(pady=5)
    tk.Button(tools_window, text="Nettoyage Disque", command=lambda: run_command("cleanmgr")).pack(pady=5)

def reseau_tools():
    tools_window = tk.Toplevel(root)
    tools_window.title("Outils Réseau")

    tk.Button(tools_window, text="Configuration IP", command=lambda: run_command("ipconfig")).pack(pady=5)
    tk.Button(tools_window, text="Propriétés Internet", command=lambda: run_command("inetcpl.cpl")).pack(pady=5)
    tk.Button(tools_window, text="Terminal", command=lambda: run_command("cmd.exe")).pack(pady=5)

def securite_tools():
    tools_window = tk.Toplevel(root)
    tools_window.title("Outils Sécurité")

    tk.Button(tools_window, text="Pare-feu", command=lambda: run_command("firewall.cpl")).pack(pady=5)
    tk.Button(tools_window, text="Paramètres Sécurité", command=lambda: run_command("wscui.cpl")).pack(pady=5)

# Main window setup
root = tk.Tk()
root.title("Boîte à Outils Windows")
root.geometry("800x400")

# Main menu buttons
tk.Label(root, text="Sélectionnez une catégorie :", font=("Helvetica", 14)).pack(pady=40)
tk.Button(root, text="Ordinateur", command=ordinateur_tools, width=40).pack(pady=5)
tk.Button(root, text="Disque", command=disque_tools, width=40).pack(pady=5)
tk.Button(root, text="Réseau", command=reseau_tools, width=40).pack(pady=5)
tk.Button(root, text="Sécurité", command=securite_tools, width=40).pack(pady=5)
tk.Button(root, text="Quitter", command=on_quit, width=40).pack(pady=5)

root.mainloop()