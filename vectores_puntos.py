import os
import math

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

def depurador_lista2d(coordenadas): #separa todas las coordenadas X e Y en listas por separado en plano de 2 dimensiones 
    eje_x = [] #coordenada x
    eje_y = [] #coordenada Y
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
    
 
    return eje_x, eje_y, eje_y, eje_w

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

            #p1 = (int(x2)-int(x1))**2
            #p2 = (int(y2)-int(y1))**2
            #dist = math.sqrt(p1+p2)
            #redondeo = round(dist,2)
            #print(p1,"+",p2,"=",redondeo)

            dist = math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2)
            redondeo = round(dist,2)
            resultados.append(redondeo)
            j += 1
        i += 1

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

            dist = math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2+(int(z2)-int(z1))**2)
            redondeo = round(dist,2)
            resultados.append(redondeo)
            j += 1
        i += 1
    
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
            w2 = z[j]

            dist = math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2+(int(z2)-int(z1))**2+(int(w2)-int(w1))**2)
            redondeo = round(dist,2)
            resultados.append(redondeo)
            j += 1
        i += 1
        
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
        z1 = z[i]
        w1 = w[i]
        t1 = t[i]
        j = i + 1

        while j < len(x):
            dist = 0
            x2 = x[j]
            y2 = y[j]
            z2 = z[j]
            w2 = z[j]
            t2 = t[j]
            dist = math.sqrt((int(x2)-int(x1))**2+(int(y2)-int(y1))**2+(int(z2)-int(z1))**2+(int(w2)-int(w1))**2+(int(t2)-int(t1))**2)
            redondeo = round(dist,2)
            resultados.append(redondeo)
            j += 1
        i += 1
        
    return resultados

def menor_dis_2d(resultados2d): #Calcula el menor valor en el plano de 2 dimensiones 
    
    minimo = min(resultados2d)
    return minimo
    

def menor_dis_3d(resultados3d): #Calcula el menor valor en el plano de 3 dimensiones 
    
    minimo = min(resultados3d)
    return minimo    

def menor_dis_4d(resultados4d): #Calcula el menor valor en el plano de 5 dimensiones
    minimo = min(resultados4d)
    return minimo
    
def menor_dis_5d(resultados5d):

    minimo = min(resultados5d)
    return minimo
    
    
if __name__ == "__main__":
    limpia_pantalla()
    entrada = input("Ingrese el numero del caso que quiere ejecutar:")
    datos = leer_archivo()
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
    mini2d = menor_dis_2d(resultados2d)
    mini3d = menor_dis_3d(resultados3d)
    mini4d = menor_dis_4d(resultados4d)
    miin5d = menor_dis_5d(resultados5d)
    while entrada == "1":
        print("Menor distancia euclidiana en 2 dimenciones es:",mini2d)
        print("Menor distancia euclidiana en 3 dimenciones es:",mini3d)
        print("Menor distancia euclidiana en 4 dimenciones es:",mini4d)
        print("Menor distancia euclidiana en 5 dimenciones es:",miin5d)
        entrada = 0