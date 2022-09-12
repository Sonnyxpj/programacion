def binariza(lista,pixeles):
    for pixel in pixeles:
        if pixel > promedio:
            pixel = 255
            lista.append(pixel)

        elif pixel > 80 and pixel < promedio:

            pixel = 100
            lista.append(pixel)

        else:
            pixel = 0
            lista.append(pixel)

    return lista

def aclarador(lista, pixeles,x):
    for pixel in pixeles:

        aclara = pixel + int(x)
        if aclara > 255:
            aclara = 255
        lista.append(aclara)

    return lista

def oscuro(lista, pixeles,x):
    for pixel in pixeles:

        oscurece = pixel - int(x)

        if oscurece < 0:
            oscurece = 0

        lista.append(oscurece)

    return lista

def negativo(lista,pixeles):
    for pixel in pixeles:

        pixel = int(umbral)-pixel
        lista.append(pixel)

    return lista

def escritura(tam, umbral, lista):
    salida = open("auto2.pgm", "w")
    salida.write(formato + "\n")
    salida.write("#Hecho por sonny" + "\n")
    salida.write(tam[0] + " " + tam[1] + "\n")
    salida.write(umbral + "\n")
    for i in lista:
        salida.write(str(i) + "\n")




if __name__ == "__main__":
    img = open("auto.pgm", "r")
    formato = img.readline().rstrip()

    comentarios = []    
    linea = img.readline().rstrip()

    while linea[0] == "#":
        comentarios.append(linea)
        linea = img.readline().rstrip()

    tam = linea.split(" ") #largo x ancho
    umbral = img.readline().rstrip("\n")

    pixeles = []
    for linea in img:
        linea = linea.rstrip()
        pixeles.append(int(linea))

    lista = []

    promedio = sum(pixeles)/len(pixeles)

    z = input("Ingrese un valor \n1) Para aclarar la imagen \n2) Para oscurecer la imagen \n3) Para obtener el negativo de la imagen \n")
    if z == "1":
        x = input("ingrse numero que desea aclarar image\n")
        aclarador(lista, pixeles,x)
        escritura(tam, umbral, lista)
    elif z == "2":
        x = input("Ingrese numero que desea oscurecer la imagen \n")
        oscuro(lista, pixeles, x)
        escritura(tam, umbral, lista)
    elif z == "3":
        negativo(lista, pixeles,)
        escritura(tam, umbral, lista)
    elif z == "0":
        binariza(lista, pixeles)
        escritura(tam, umbral, lista)