from funciones import *

# Menú principal
def menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def main():
    # Cargar datos desde archivo
    inventario = cargar_datos()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(inventario)

        elif opcion == "2":
            mostrar_productos(inventario)

        elif opcion == "3":
            buscar_producto(inventario)

        elif opcion == "4":
            eliminar_producto(inventario)

        elif opcion == "5":
            guardar_datos(inventario)
            print("Datos guardados. Saliendo...")
            break

        else:
            print("Opción inválida")

# Ejecutar programa
if __name__ == "__main__":
    main()