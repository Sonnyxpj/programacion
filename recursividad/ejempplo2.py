#potencia de un numero

def potenRecu(base , expo, total):
    if (expo == 0):
        return total
    else: 
        total = total * base
        return potenRecu(base, expo - 1 , total)

if __name__ == "__main__":
    base = int(input("Ingrese el valor de la base:"))
    expo = int(input("Ingrese el valro del expornente: "))
    total = 1
    poRu = potenRecu(base , expo, total)
    print(poRu)