#Suma de pares recursivo
#Benjamín Garrido

def sumaParRecu(ent, suma, ini):
    if ini == ent*2:
        return suma
    else:
        mod = ini%2
        if (mod == 0):

            suma = suma + ini
            return sumaParRecu(ent, suma, ini + 1)

        else: 
            return sumaParRecu(ent, suma, ini + 1)



if __name__ == "__main__":
    ent = int(input("Ingrese una valor natural: "))
    suma = 0
    ini = 0
    total = sumaParRecu(ent, suma, ini)

    print("Suma de pares recursivo:", total)