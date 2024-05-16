import tkinter as tk
import csv


class Scoreboard:

    liste_score = []
    fenetre = None
    listbox = None


    # Méthode pour ouvrir le formulaire et enregistrer le score du joueur.
    def ouvrir(self, nom_joueur, pointage) -> None:

        # Sauvegarde du score :




        self.fenetre = tk.Tk()
        self.fenetre.title("Scoreboard")

        self.listbox = tk.Listbox(self.fenetre, selectmode=tk.SINGLE)
        self.listbox.pack()

        # Ajout des scores du fichier CSV dans la listbox :

        


        self.fenetre.mainloop()
