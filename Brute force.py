def force_brute():
    code_secret = "579"
    tentative = 0
    print("Debut de l'attack par force brute")
    for i in range(1000):
        nombre = str(i)
        if len(nombre) == 1:
            nombre = "00" + nombre
        elif len(nombre) == 2:
            nombre = "0" + nombre
        print(nombre)
        tentative += 1
        if nombre == code_secret:
            print("le nombre de tentative est " + str(tentative) + ". Le code secret est " + str(code_secret))
            break
        
        
    return nombre
        
        
val = force_brute()
print(val)