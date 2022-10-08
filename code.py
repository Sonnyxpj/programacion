def promedio(lista):
    num = []
    for x in lista:
        x.insert(lista[1],num)
    print(num)

if __name__ =="__main__":
    datos = open("acciones.txt","r")
    lista = []
    for linea in datos:
        lista.append(linea.rstrip())
    print(lista)
    promedio(datos)
    datos.close()