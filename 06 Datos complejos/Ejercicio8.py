'''8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.'''

# Creamos un diccionario para almacenar productos y su stock
stock_productos = {}
while True:  # Bucle para mantener el programa corriendo
    print("\n1. Consultar stock\n2. Agregar unidades\n3. Agregar nuevo producto\n4. Salir")
    opcion = input("Seleccione una opción: ")  # Solicita la opción
    if opcion == '1':  # Opción para consultar stock
        producto = input("Ingrese el nombre del producto: ")  # Solicita el nombre del producto
        if producto in stock_productos:  # Verifica si existe
            print(f"Stock de {producto}: {stock_productos[producto]}")  # Muestra el stock
        else:
            print(f"El producto {producto} no existe.")  # Indica que no existe
    elif opcion == '2':  # Opción para agregar unidades
        producto = input("Ingrese el nombre del producto: ")  # Solicita el nombre del producto
        if producto in stock_productos:  # Verifica si existe
            unidades = int(input("Ingrese la cantidad de unidades a agregar: "))  # Solicita unidades
            stock_productos[producto] += unidades  # Aumenta el stock
            print(f"Nuevo stock de {producto}: {stock_productos[producto]}")  # Muestra el nuevo stock
        else:
            print(f"El producto {producto} no existe.")  # Indica que no existe
    elif opcion == '3':  # Opción para agregar nuevo producto
        producto = input("Ingrese el nombre del nuevo producto: ")  # Solicita el nombre
        unidades = int(input("Ingrese el stock inicial: "))  # Solicita el stock inicial
        stock_productos[producto] = unidades  # Agrega el producto al diccionario
        print(f"Producto {producto} agregado con stock: {unidades}")  # Confirma la adición
    elif opcion == '4':  # Opción para salir
        print("Saliendo del programa.")  # Mensaje de salida
        break  # Sale del bucle
    else:
        print("Opción inválida.")  # Mensaje para opción no válida