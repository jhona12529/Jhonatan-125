import os
import pickle

ARCHIVO_TEXTO = "inventario.txt"
ARCHIVO_BINARIO = "inventario.bin"

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Agregar producto (modo añadir - texto)")
    print("5. Guardar inventario en archivo binario")
    print("6. Leer inventario desde archivo binario")
    print("7. Salir")

def agregar_producto(modo_append=False):
    id_producto = input("ID del producto: ")
    nombre = input("Nombre del producto: ")
    precio = input("Precio: ")
    stock = input("Stock: ")
    producto = f"{id_producto},{nombre},{precio},{stock}\n"

    if modo_append:
        with open(ARCHIVO_TEXTO, "a") as archivo:
            archivo.write(producto)
        print("Producto añadido (modo append).")
    else:
        with open(ARCHIVO_TEXTO, "w") as archivo:
            archivo.write(producto)
        print("Producto guardado (sobrescribe).")