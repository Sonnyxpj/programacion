#Mateo Antonio Gonzalez Lisboa; mateo.gonzalez@alu.ucm.cl; 21271756-8
#Benjamin Ignacio Garrido Jara; benjamin.garrido.02@alu.ucm.cl; 21514798-3
#Seccion 3
#Fecha: 18-10-2022
import random
import os
import time

def clear(): #limpia la consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def tragamonedas(saldo, separador): #Mantiene en ejecucion el juego
    detener = False

    while detener != True: 
        print(separador.center(50,"=") + "\n")
        apostado = apostar(saldo)
        time.sleep(0.5)
        saldo = saldo - apostado
        figuras_obtenidas = gira_rueda()
        ganancias = combinaciones(figuras_obtenidas, apostado)

        if ganancias == 0:
            print("Perdiste $" + str(apostado))
        else:
            print("Ganaste $" + str(ganancias))
            saldo = saldo + ganancias
        
        detener = cond_para_detener(saldo)#Detendra el programa si cumple las condiciones

def monto_inicial(separador):#Solicita dinero para jugar
    print(separador.center(50,"=") + "\n")
    suficiente = False

    while suficiente != True:
        print("La cantidad minima a depositar es de $100")
        saldo_inicial = input("Deposite monto inicial: $")

        comprobar = verifica_dinero(saldo_inicial)
        if comprobar == True:
            if int(saldo_inicial) < 100:
                print("¡Valor mal ingresado! \n")

            else:
                suficiente == True
                return int(saldo_inicial) #Solo aceptara saldo mayor o igual a 100$

def apostar(saldo): 
    apostando = True

    while apostando == True: 
        print("Tu saldo actual: $" + str(saldo))
        print("¿Cuanto quiere apostar?")
        print("$100, $500 o $1000 \n")
        apostar = input("Quiero apostar ---> $")
        comprobar = verifica_dinero(apostar)

        if comprobar == True:
            apostar = int(apostar)

            if apostar == 100 or apostar == 500 or apostar == 1000:#Verifica se apuesten los valores correctos
                if saldo < apostar:
                    print("No tiene dinero suficiente para esa apuesta... \n")
                    time.sleep(0.5)
                else:
                    print("Esta apostando: $" + str(apostar))
                    time.sleep(0.5)
                    return apostar
            else:
                print()
                print("¡Debe apostar los valores que aparecen en pantalla! \n")
                time.sleep(0.5)

def verifica_dinero(dinero): #Solo aceptara valores numericos positivos
        comprueba_numero = dinero.isdigit()
        print()
        
        if comprueba_numero == True:
            return comprueba_numero
        else:
            print("¡Valor mal ingresado! \n")

def gira_rueda(): 
    figuras = ["0", "1", "2", "3", "4", "5", "6", "7"]
    resultado = random.choices(figuras, [30, 20, 20, 10, 10, 5, 3, 2], k=3) #figuras asociadas a su probabilidad
    print(resultado[0],"-",resultado[1],"-",resultado[2]) 
    
    return resultado

def combinaciones(figuras, apostar): #Verifica combinaciones ganadoras y entrega recompensas
    recompensa = 0

    if figuras.count("7") == 3:
        recompensa = apostar*1000
    elif figuras.count("6") == 3:
        recompensa = apostar*250
    elif figuras.count("5") == 3:
        recompensa = apostar*150
    elif figuras.count("4") == 3:
        recompensa = apostar*50
    elif figuras.count("3") == 3:
        recompensa = apostar*50
    elif figuras.count("2") == 3:
        recompensa = apostar*30
    elif figuras.count("1") == 3:
        recompensa = apostar*30
    elif figuras.count("0") == 3:
        recompensa = apostar*20
    elif figuras.count("5") == 2 or figuras.count("6") == 2 or figuras.count("7") == 2:
        recompensa = apostar*10
    elif figuras.count("7") == 1:
        recompensa = apostar*5
    elif figuras.count("5") == 1 or figuras.count("6") == 1:
        recompensa = apostar*2
    
    return recompensa

def cond_para_detener(saldo):
    print()
    if saldo < 100: #Para jugar se debe tener minimo $100
        print("Tu saldo actual: $" + str(saldo))
        print("Ya no tiene suficiente saldo, cerrando el programa... \n")
        return True
            
    else:
        decidido = False

        while decidido != True: #El jugador tomara la decision
            print("Tu saldo actual: $" + str(saldo))
            continuar = input("¿Quieres continuar? (Si o No): ")
            continuar = continuar.lower()

            if continuar == "si":
                time.sleep(0.5)
                print()
                return False

            if continuar == "no":
                print("Se retira con el saldo total de ---> $" + str(saldo) + "\n")
                return True

if __name__ == "__main__":
    clear()
    saldo = monto_inicial("Tragamonedas")
    tragamonedas(saldo, "Tragamonedas")