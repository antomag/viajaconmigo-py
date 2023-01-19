from tkinter import *
from PIL import Image, ImageTk
import re
import requests
import tkinter as tk
from tkinter import ttk

#VENTANA CONVERSOR
def ventanaConversor():
    class ConversorDivisas():
        def __init__(self,url):
            self.data = requests.get(url).json()
            self.monedas = self.data['rates']

        def convert(self, desde_moneda, a_moneda, monto):  
            if desde_moneda != 'USD' : 
                monto = monto / self.monedas[desde_moneda] 
            # limitar a 2 decimales
            monto = round(monto * self.monedas[a_moneda], 2) 
            return monto


    class App(tk.Tk):
        def __init__(self, converter):
            tk.Tk.__init__(self)
            self.title('CONVERSOR DE DIVISAS')
            self.currency_converter = converter
            self.resizable(False,False)
            self.iconbitmap("Images/monedas.ico")
            self.geometry("890x470+300+200")

            # Label imagen fondo
            self.fondo_conversor = Image.open("Images/cambio-de-moneda.png")
            self.fondo_conversor = self.fondo_conversor.resize((890,470))
            self.fondo_conversor = ImageTk.PhotoImage(self.fondo_conversor)
            self.intro_label = Label(self, image=self.fondo_conversor)
            self.intro_label.pack()

            # Campo monto Entry
            validar = (self.register(self.restringir_a_numeros), '%d', '%P')
            self.campo_monto = Entry(self,relief = tk.GROOVE, justify = tk.CENTER, fg = 'white', bg = 'black', font='bold',  validate='key',validatecommand=validar)
            self.campo_monto.place(x = 150, y = 200)

            # Campo monto Label
            self.campo_monto_label = Label(self, text = '', fg = 'white', bg = 'black', relief = tk.GROOVE, justify = tk.CENTER, width = 17, height=3, font='bold')
            self.campo_monto_label.place(x = 580, y = 190)

            # Desplegables
            self.desde_moneda_variable = StringVar(self)
            self.desde_moneda_variable.set("ARS") # default value
            self.a_moneda_variable = StringVar(self)
            self.a_moneda_variable.set("USD") # default value

            font = ("Arial", 12, "bold")
            self.option_add('*TCombobox*Listbox.font', font)

            # Combobox desde
            self.desde_moneda_dropdown = ttk.Combobox(self, textvariable=self.desde_moneda_variable,values=list(self.currency_converter.monedas.keys()), font = font, state = 'readonly', width = 13,justify = tk.CENTER)
            self.desde_moneda_dropdown.place(x = 190, y= 150)

            # Combobox a
            self.a_moneda_dropdown = ttk.Combobox(self, textvariable=self.a_moneda_variable,values=list(self.currency_converter.monedas.keys()), font = font, state = 'readonly', width = 13, justify = tk.CENTER)
            self.a_moneda_dropdown.place(x = 610, y= 150)

            # Boton convertir
            self.boton_convertir = Button(self, text = "CONVERTIR", bg='black' ,fg = "white", command = self.cambiar) 
            self.boton_convertir.config(font=('Courier', 15, 'bold'))
            self.boton_convertir.place(x = 380, y = 300)

            # Boton Volver
            self.boton_volver = Button(self, text = "VOLVER", bg='grey' ,fg = "white") 
            self.boton_volver.place(x = 420, y = 400)


        # Funcion convertir monto inicial a moneda final
        def cambiar(self):
            monto = float(self.campo_monto.get())
            from_curr = self.desde_moneda_variable.get()
            to_curr = self.a_moneda_variable.get()

            monto_convertido = self.currency_converter.convert(from_curr,to_curr,monto)
            monto_convertido = round(monto_convertido, 2)

            self.campo_monto_label.config(text = str(monto_convertido))
        
        # Restringe input ingreso monto a solo numeros
        def restringir_a_numeros(self, action ,string):
            regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
            resultado = regex.match(string)
            return (string == "" or (string.count('.') <= 1 and resultado is not None))

    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = ConversorDivisas(url)

    App(converter)
    mainloop()