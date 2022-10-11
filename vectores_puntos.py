import	os
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

def depurador_lista2d(coordenadas):
    eje_x = []
    eje_y = []
    for x in coordenadas[0]: 
        eje_x.append(x[0])
    for y in coordenadas[0]:
        eje_y.append(y[1])
    
    #print(eje_x)
    #print()
    #print(eje_y)
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
    
    print(eje_x,"\n",eje_y,"\n",eje_z)
    
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
    
    print(eje_x,"\n",eje_y,"\n",eje_z,"\n",eje_w)

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
    
    print(eje_x)
    print()
    print(eje_y)
    print()
    print(eje_z)
    print()
    print(eje_w)
    print()
    print(eje_t)

def distancia_2d(valores2d):
    x = valores2d[0]
    y = valores2d[1]
    #print(x[1], x[0])
    #print(y[1], y [0])
    valor = math.sqrt((int(x[1])-int(x[0]))**2+(int(y[1])-int(y[0]))**2)
    
    
    #q = 1
    #while q <=len(x):
    #    valor = math.sqrt((int(x[1])-int(x[0]))**2+(int(y[1])-int(y[0]))**2)
    #    q += 1

    

    
    
    #print(x[0],x[1])
    print(valor)
    

if __name__ == "__main__":
    limpia_pantalla()
    datos = leer_archivo()
    lista = almacenar_datos(datos)
    coordenadas = dimension(lista)
    valores2d = depurador_lista2d(coordenadas)
    distancia_2d(valores2d)
    #prueba = np.sqrt((2-2)**2+(2-3)**2)
    

    

    
    
    