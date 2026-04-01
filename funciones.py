import json

ARCHIVO = "inventario.json"

# Cargar datos desde el archivo
def cargar_datos():
    try:
        with open(ARCHIVO, "r") as archivo:
            return json.load(archivo)
    except:
        return []

# Guardar datos en el archivo
def guardar_datos(inventario):
    with open(ARCHIVO, "w") as archivo:
        json.dump(inventario, archivo, indent=4)

# Agregar producto
def agregar_producto(inventario):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente")

# Mostrar productos
def mostrar_productos(inventario):
    if not inventario:
        print("No hay productos")
        return

    print("\n--- INVENTARIO ---")
    for producto in inventario:
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: {producto['precio']}")
        print(f"Cantidad: {producto['cantidad']}")
        print("-------------------")

# Buscar producto
def buscar_producto(inventario):
    nombre = input("Ingrese el nombre a buscar: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            print("Producto encontrado:")
            print(producto)
            return

    print("Producto no encontrado")

# Eliminar producto
def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre a eliminar: ")

    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            inventario.remove(producto)
            print("Producto eliminado")
            return

    print("Producto no encontrado")