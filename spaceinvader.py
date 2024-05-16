import pgzrun
import tkinter as tk




WIDTH = 800
HEIGHT = 600

class SpaceInvader:

    # Variables pour la saisie du nom du joueur
    partie_commence = False # Indice : utilisez cette variable pour savoir quand un nom valide a été saisie et quand on peut enfin instancier et déplacer les objets du jeu.
    nom_joueur = ""
    varNom = None
    formulaire = None

    # Ajoutez d'autres variables pertinentes ici :
    



    # Une partie du formulaire est fournie pour vous aider.
    def saisir_joeur(self):

        self.fenetre = tk.Tk()
        self.fenetre.title("Space Invader")

        self.varNom = tk.StringVar()

        # Ajoutez un libellé (label) ici :



        txtNom = tk.Entry(self.fenetre, textvariable=self.varNom, width=40)
        txtNom.pack()

        btnOk = tk.Button(self.fenetre, text="Ok", command=self.confirmer_nom)
        btnOk.pack()

        self.fenetre.mainloop()


    # Méthode qui reçoit le retour du bouton pour confirmer la saisie du mom du joueur.
    # C'est à partir d'ici qu'on peut commencer à instancier les objets et activer leur déplacement.
    # Indice : pour fermer une fenêtre : laFenetreOuLeFormulaire.destroy()
    def confirmer_nom(self):
        pass





    def dessiner(self, ecran):
        pass


    def mettre_a_jour(self, clavier):
        pass
        

        



# Initialisation du jeu
jeu = SpaceInvader()
jeu.saisir_joeur()

def draw():
    jeu.dessiner(screen)

def update():
    jeu.mettre_a_jour(keyboard)

pgzrun.go()