from tkinter import *
from PIL import Image, ImageTk
from conversor import ventanaConversor
from pronostico import ventanaPronostico

#HOME
root = Tk()
root.title("VIAJA CONMIGO")
root.geometry("900x500")
root.resizable(False,False)
root.iconbitmap("Images/avion.ico")

homeImg = Image.open("Images/home.jpg")
homeImg = homeImg.resize((1200, 600))
homeImg = ImageTk.PhotoImage(homeImg)
labelImgHome = Label(root,image=homeImg)
labelImgHome.pack()

def abrirClima():
    root.destroy()
    ventanaPronostico()

def abrirConversor():
    root.destroy()
    ventanaConversor()

#BOTON CLIMA
botonClima = Button(labelImgHome, text="SERVICIO METEOROLOGICO", command=abrirClima, bg='#40a19d')
botonClima.place(y=400,x=400)
botonClima.config(width='25', height='3')
#BOTON DIVISAS
botonDivisas = Button(labelImgHome, text="CONVERSOR DE DIVISAS", command=abrirConversor, bg='#f6c84b')
botonDivisas.place(y=400,x=600)
botonDivisas.config(width='20', height='3')

root.mainloop()
