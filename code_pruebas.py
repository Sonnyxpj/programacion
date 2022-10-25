import random as rd
import os

def clear(): #limpia la consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def prueba():
    i = 0
    figuras = ["0", "1", "2", "3", "4", "5", "6", "7"]
    while i <= 5:
        resultado = rd.choices(figuras, [30, 20, 20, 10, 10, 5, 3, 2], k=3)
        print(resultado)
        i += 1
    return resultado

if __name__ == "__main__":
    clear()
    prueba()
    print(prueba())