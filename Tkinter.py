from tkinter import *
import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from tkinter import ttk
import csv

# def ajouter_joueur(entry_element, pointage):
#     nouveau_joueur = entry_element.get()
#     liste = [nouveau_joueur, pointage]
#     if len(nouveau_joueur) < 5:
#         messagebox.showinfo("Saisie du joueur", "Le nom du joueur doit avoir au moins 5 caractères")
#     else:
#         with open ("scores.csv", "a", encoding="utf-8", newline='') as fichierCSV:
#             ecriture = csv.writer(fichierCSV, delimiter=";")
#             for enregistrement in liste:    
#                 ecriture.writerow(enregistrement)



def main():
    fenetre = tk.Tk()
    fenetre.title("Space Invader")

    # Entrée pour ajouter un nouvel élément
    label_element = ttk.Label(fenetre, text="Nom du joueur:")
    label_element.grid(row=0, column=1, padx=10, pady=10)

    entry_element = ttk.Entry(fenetre, width=30)
    entry_element.grid(row=1, column=1, padx=10, pady=10)

    bouton_ajouter = ttk.Button(fenetre, text="OK", command=lambda: ajouter_joueur(entry_element))
    bouton_ajouter.grid(row=2, column=1, padx=10, pady=10)

    fenetre.mainloop()

# Appel de la fonction principale
main()