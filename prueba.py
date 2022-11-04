import tkinter as ttk

ventana = ttk.Tk("Tragamonedas")
etiqueta = ttk.Label(ventana, text="Tragamonedas")
etiqueta.pack()

cajatexto= ttk.Entry(ventana)
cajatexto.pack()

etiqueta2 = ttk.Label(ventana, text="")
etiqueta2.pack()

def textoDeLaCaja():
    text100 = cajatexto.get()
    etiqueta2["text"] = text100

boton1 = ttk.Button(ventana, text= "click",command= textoDeLaCaja)
boton1.pack()

ventana.geometry("400x400")
ventana.mainloop()