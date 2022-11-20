from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from math import *

def visor(num):
    global operador
    if num == "DEL":
        if operador == "=":
            pass
        else:
            operador = operador[:-1]
            entrada1.set(operador)
    elif num == "CE":
        operador = ""
        entrada1.set(0)
    else:
        operador = operador + str(num)
        entrada1.set(operador)


def ejecutar():
    global operador
    try:
        opera = str(eval(operador))
        entrada2.set(opera)
    except ZeroDivisionError:
        entrada2.set("MATH ERROR")
    except:
        entrada2.set("ERROR")
    operador = ""    


def info():
    messagebox.showinfo(message = "Precione (O) para activar el modo ocuro \nPrecione (L) para activar el modo claro")


def tema_oscuro(*args):
    estilos.configure("mainframe.TFrame", background = "#010924")

    estilos_label1.configure("Label1.TLabel", background = "#010924", foreground = "white")
    estilos_label2.configure("Label2.TLabel", background = "#010924", foreground = "white")

    estiloss_botones.configure("Botones_numeros.TButton", background = "#00044A", foregrounf = "white")
    estiloss_botones.map("Botones_numeros.TButton", background = [("active","#020A90")])
    estiloss_botones_borrar.configure("Botones_borrar.TButton", background = "#010924", foreground = "white")
    estiloss_botones_borrar.map("Botones_borrar.TButton", background = [("active", "#000AB1")])
    estiloss_botones_restantes.configure("Botones_restantes.TButton", background = "#010924", foreground = "white")
    estiloss_botones_restantes.map("Botones_restantes.TButton", background = [("active", "#000AB1")])

def tema_claro(*args):
    estilos.configure("mainframe.TFrame", background = "#DBDBDB", foreground = "black")
    
    estilos_label1.configure("Label1.TLabel", background = "#DBDBDB", foreground = "black")
    estilos_label2.configure("Label2.TLabel", background = "#DBDBDB", foreground = "black")

    estiloss_botones.configure("Botones_numeros.TButton", background = "#FFFFFF", foregrounf = "black")
    estiloss_botones.map("Botones_numeros.TButton", background = [("active","#B9B9B9")])
    estiloss_botones_borrar.configure("Botones_borrar.TButton", background = "#CECECE", foregrounf = "black")
    estiloss_botones_borrar.map("Botones_borrar.TButton", background = [("active", "#858585")])
    estiloss_botones_restantes.configure("Botones_restantes.TButton", background = "#CECECE", foregrounf = "black")
    estiloss_botones_restantes.map("Botones_restantes.TButton", background = [("active", "#858585")])


root = Tk()
root.title("Calculadora")
root.geometry("+500+80")
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

operador = ""

estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure("mainframe.TFrame", background = "#DBDBDB")


mainframe = ttk.Frame(root, style = "mainframe.TFrame")
mainframe.grid(column = 0, row = 0,sticky = (W, N ,E ,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.columnconfigure(1, weight = 1)
mainframe.columnconfigure(2, weight = 1)
mainframe.columnconfigure(3, weight = 1)

mainframe.rowconfigure(0, weight = 1)
mainframe.rowconfigure(1, weight = 1)
mainframe.rowconfigure(2, weight = 1)
mainframe.rowconfigure(3, weight = 1)
mainframe.rowconfigure(4, weight = 1)
mainframe.rowconfigure(5, weight = 1)
mainframe.rowconfigure(6, weight = 1)
mainframe.rowconfigure(7, weight = 1)

#Estiloss
estilos_label1 = ttk.Style()
estilos_label1.configure("Label1.TLabel", font = "arial 20 bold", anchor = "e",)

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable = entrada1, style = "Label1.TLabel")
label_entrada1.grid(row = 0 , column = 0,columnspan = 4, sticky = (W, N, E, S))

estilos_label2 = ttk.Style()
estilos_label2.configure("Label2.TLabel", font = "arial 40 bold", anchor = "e")

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable = entrada2, style = "Label2.TLabel")
label_entrada2.grid(row = 1, column = 0,columnspan = 4, sticky = (W, N, E, S))

#Estiloss para los botones

estiloss_botones = ttk.Style()
estiloss_botones.configure("Botones_numeros.TButton", font = "arial 22", width = 5, background = "#FFFFFF", relief = "flat")
estiloss_botones.map("Botones_numeros.TButton", background = [("active","#B9B9B9")]) 

estiloss_botones_borrar = ttk.Style()
estiloss_botones_borrar.configure("Botones_borrar.TButton", font = "arial 22", width = 5, relief = "flat")
estiloss_botones_borrar.map("Botones_borrar.TButton", foreground = [("active", "#FF0000")])

estiloss_botones_restantes = ttk.Style()
estiloss_botones_restantes.configure("Botones_restantes.TButton", font = "arial 22", width = 5, relief = "flat")
estiloss_botones_restantes.map("Botones_restantes.TButton", background = [("active", "#858585")])

boton0 = ttk.Button(mainframe,text = "0",style = "Botones_numeros.TButton", command= lambda : visor(0))
boton1 = ttk.Button(mainframe,text = "1",style = "Botones_numeros.TButton", command= lambda : visor(1))
boton2 = ttk.Button(mainframe,text = "2",style = "Botones_numeros.TButton", command= lambda : visor(2))
boton3 = ttk.Button(mainframe,text = "3",style = "Botones_numeros.TButton", command= lambda : visor(3))
boton4 = ttk.Button(mainframe,text = "4",style = "Botones_numeros.TButton", command= lambda : visor(4))
boton5 = ttk.Button(mainframe,text = "5",style = "Botones_numeros.TButton", command= lambda : visor(5))
boton6 = ttk.Button(mainframe,text = "6",style = "Botones_numeros.TButton", command= lambda : visor(6))
boton7 = ttk.Button(mainframe,text = "7",style = "Botones_numeros.TButton", command= lambda : visor(7))
boton8 = ttk.Button(mainframe,text = "8",style = "Botones_numeros.TButton", command= lambda : visor(8))
boton9 = ttk.Button(mainframe,text = "9",style = "Botones_numeros.TButton", command= lambda : visor(9))

boton_borrar = ttk.Button(mainframe, text = chr(9003), style = "Botones_borrar.TButton",command= lambda : visor("DEL")) #chr(9003) simbolo de borrar uno por uno 
boton_borrar_todo = ttk.Button(mainframe, text = "CE", style = "Botones_borrar.TButton", command= lambda : visor("CE"))
boton_parantesi1 = ttk.Button(mainframe, text = "(", style = "Botones_restantes.TButton", command= lambda : visor("("))
boton_parantesi2 = ttk.Button(mainframe, text = ")", style = "Botones_restantes.TButton", command= lambda : visor(")"))
boton_punto = ttk.Button(mainframe, text = ".", style = "Botones_restantes.TButton", command= lambda : visor("."))

#operaciones 
boton_suma = ttk.Button(mainframe, text = "+", style = "Botones_restantes.TButton", command= lambda : visor("+"))
boton_resta = ttk.Button(mainframe,text = "-", style = "Botones_restantes.TButton", command= lambda : visor("-"))
boton_multi = ttk.Button(mainframe, text = "x", style = "Botones_restantes.TButton", command= lambda : visor("*"))
boton_div = ttk.Button(mainframe, text = chr(247), style = "Botones_restantes.TButton", command= lambda : visor("/")) #simbolo de división 

boton_igual = ttk.Button(mainframe, text = "=", style = "Botones_restantes.TButton",command= ejecutar)
boton_raiz_cuadrada = ttk.Button(mainframe, text ="√", style = "Botones_restantes.TButton",command= lambda : visor(sqrt))

boton_parantesi1.grid(row = 2, column = 0, sticky = (W, N, E, S))
boton_parantesi2.grid(row = 2, column = 1, sticky = (W, N, E, S))
boton_borrar_todo.grid(row = 2, column = 2, sticky = (W, N, E, S))
boton_borrar.grid(row = 2, column = 3, sticky = (W, N, E, S)) 

boton7.grid(row = 3, column = 0, sticky = (W, N, E, S))
boton8.grid(row = 3, column = 1, sticky = (W, N, E, S))
boton9.grid(row = 3, column = 2, sticky = (W, N, E, S))
boton_div.grid(row = 3, column = 3, sticky = (W, N, E, S))

boton4.grid(row = 4, column = 0, sticky = (W, N, E, S))
boton5.grid(row = 4, column = 1, sticky = (W, N, E, S))
boton6.grid(row = 4, column = 2, sticky = (W, N, E, S))
boton_multi.grid(row = 4, column = 3, sticky = (W, N, E, S))

boton1.grid(row = 5, column = 0, sticky = (W, N, E, S))
boton2.grid(row = 5, column = 1, sticky = (W, N, E, S))
boton3.grid(row = 5, column = 2, sticky = (W, N, E, S))
boton_suma.grid(row = 5, column = 3, sticky = (W, N, E, S))

boton0.grid(row = 6, column = 0, columnspan = 2, sticky = (W, N, E, S))
boton_punto.grid(row = 6, column = 2, sticky = (W, N, E, S))
boton_resta.grid(row = 6, column = 3, sticky = (W, N, E, S))

boton_igual.grid(row = 7, column = 0, columnspan = 2, sticky = (W, N, E, S))
boton_raiz_cuadrada.grid(row = 7, column = 2, sticky = (W, N, E, S))

info = ttk.Button(mainframe, text= "Info",style="Botones_restantes.TButton", command= info).grid(row = 7, column = 3)



for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind("<KeyPress-o>", tema_oscuro)
root.bind("<KeyPress-l>", tema_claro)
root.mainloop()