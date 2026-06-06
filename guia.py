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

def mostrar_productos():
    try:
        with open(ARCHIVO_TEXTO, "r") as archivo:
            print("\n--- LISTA DE PRODUCTOS ---")
            print(f"{'ID':<10} {'Nombre':<20} {'Precio':<10} {'Stock':<10}")
            print("-" * 50)
            for linea in archivo:
                id_p, nombre, precio, stock = linea.strip().split(",")
                print(f"{id_p:<10} {nombre:<20} {precio:<10} {stock:<10}")
    except FileNotFoundError:
        print("El archivo de inventario no existe aún.")

def buscar_producto():
    busqueda = input("Ingrese ID o nombre a buscar: ").lower()
    encontrado = False
    try:
        with open(ARCHIVO_TEXTO, "r") as archivo:
            for linea in archivo:
                id_p, nombre, precio, stock = linea.strip().split(",")
                if busqueda == id_p.lower() or busqueda in nombre.lower():
                    print(f"ID: {id_p}, Nombre: {nombre}, Precio: {precio}, Stock: {stock}")
                    encontrado = True
        if not encontrado:
            print("Producto no encontrado.")
    except FileNotFoundError:
        print("Archivo no existe.")

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

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_producto(modo_append=False)
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            agregar_producto(modo_append=True)
        elif opcion == "5":
            guardar_binario()
        elif opcion == "6":
            leer_binario()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida.")

if _name_ == "_main_":
    main()
