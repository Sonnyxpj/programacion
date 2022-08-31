cod=1
while cod==1:
        time.sleep(1)
        ent = int(input("Qué desea calcular? \nSuma: 1 \nResta: 2 \nMultiplicacion: 3 \nDivisión: 4 \nPotencia: 5 \nSeno: 6 \nCoseno: 7 \nSalir: 8 \n> "))
        if ent==1:
            var1=int(input("Introduzca el primer valor: \n>"))
            var2=int(input("Introduzca el segundo valor: \n>"))
            suma=var1+var2
            print("El resultado es:",suma)
            cod=1
            prin
        if ent==2:
            var1=int(input("Introduzca el primer valor: \n>"))
            var2=int(input("Introduzca el segundo valor: \n>"))
            rest=var1-var2
            print("El resultado es:",rest)
            cod=1
        if ent==3:
            var1=int(input("Introduzca el primer valor: \n>"))
            var2=int(input("Introduzca el segundo valor: \n>"))
            multi=var1*var2
            print("El resultado es:",multi)
            cod=1
        if ent==4:
            var1=int(input("Introduzca el dividendo: \n>"))
            var2=int(input("Introduzca el divisor: \n>"))
            divi=var1/var2
            print("El resultado es:",divi)
        if ent==5:
            var1=int(input("Introduzca el primer valor: \n>"))
            var2=int(input("Introduzca el segundo valor: \n>"))
            ele=var1**var2
            print("El resultado es:",ele)
        if ent==6:
            var1=int(input("Introduzca un valor en grados: \n>"))
            sin=math.radians(var1)
            math.sin(sin)
            print("El resultado es:",sin)
        if ent==7:
            var1=int(input("Introduzca un valor en grados: \n>"))
            cos=math.radians(var1)
            math.sin(cos)
            print("El resultado es:",cos)
        if ent==8:
            var1=int(input("Saliendo..."))
            exit()
