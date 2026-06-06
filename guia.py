import os
import pickle

ARCHIVO_TEXTO = "inventario.txt"
ARCHIVO_BINARIO = "inventario.bin"

def guardar_binario():
    productos = []
    try:
        with open(ARCHIVO_TEXTO, "r") as archivo_txt:
            for linea in archivo_txt:
                id_p, nombre, precio, stock = linea.strip().split(",")
                productos.append((id_p, nombre, precio, stock))
        with open(ARCHIVO_BINARIO, "wb") as archivo_bin:
            pickle.dump(productos, archivo_bin)
        print(f"Inventario guardado en {ARCHIVO_BINARIO} (formato binario).")
    except FileNotFoundError:
        print("Primero debe crear productos en el archivo de texto.")

def leer_binario():
    try:
        with open(ARCHIVO_BINARIO, "rb") as archivo_bin:
            productos = pickle.load(archivo_bin)
        print("\n--- INVENTARIO DESDE ARCHIVO BINARIO ---")
        print(f"{'ID':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
        print("-" * 50)
        for id_p, nombre, precio, stock in productos:
            print(f"{id_p:<10} {nombre:<20} {precio:<10} {stock:<10}")
    except FileNotFoundError:
        print("El archivo binario no existe aún.")