def tamaño(img):
    autor = img.readline().rstrip("\n")
    
    texto = []
    linea = img.readline().rstrip("\n")
    if linea[0] == "#":
        texto.append(linea)
        linea = img.readline().rstrip("\n")
    
    tam = linea.split(" ")

    ancho = int(tam[0])
    largo = int(tam[1])
    
    return tam,ancho,largo


def grises(img):
    rango = int(img.readline().rstrip())

    print(rango)

    pixels = []

    for linea in img:
        linea = linea.rstrip('\n')
        l = linea.split(' ')
        for pixel in l:
            if pixel != '':
                pixels.append(int(pixel))
    #print(pixels)
    

    if entrada == str(1):
        
        binaria = []
        for pixel in pixels:
            aclarar = pixel + 160
            if aclarar > 255: 
                aclarar = 255
            binaria.append((aclarar))
    

    if entrada == str(2):
        binaria = []
        for pixel in pixels:
            oscurecer = pixel - 50
            if oscurecer < 0:
                oscurecer = 0
                binaria.append((oscurecer))
    print(binaria)
    return rango

def crear(tam,grises,binaria):
    sal = open("auto2.pgm","w")
    sal.write(P2+"\n")
    sal.write("#Hecho por Sonny")
    sal.write(ancho+ " "+alto)
    sal.write(rango+"\n")
    for i in binaria:
        sal.write(i+"\n")




if __name__ == "__main__":
    img = open("auto.pgm","r")
    entrada = input("ingrese un valor\n")
    tamaño(img)
    grises(img)
    


    img.close()