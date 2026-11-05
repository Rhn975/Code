from random import *
from pathlib import Path

def Autenthification():
    mot_de_passe = "1636"
    nbr_max_tentative = 3
    compteur = 0
    print("Authentification requise")
    while True:
        mot_de_passe_user = input("Quelle est votre mot de passe ? ")
        if mot_de_passe != mot_de_passe_user:
            nbr_max_tentative -= 1
            print("Le mot de passe ne correspond pas. il vous reste " + str(nbr_max_tentative) + " tentative")
            if nbr_max_tentative == 0:
                print("Vous n'avez plus de tentative")
                return
        else:
            break
    if nbr_max_tentative <= 1:
        print("Vous aller recevoir un pin")
        pin = generate_pin()
        get_desktop_path__write_pin_file(pin)
        compteur = 0
        while compteur != 2:
            mot_de_passe_pin = int(input("Quel est le pin qui a ete envoyé ? :"))
            if mot_de_passe_pin == int(pin):
                print("Le pin est bon\nBienvenu")
                return
            else:
                print("Erreur ce n'est pas le bon code pin")
            compteur += 1
        print("Vous ne pouver pas acceder au site")
        detecte_bruteforce()
    else:
        print("Le mot de passe est correcte\nBienvenu")

def generate_pin():
    nombre = ''
    while len(nombre) != 4:
        valeur = randint(0,9) 
        nombre = nombre + str(valeur)
    return nombre



def get_desktop_path__write_pin_file(pin):
    bureau = Path.home() / "OneDrive" / "Bureau"
    fichier = bureau / "mon_pin.txt"
    fichier.write_text(pin)
    print("Fichier crée .Voici le chemin: \n",fichier.resolve)
    
def detecte_bruteforce():
    bureau = Path.home() / "OneDrive" / "Bureau"
    fichier = bureau / "bruteforce_detected.txt"
    fichier.write_text("Une tentative suspecte a été détectée.")
    


Autenthification()