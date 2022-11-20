
from tkinter import *
from math import *
 

def presionar(num):
    global operador
    operador = operador+str(num)
    pantalla.set(operador)
 

def resultado():
    global operador
    try:
        opera=str(eval(operador))
        pantalla.set(opera)
    except:
        pantalla.set("ERROR")
    operador = ""
 

def clear():
    global operador
    operador=("")
    pantalla.set("0")
 
 
ventana=Tk()
ventana.title("CALCULADORA")

ventana.configure(background="SkyBlue4")
color_boton=("gray77")
 
ancho_boton=11
alto_boton=3
pantalla=StringVar()
operador=""
 
Salida=Entry(ventana,font=('arial',20,'bold'),textvariable=pantalla,bd=20,insertwidth=4,bg="powder blue",justify="right")
Salida.grid(row =1 ,columnspan= 6,sticky=W+E)
 
#AÑADIR BOTONES.
#CREAMOS NUESTROS BOTONES
boton0 = Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(0))
boton1 = Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(1))
boton2 = Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(2))
boton3 = Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(3))
boton4 = Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(4))
boton5 = Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(5))
boton6 = Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(6))
boton7 = Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(7))
boton8 = Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(8))
boton9 =Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(9))
boton_pi =Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("pi"))
boton_coma = Button(ventana,text=",",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("."))
boton_suma = Button(ventana,text="+",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("+"))
boton_resta = Button(ventana,text="-",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("-"))
boton_multi = Button(ventana,text="*",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("*"))
boton_div = Button(ventana,text="/",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("/"))
boton_raiz = Button(ventana,text="√",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("sqrt("))
boton_parantesis1 = Button(ventana,text="(",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("("))
boton_parentesis2 = Button(ventana,text=")",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar(")"))
boton_porcentaje = Button(ventana,text="%",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("%"))
boton_ln = Button(ventana,text="ln",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("log("))
Boton_borrar_todo = Button(ventana,text="C",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear)
boton_exp = Button(ventana,text="EXP",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:presionar("**"))
boton_igual = Button(ventana,text="=",bg=color_boton,width=ancho_boton,height=alto_boton,command=resultado)


boton7.grid(row = 2, column = 0,sticky= W+E)
boton8.grid(row = 2, column = 1,sticky= W+E)
boton9.grid(row = 2, column = 2,sticky= W+E)
Boton_borrar_todo.grid(row = 2, column = 3, sticky = W+E)
boton_parantesis1.grid(row = 2, column = 4, sticky = W+E)
boton_parentesis2.grid(row = 2, column = 5, sticky = W+E)

boton4.grid(row = 3, column = 0, sticky = W+E)
boton5.grid(row = 3, column = 1, sticky = W+E)
boton6.grid(row = 3, column = 2, sticky = W+E)
boton_suma.grid(row = 3, column = 3, sticky = W+E)
boton_resta.grid(row = 3, column = 4, sticky = W+E)
boton_multi.grid(row = 3, column = 5, sticky = W+E)

boton3.grid(row = 4, column = 0, sticky = W+E)
boton2.grid(row = 4, column = 1, sticky = W+E)
boton1.grid(row = 4, column = 2, sticky = W+E)
boton_div.grid(row = 4, column = 3, sticky = W+E)
boton_pi.grid(row = 4, column = 4, sticky = W+E)
boton_raiz.grid(row = 4, column = 5, sticky = W+E)

boton0.grid(row = 5, columnspan= 2 ,sticky = W+E)
boton_coma.grid(row = 5, column = 2, sticky = W+E)
boton_porcentaje.grid(row = 5, column = 3, sticky = W+E)
boton_ln.grid(row = 5, column = 4, sticky = W+E)
boton_exp.grid(row = 5, column = 5, sticky = W+E)

boton_igual.grid(row = 6, columnspan= 6,sticky = W+E )

clear()
ventana.mainloop()