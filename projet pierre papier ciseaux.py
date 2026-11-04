import random

def main():
    print("Jouer contre le robot en 5 manche : ")
    choix_robot = choi_robot()
    nombre = user()
    affrontement(nombre,choix_robot)
    
def choi_robot():
    choix_robot = random.randint(1,3)
    return choix_robot
    
    
def user():
    nombre = 0
 
    while nombre == 0:
        choix = input("Que vouler vous choisir pierre,papier,ciseaux ? : ")
        if choix == "Pierre" or choix == "pierre" or choix == "PIERRE":
            nombre = 1
        elif choix == "papier" or choix == "Papier" or choix == "PAPIER":
            nombre = 2
        elif choix == "ciseaux" or choix == "CISEAUX" or choix == "Ciseaux":
            nombre = 3
        else:
            print("Veullier mettre pierre/papier ou ciseaux ")
            choix = input("Que vouler vous choisir pierre,papier,ciseaux ? : ")
    return nombre

def affrontement(nombre,choix_robot):
    manche = 1
    point_joueur = 0
    point_robot = 0
    while manche != 5:
        print("Manche ",manche)
        manche += 1
        if nombre == choix_robot:
            print("Vous avez jouer le meme coup que le robot egalité")
        if nombre == 1 and choix_robot == 2:
            point_robot += 1
            print("Le robot a jouer papier ")
            print("Le robot gagne la manche")
        elif nombre == 2 and choix_robot == 1:
            print("Le robot a jouer Pierre ")
            point_joueur += 1
            print("Le joueur gagne la manche")
        elif nombre == 1 and choix_robot == 3:
            print("Le robot a jouer ciseaux ")
            point_joueur += 1
            print("Le joueur gagne la manche")
        elif nombre == 3 and choix_robot == 1:
            print("Le robot a jouer Pierre ")
            point_robot += 1
            print("Le robot gagne la manche")
        elif nombre == 3 and choix_robot == 2:
            print("Le robot a jouer papier ")
            point_joueur += 1
            print("Le joueur gagne la manche")
        elif nombre == 2 and choix_robot == 3:
            print("Le robot a jouer ciseaux ")
            point_robot += 1
            print("Le robot gagne la manche")
        nombre = user()
        choix_robot = choi_robot()
    if point_robot == point_joueur:
        print("Math Nul")
    elif point_robot > point_joueur:
        print("Le robot a gagner plus de partie (Looser)",point_robot,point_joueur)
    elif point_robot < point_joueur:
        print("vous avez gagner plus de partie que le robot",point_joueur,point_robot)
            
main()  
    