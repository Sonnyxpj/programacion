#Matias Thetower matias.latorre.01@alu.ucm.cl
#Joaquin Whistle joaquin.silva.01@alu.ucm.cl
#Seccion 3

import random


def probabilidades_ruleta():
    i = 0 
    ruleta = []
    while i < 3:
        valor = random.randint(0,99)
        ruleta.append(valor)
        i += 1   

    return ruleta

def figura_probabilidad(ruleta1):
    lista = []
    for elem in ruleta1:
        if 0 <= elem <=1:
            lista.append(7)
        elif 2 <= elem <= 4:
            lista.append(6)
        elif 5 <= elem <= 9:
            lista.append(5)
        elif 10 <= elem <= 19:
            lista.append(4)
        elif 20 <= elem <= 29:
            lista.append(3)
        elif 30 <= elem <= 49:
            lista.append(2)
        elif 50 <= elem <= 69:
            lista.append(1)
        else:
            lista.append(0)
    print(lista[0],"-",lista[1],"-",lista[2])
    return lista



def configuracion(apuesta, ruleta_real):
    ganancia= 0
    if [7,7,7] == ruleta_real:
        ganancia = apuesta*1000
    elif [6,6,6] == ruleta_real:
        ganancia = apuesta*250
    elif [5,5,5] == ruleta_real:
        ganancia = apuesta*150
    elif ([4,4,4] == ruleta_real)or ([3,3,3] == ruleta_real):
        ganancia = apuesta*50
    elif ([2,2,2] == ruleta_real) or ([1,1,1] == ruleta_real):
        ganancia = apuesta*30
    elif [0,0,0] == ruleta_real:
        ganancia = apuesta*20
    elif (ruleta_real.count("5") == 2) or (ruleta_real.count("6") == 2) or (ruleta_real.count("7") == 2):
        ganancia = apuesta*10
    elif (ruleta_real.count("7") == 1):
        ganancia = apuesta*5
    elif (ruleta_real.count("5") == 1) or (ruleta_real.count("6")):
        ganancia = apuesta*2
    else:
        print("QUEDASTE POBRE")
    
    return ganancia
    

if __name__ == '__main__':
    z = 0
    while z == 0:
        saldo = int(input('Ingresa saldo disponible: $'))
        if saldo < 100:
            print("Ingrese nuevamente el saldo que desea ingresa nuevamen")
        
        apuesta = int(input('Cuanto desea apostar: $'))
        
        if (apuesta == 100) or (apuesta == 500) or (apuesta == 1000):
            print("Apuesta ingresada: $"+str(apuesta))
            ruleta1 = probabilidades_ruleta()
            ruleta_real = figura_probabilidad(ruleta1)
            resultado = configuracion(apuesta, ruleta_real) 
            Saldo_final =  saldo - apuesta + resultado
            z = 1
        else:
            print('valor no valido, vuelva a escribir')
    