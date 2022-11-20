from tkinter import *

def visor(num):
    global operador
    if num == "DEL":
        if operador == "=":
            pass
        else:
            operador = operador[:-1]
            input_cal.set(operador)
    elif num == "CE":
        operador = ""
        input_cal.set(0)
    else:
        operador = operador + str(num)
        input_cal.set(operador)

def ejecutar():
    global operador
    try:
        opera = str(eval(operador))
        input_cal.set(opera)
    except ZeroDivisionError:
        input_cal.set("Math ERROR")
    except:
        input_cal.set("ERROR")
    operador = ""



root = Tk()
root.geometry("400x200")
root.title("Calculadora")

operador = ""
input_cal = IntVar()
entrada = Entry(root, font = ("arial",12,"bold"), textvariable = input_cal,justify="right").grid(row = 0 , columnspan = 5)

#Botones númericos
b1 = Button(root,  text = "1", command= lambda : visor(1)).grid(row = 1, column = 0, sticky=W+E)
b2 = Button(root, text = "2", command= lambda : visor(2)).grid(row = 1, column = 1, sticky= W+E)
b3 = Button(root, text = "3", command= lambda : visor(3)).grid(row = 1, column = 2, sticky= W+E)
b4 = Button(root, text = "4", command= lambda : visor(4)).grid(row = 2, column = 0, sticky= W+E)
b5 = Button(root, text = "5", command= lambda : visor(5)).grid(row = 2, column = 1, sticky= W+E)
b6 = Button(root, text = "6", command= lambda : visor(6)).grid(row = 2, column = 2, sticky= W+E)
b7 = Button(root, text = "7", command= lambda : visor(7)).grid(row = 3, column = 0, sticky= W+E)
b8 = Button(root, text = "8", command= lambda : visor(8)).grid(row = 3, column = 1, sticky= W+E)
b9 = Button(root, text = "9", command= lambda : visor(9)).grid(row = 3, column = 2, sticky= W+E)
b0 = Button(root, text = "0", command= lambda : visor(0)).grid(row = 4, columnspan= 3,sticky= W+E)

#Botones operaciones
suma = Button(root, text = "+", command= lambda : visor("+")).grid(row = 1, column = 3,sticky = W+E)
resta = Button(root, text ="-", command= lambda : visor("-")).grid(row = 2,column = 3,sticky = W+E)
multi = Button(root, text = "x", command= lambda : visor("*")).grid(row = 3, column = 3,sticky = W+E)
division = Button(root, text= chr(247), command= lambda : visor("/")).grid(row = 3,column = 4,sticky = W+E)
resultado = Button(root, text = "=", command= ejecutar).grid(row = 4, column= 3, columnspan= 2, sticky= W+E)
DEL = Button(root, text = "DEL", command= lambda : visor("DEL")).grid(row = 1, column = 4, sticky= W+E)
CE = Button(root, text = "CE", command= lambda : visor ("CE")).grid(row = 2, column= 4,sticky= W+E)

estilo = 

root.mainloop()
