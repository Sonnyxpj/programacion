import	os
import math

from numpy import rint

# Vectores de puntos 
# Hecho por Benjamín Garrido
# 05/01/2022

def limpia_pantalla(): #limpiar consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def leer_archivo(): #leer txt
    dt = open("entrada.txt")
    return dt
     
def almacenar_datos(dt): #Extrae datos para almacenarlo 
    lista = []
    for elemt in dt:
        lista.append(elemt.rstrip().split(","))
    
    return lista

def dimension(lista): #Separa las coordenadas por dimensiones 
    
    tipo2 = []
    tipo3 = []
    tipo4 = []
    tipo5 = []
    for elemt in range(0,len(lista)):
        if len(lista[elemt]) == 2:
            tipo2.append(lista[elemt])
        if len(lista[elemt]) == 3:
            tipo3.append(lista[elemt])
        if len(lista[elemt]) == 4:
            tipo4.append(lista[elemt])    
        if len(lista[elemt]) == 5:
            tipo5.append(lista[elemt])   

    
    return tipo2, tipo3, tipo4, tipo5

def depurador_lista2d(coordenadas):
    
    eje_x = []
    eje_y = []
    for x in coordenadas[0]: 
        eje_x.append(x[0])
            
    for y in coordenadas[0]:
        eje_y.append(y[1])
        

    return eje_x, eje_y

def depurador_lista3d(coordenadas):
    eje_x = []
    eje_y = []
    eje_z = []
    for x in coordenadas[1]:
        eje_x.append(x[0])
    for y in coordenadas[1]:
        eje_y.append(y[1])
    for z in coordenadas[1]:
        eje_z.append(z[2])

    return eje_x, eje_y, eje_z
    
def depurador_lista4d(coordenadas):
    eje_x = []
    eje_y = []
    eje_z = []
    eje_w = []
    for x in coordenadas[2]:
        eje_x.append(x[0])
    for y in coordenadas[2]:
        eje_y.append(y[1])
    for z in coordenadas[2]:
        eje_z.append(z[2])
    for w in coordenadas[2]:
        eje_w.append(w[3])


    return eje_x, eje_y, eje_z, eje_w

def depurador_lista5d(coordenadas):
    eje_x = []
    eje_y = []
    eje_z = []
    eje_w = []
    eje_t = []
    for x in coordenadas[3]:
        eje_x.append(x[0])
    for y in coordenadas[3]:
        eje_y.append(y[1])
    for z in coordenadas[3]:
        eje_z.append(x[2])
    for w in coordenadas[3]:
        eje_w.append(x[3])
    for t in coordenadas[3]:
        eje_t.append(t[4])

    return eje_x, eje_y, eje_z, eje_w, eje_t

def distancia_2d(valores2d):
    x = valores2d[0]
    y = valores2d[1]
    resultados = []

    i = 0
    while i < len(x)-1:
        x1 = x[i]
        y1 = y[i]
        j = i + 1

        while j < len(x):
            dist = 0
            x2 = x[j]
            y2 = y[j]

            dist = round(math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2),2)
            resultados.append(dist)
            j += 1
        i += 1
    if len(resultados) == 0:
        resultados.append(0)
    return resultados

def distancia_3d(valores3d):
    x = valores3d[0]
    y = valores3d[1]
    z = valores3d[2]
    resultados = []

    i = 0
    while i < len(x)-1:
        x1 = x[i]
        y1 = y[i]
        z1 = z[i]
        j = i + 1

        while j < len(x):
            dist = 0
            x2 = x[j]
            y2 = y[j]
            z2 = z[j]

            dist = round(math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2+(int(z2)-int(z1))**2),2)
            resultados.append(dist)
            j += 1
        i += 1
    if len(resultados) == 0:
        resultados.append(0)
    return resultados

def distancia_4d(valores4d):
    x = valores4d[0]
    y = valores4d[1]
    z = valores4d[2]
    w = valores4d[3]
    resultados = []

    i = 0
    while i < len(x)-1:
        x1 = x[i]
        y1 = y[i]
        z1 = z[i]
        w1 = w[i]
        j = i + 1

        while j < len(x):
            dist = 0
            x2 = x[j]
            y2 = y[j]
            z2 = z[j]
            w2 = w[j]

            dist = round(math.sqrt((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2 + (int(z2)-int(z1))**2 + (int(w2)-int(w1))**2),2)
            resultados.append(dist)
            j += 1
        i += 1
    if len(resultados) == 0:
        resultados.append(0)
    return resultados

def distancia_5d(valores5d):
    x = valores5d[0]
    y = valores5d[1]
    z = valores5d[2]
    w = valores5d[3]
    t = valores5d[4]
    resultados = []

    i = 0
    while i < len(x)-1:
        x1 = x[i]
        y1 = y[i]
        z1 = y[i]
        w1 = w[i]
        t1 = t[i]
        j = i + 1

        while j < len(x):
            dist = 0
            x2 = x[j]
            y2 = y[j]
            z2 = z[j]
            w2 = w[j]
            t2 = t[j]

            dist = round(math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2+(int(z2)-int(z1))**2+(int(w2)-int(w1))**2+(int(t2)-int(t1))**2),2)
            resultados.append(dist)
            j += 1
        i += 1
    if len(resultados) == 0:
        resultados.append(0)

    return resultados    

def menor_res2d(resultados2d):
    minimo = min(resultados2d)
    return minimo
    
def menor_res3d(resultados3d):
    minimo = min(resultados3d)
    return minimo

def menor_res4d(resultados4d):
    minimo = min(resultados4d)
    return minimo

def menor_res5d(resultados5d):
    minimo = min(resultados5d)
    return minimo

if __name__ == "__main__":
    limpia_pantalla()
    datos = leer_archivo()
    numero = input("Ingrese el numero del caso a realizar:")
    lista = almacenar_datos(datos)
    coordenadas = dimension(lista)
    valores2d = depurador_lista2d(coordenadas)
    valores3d = depurador_lista3d(coordenadas)
    valores4d = depurador_lista4d(coordenadas)
    valores5d = depurador_lista5d(coordenadas)
    resultados2d = distancia_2d(valores2d)
    resultados3d = distancia_3d(valores3d)
    resultados4d = distancia_4d(valores4d)
    resultados5d = distancia_5d(valores5d)
    caso1_2d = menor_res2d(resultados2d)
    caso1_3d = menor_res3d(resultados3d)
    caso1_4d = menor_res4d(resultados4d)
    caso1_5d = menor_res5d(resultados5d)
    #print(depurador_lista2d(coordenadas))
    while numero == "1":
        print("El menor valor en 2 dimensiones es:",caso1_2d)
        print("El menor valor en 3 dimensiones es:",caso1_3d)
        print("El menor valor en 4 dimensiones es:",caso1_4d)
        print("El menor valor de 5 dimensiones es:",caso1_5d)
        numero = 10
    

    

    
    
    