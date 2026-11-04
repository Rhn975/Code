import random


def main():
    nombre = affichage()
    nombre_robot = robot()
    tentative_du_joueur(nombre,nombre_robot)
    
    
    
def affichage():
    print("Tenter de deviner le nombre aleatoire ")
    while True:
        try:
            nombre = int(input("Quelle est votre chiffre : "))
            break
        except ValueError:
            print("Veullier entrer un vrai nombre")
            
    return nombre

def robot():
    nombre_robot = random.randint(1, 100)
    return nombre_robot

def tentative_du_joueur(nombre,nombre_robot):

    compteur = 10
    while nombre != nombre_robot:
        compteur -= 1
        print("Votre nombre n'est pas le bon .Il vous reste ",compteur,"tentative")
        if nombre > nombre_robot:
            print("C'est plus petit")
        else:
            print("C'est plus grand")
        while True:
            try:
                nombre = int(input("Quelle est votre chiffre : "))
                break
            except ValueError:
                print("Veullier entrer un vrai nombre")
                
        if compteur == 0:
            print("Vous n'avez pas trouver meme apres 10 tentative .Le bon nombre a trouvé etait : ",nombre_robot)
            exit()
        
    print("Bravos vous avez trouver le nombre en ",10 - compteur,"tentative(s)")
 
main()
    