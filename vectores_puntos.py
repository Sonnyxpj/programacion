import	os


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

def depurador_lista2d(tipo2):
    for x in tipo2[0]: 
        print(x)



#def separador_puntos(tipo2): #Almacena en partes las coordenadas x e y
#    eje_x = []
#    eje_y = []
#    tam = len(tipo2[0])
#    i = 1
#    while i <= 5:
#        
#        eje_x.append(tipo2[0][0])
#        i +=1
#    print(tam)       
#    return eje_x, eje_y

if __name__ == "__main__":
    limpia_pantalla()
    datos = leer_archivo()
    lista = almacenar_datos(datos)
    tipo2 = dimension(lista)
    #separador_puntos(tipo2)
    depurador_lista(tipo2)
    #print(separador_puntos(tipo2)[0])

    

    
    
    