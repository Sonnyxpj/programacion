import random
lista = ["0","1","2","3","4","5","6","7"]
a = random.choices(lista,[30,20,20,10,10,5,3,2],k=3)

print(a[0],"-",a[1],"-",a[2])
