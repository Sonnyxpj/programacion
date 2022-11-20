from tkinter import *


def collatz(num):
    num = int(num)
    while num !=1:
        mod =  num % 2
        if mod == 0:
            num = num / 2
        else:
            num = num * 3 + 1 
        escribe(num)
    return num

def escribe(num):
    """label2 = Label(ventana, text= "Su resultado es:" )
    label2.pack()"""
    label_resultado = Label(ventana, text = str(num))
    label_resultado.pack()

if __name__ == "__main__":  
    ventana = Tk()
    ventana.geometry("+700+400")
    ventana.title("Conjetura de Collatz")
    label1=Label(ventana,text="Ingrese un número mayor que 1:")
    label1.pack()

    variable_string = StringVar()
    entrada = Entry(ventana,textvariable=variable_string)
    entrada.pack()

    boton1 = Button(text= "Empezar", command = lambda:collatz((entrada.get())))
 
    boton1.pack()


    ventana.mainloop()


