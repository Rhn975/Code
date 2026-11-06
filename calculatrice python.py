def main():
    while (1 == 1):
        nombre = demande_utilisateur()
        calcul = demande_choix(nombre)
        print(calcul)
        continuation()
       
def demande_utilisateur():
    print("1 : addition")
    print("2 : soustraction")
    print("3 : multiplication")
    print("4 : division")
    reponse =  input("Quelle calcul voulez vous faire ? ")
    while ((reponse != "+")and(reponse != "-")and(reponse != "*")and(reponse != "/")):
            print("Le caractere mis n'est pas correct(+,-,*,/)")
            reponse = input("Quelle calcul voulez vous faire ? ")
    return reponse

    


def demande_choix(nombre):
    while True:
        try:
            a = int(input("Quelle est votre chiffre ? : "))
            break
        except ValueError:
            print("Veullier entrer un vrai nombre")
    while True:
        try:
            b = int(input("Quelle est votre second chiffre ? : "))
            break
        except ValueError:
            print("Veullier entrer un vrai nombre")

    if (nombre == "+"):
        return a + b            
    elif (nombre == "-"):
        return a - b
    elif (nombre == "*"):
        return a * b           
    elif(nombre == "/" and (a == 0 or b == 0)):
        print("Erreur : on ne peut diviser par zero")
        a = int(input("Quelle est votre chiffre ? : "))
        b = int((input("Quelle est votre second chiffre ? : ")))
    elif (nombre == "/"):
        return a / b
       

def continuation():
    reponse = input("Voulez vous faire un autre calcul (oui/non) ? : ")
    if reponse == "non":
        return exit()
    while reponse != "oui":
        print("Veullier mettre dans le bon format(oui/non)")
        reponse = input("Voulez vous faire un autre calcul (oui/non) ? : ")

main()
