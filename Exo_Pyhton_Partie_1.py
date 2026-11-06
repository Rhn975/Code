from math import *
from random import *

#Exo 29

def carre_parfait(n):
    valeur = sqrt(n)
    if valeur % 1 == 0:
        return True
    return False

val = carre_parfait(49)
print(val)

#Exo 29 partie 2

def carre_parfait(n):
    valeur = sqrt(n)
    if valeur % 1 == 0:
        return True
    return False

def somme_carrés(n):
    somme = 0
    for i in range(1, n + 1):
        if carre_parfait(i):
            somme += i
    return somme

val = somme_carrés(100)
print(val)

#Exo 30

def pile_face():
    hasard = randint(1,2)
    if hasard == 1:
        return "pile"
    return "face"

val = pile_face()
print(val)

#Exo 31

def lance_de():
    hasard = randint(1,6)
    return hasard

val = lance_de()
print(val)

#Exo 32

def tirage_monopoly():
    resultat = 0
    for i in range(2):
        valeur = randint(1,6)
        resultat += valeur
    return resultat

val = tirage_monopoly()
print(val)

#Exo 33

def lance_de():
    hasard = randint(1,6)
    return hasard

def simulation(n):
    compteur = 0
    for i in range(n):
        if lance_de() == 6:
            compteur = compteur + 1
    return compteur / n

val = simulation(10)
print(val)

# Exo 34

def lance_de():
    hasard = randint(1,6)
    return hasard

def obtenir_six():
    compteur = 0
    resultat = 0
    while resultat != 6:
        resultat = lance_de()
        compteur = compteur + 1
    return compteur

val = obtenir_six()
print(val)

# Exo 35

def est_pair(nombre):
    return nombre % 2 == 0

def syracuse(n,a):
    u = a
    for _ in range(n):
        if est_pair(u):
            u = u / 2
        else:
            u = 3*u + 1
    return u

def vol(a):
    valeur = [a]
    u = a
    n = 0
    while u != 1:
        n += 1
        u = syracuse(n,a)
        valeur.append(u)
    return valeur

def temp_vol(a):
    return len(vol(a)) - 1

def altitude(a):
    return max(vol(a))

val = altitude(15)
print(val)
    

