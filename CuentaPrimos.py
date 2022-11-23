#Programa creado por Nelson Andrés Araya Rojas en Python 3 año 2019.
#Modificado por Philip para próximas generaciones

from tkinter import *
from tkinter import messagebox
from math import *


# Ventana de información del boton 'Acerca De'.
def AcercaDe(ventana):
	mensaje2 = "Cuenta Números Primos " + "\n" + "Programa creado por Nelson Andrés Araya Rojas 2019"+ "\n" + "Modificado por Philip para próximas generaciones"  
	messagebox.showinfo(ventana,mensaje2)

# Ventana de información del boton 'Ayuda'.
def Ayuda(ventana):
	mensaje3 = "Cuenta Números Primos" + "\n" + "Introducir un número en el rectángulo correspondiente (recuerda que el número debe estar entre '3 y 10000', luego presionar el botón 'Siguiente Número' y el programa dirá si el número ingresado es primo o no; con la condición de que si es primo lo sumara. Al presionar el botón 'Finalizar', se entregará la cantidad total de números ingresados, junto con la suma de los primos y la cantidad de números no primos ingresados."
	messagebox.showinfo(ventana,mensaje3)

#Función que verifica si el numero ingresado es primo o no, junto con esto almacena en listas separada los primos y los no primos.
def Primos(numeros,primos,noprimos):
	#print (numeros)
	i = 0
	div = 0
	j = 2
	while j < (int(numeros)//2) and div == 0:
		if (int(numeros)%j) == 0 or int(numeros) == 1:
			div = 1
			noprimos.append(str(numeros))
		j = j + 1
	if div == 0:
		primos.append(str(numeros))
	return primos,noprimos

#Función que suma los primos, si la variable de entrada 'Entry' esta vacía iguala está a 0.
def SumaPrimos (numero,Suma):
	a = numero.get() 
	if Suma.get():
		b = Suma.get()
	else:
		b = 0
	suma = int(a) + int(b)
	return Suma.set(suma)

#Función que se encarga de calcular el total gracias al largo de las listas de primos y no primos, además entrega la suma de primos y la cantidad de números no primos.
def Finalizar(noprimos,primos,suma,ventana):
	total = (int(primos)+int(noprimos))
	mensaje =  "Números Ingresados: "+ str(total)+ "\n" + "La suma de los números primos es: " + str(suma)+"\n" + "La cantidad de números no primos fue: " +str(noprimos)
	messagebox.showinfo(ventana,mensaje)

#Función que verifica si el número es válido o no y que se encarga de los 'Checkbutton' cambiando su estado cuando un número es primo y cuando no, además suma los números primos.
def VerificarNumero (numero,ventana,j,a,chk_state,chk_state2,primos,noprimos,Suma):
	if numero.get() and int(numero.get()) > 0 and int(numero.get()) >= 3 and int(numero.get()) <= 10000:
		primos, noprimos = Primos (numero.get(),primos,noprimos)
		if (str(numero.get())) in primos:
			Suma = SumaPrimos (numero,Suma)
			return chk_state.set(True),chk_state2.set(False),Suma
		else:
			return chk_state2.set(True),chk_state.set(False)
	else:
		mensaje =  " " +str("Numero Inválido ")
		messagebox.showinfo(ventana,mensaje)

def veriicar_raiz(numero2, exacta, noexacta):
	valor = int(numero2.get())

	raiz = int(sqrt(valor))
	verifica = raiz ** 2
	if valor == verifica:
		#print("Tiene raiz exacta")
		return exacta.set(True), noexacta(False)
	else: 
		print("No tiene raiz exacta")
		#noexacta = True
		return noexacta.set(True), exacta.set(False)

# Se hace la declaración de las variables a utilizar y se crean los 'botones', 'etiquetas', 'entradas', 'Checkbutton' e 'imagenes' correspondientes.
if __name__ == '__main__':
	j = 0
	a = []
	primos = []
	noprimos = []
	ventana = Tk()
	ventana.title("Cuenta Números Primos")
	ventana.geometry("500x250")

	
	et1 = Label (ventana, text = "Cuenta Números Primos").place(x=120,y=50)
	et2 = Label (ventana, text = "Suma ").place(x=50,y=100)
	et3 = Label (ventana, text = "Número ").place(x=50,y=130)
	Suma = StringVar()
	Suma.set("0")
	numero2 = StringVar ()
	number = Entry (ventana, textvariable = numero2 ).place(x=130,y=130)
	suma = Label (ventana,background = "white" ,textvariable = Suma,width = 17).place(x=130,y=100)
	esprimo = BooleanVar()
	esprimo.set(False)
	noesprimo = BooleanVar()
	noesprimo.set(False)
	exacta = BooleanVar()
	exacta.set(False)
	noexacta = BooleanVar()
	noexacta.set(False)

	si_primo = Checkbutton(ventana, text='Es primo', var=esprimo).place(x=270,y=100)
	si_raiz_exac = Checkbutton(ventana, text = "Raiz exacta", var = exacta).place(x = 340, y = 100)
	no_primo = Checkbutton(ventana, text='No es primo', var=noesprimo).place(x=270,y=130)
	no_raiz_exac = Checkbutton(ventana, text = "No tiene raiz exacta", var = noexacta).place(x = 360, y = 130)
	acercade = Button (ventana,text = "Acerca de ", bg = "#00FF93",command = lambda: AcercaDe(ventana) ).place(x=5,y=5)
	ayuda = Button (ventana,text = "Ayuda ", bg = "#00FF93", command = lambda: Ayuda(ventana)).place(x=80,y=5)
	signum = Button (ventana, text = "Siguiente Número", bg = "#00FF93", command = lambda: VerificarNumero(numero2,ventana,j,a,esprimo,noesprimo,primos,noprimos,Suma) and veriicar_raiz(numero2, exacta, noexacta) ).place(x=50,y=200)
	salir = Button (ventana, text = "Finalizar", bg = "#00FF93", command = lambda: Finalizar(len(noprimos),len(primos),Suma.get(),ventana)).place(x=200,y=200)
	salir2 = Button (ventana, text = "Salir", bg = "#9041FC", command = quit).place(x=300,y=200)
	ventana.mainloop()  
