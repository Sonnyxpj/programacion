# -*- coding: utf-8 -*-
from cgi import print_arguments
import os


def clear(): #Limpia la consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
def leer():
    ent = open("entrada.txt")
  
    lista = []
    for elem in ent:
        #ent = ent.read()
        lista.append(elem.strip().splitlines())    

    prueba = []
    for x in lista:
        #prueba.append(x)
        
        print(x)    
    #print(prueba)

    return prueba
    
def procesa(palabras):

        
    pass
    

if __name__ == "__main__":
    clear()
    palabras = leer()
    procesa(palabras)