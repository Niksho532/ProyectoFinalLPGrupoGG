# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 17:33:47 2024

@author: Personal
"""

import tkinter as tk
from tkinter import filedialog
import csv

#Inicio Paradigma Imperativo *...
# Selección de archivo csv
def SelecArchivo():
    global archivo
    archivo = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if archivo:
        MostrarConten(archivo)


# Mostrar contenido del archivo
def MostrarConten(archivo):
    try:
        with open(archivo, newline='', encoding='utf-8') as archivoCSV:
            red = csv.reader(archivoCSV)
            contenidocsv = ""
            for row in red:
                contenidocsv += " ".join(row) + "\n"
            # Mostrar el contenido del CSV en la caja de texto izquierda
            cajatext1.delete(1.0, tk.END)
            cajatext1.insert(tk.END, contenidocsv)
    except Exception as e:
        cajatext1.delete(1.0, tk.END)
        cajatext1.insert(tk.END, f"Ocurrió un error al leer el archivo: {e}")

# Obtener texto del archivo
def ObtenerTexto(archivo):
    try:
        with open(archivo, newline='', encoding='utf-8') as archivoCSV:
            red = csv.reader(archivoCSV)
            contenidocsv = ""
            for row in red:
                contenidocsv += " ".join(row) + "\n"
            return contenidocsv
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"


# Mostrar texto cifrado en caja de texto derecha
def MostrarTextoCifrado(texto):
    cajatext2.delete(1.0, tk.END)
    cajatext2.insert(tk.END, texto)


# Escribir texto cifrado en un nuevo archivo CSV
def EscribirCSVConCifrado(NombreArchivo, TextoCifrado):
    try:
        with open(NombreArchivo, mode='w', newline='', encoding='utf-8') as ArchivoCSV:
            EscritorCSV = csv.writer(ArchivoCSV)
            for linea in TextoCifrado.split('\n'):
                EscritorCSV.writerow([linea])
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo CSV: {e}")
#Fin paradigma Imperativo ....*        


#Inicio paradigma Funcional *....
# Cifrado César
def CifradoCesar(texto, desplazamiento):
    def EncriptarCaracter(char):
        if char.isalpha():
            valor = 65 if char.isupper() else 97
            return chr((ord(char) - valor + desplazamiento) % 26 + valor)  # Se aplica la formula del cifrado cesar
        else:
            return char
    resultado = "".join(map(EncriptarCaracter, texto))
    return resultado

# Cifrado Affine
def CifradoAffine(texto, a, b):
    def EncriptarCaracter(char):
        if char.isalpha():
            valor = 65 if char.isupper() else 97
            return chr(((a * (ord(char) - valor) + b) % 26) + valor)  # Se aplica la formula del cifrado Affine
        else:
            return char

    resultado = "".join(map(EncriptarCaracter, texto))  # Con map se encripta cada caracter del texto y luego con join se junta en una sola cadena sin espacios
    return resultado

# Cifrado Mixto (Primero Affine y despues César)
def CifradoMixto(texto, a, b, desplazamiento):
    textoAffine = CifradoAffine(texto, a, b)
    return CifradoCesar(textoAffine, desplazamiento)


# Aplicar cifrado César
def Cesar():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoCesar(texto, 3)  # Usando un desplazamiento de 3
        MostrarTextoCifrado(TextoCifrado)
        EscribirCSVConCifrado('TextoCesar.csv', TextoCifrado)

# Aplicar cifrado Affine
def Affine():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoAffine(texto, 5, 8)  # Usando a=5 y b=8
        MostrarTextoCifrado(TextoCifrado)
        EscribirCSVConCifrado('TextoAffine.csv', TextoCifrado)

# Aplicar cifrado Mixto
def Mixto():
    if archivo:
        texto = ObtenerTexto(archivo)
        TextoCifrado = CifradoMixto(texto, 5, 8, 3)  # Usando a=5, b=8 y desplazamiento=3
        MostrarTextoCifrado(TextoCifrado)
        EscribirCSVConCifrado('TextoMixto.csv', TextoCifrado)
#Fin paradigma Funcional ....*

#Inicio Paradigma orientado a objetos *...
# Interfaz gráfica
ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Ventana Principal")

msg = tk.Label(ventana, text="Proyecto Lenguajes de Programacion 2024-1")
msg.pack()

lbl = tk.Label(ventana, text='Seleccione un archivo .csv')
lbl.place(x=178, y=40)

# Botón Seleccionar
botonSelec = tk.Button(ventana, text='Seleccionar', bg="orange", command=SelecArchivo)
botonSelec.place(x=210, y=60)

# Botón César
botonCesar = tk.Button(ventana, text='Cesar', command=Cesar)
botonCesar.place(x=120, y=110)

# Botón Affine
botAffine = tk.Button(ventana, text='Affine', command=Affine)
botAffine.place(x=225, y=110)

# Botón Mixto
botMixto = tk.Button(ventana, text='Mixto', command=Mixto)
botMixto.place(x=320, y=110)

# Caja de texto izquierda (3)
cajatext1 = tk.Text(ventana, width=24, wrap=tk.NONE, height=16, bg="white")
cajatext1.place(x=50, y=160)

scrolY1 = tk.Scrollbar(ventana, orient="vertical", command=cajatext1.yview)
scrolY1.pack(side="right", fill="y")
cajatext1.config(yscrollcommand=scrolY1.set)

scrolX1 = tk.Scrollbar(ventana, orient="horizontal", command=cajatext1.xview)
scrolX1.pack(side="bottom", fill="x")
cajatext1.config(xscrollcommand=scrolX1.set)

# Caja de texto derecha (2)
cajatext2 = tk.Text(ventana, width=24, wrap=tk.NONE, height=16, bg="white")
cajatext2.place(x=250, y=160)

scrolY2 = tk.Scrollbar(ventana, orient="vertical", command=cajatext2.yview)
scrolY2.pack(side="right", fill="y")
cajatext2.config(yscrollcommand=scrolY2.set)

scrolX2 = tk.Scrollbar(ventana, orient="horizontal", command=cajatext2.xview)
scrolX2.pack(side="bottom", fill="x")
cajatext2.config(xscrollcommand=scrolX2.set)

#Fin paradigma orienado a objetos ...*
ventana.mainloop()
