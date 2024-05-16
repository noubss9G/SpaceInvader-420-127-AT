from pgzero.builtins import Actor, animate, keyboard

class Objet_Mobile:

    acteur = None
    direction = 0
    vitesse = 3

    def __init__(self) -> None:
        self.acteur = Actor()
        