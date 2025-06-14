'''9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Ejemplo:
Agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles"
}
'''
# Creamos un diccionario para la agenda con tuplas (día, hora) como claves
agenda = {}
while True:  # Bucle para mantener el programa corriendo
    print("\n1. Agregar evento\n2. Consultar evento\n3. Salir")
    opcion = input("Seleccione una opción: ")  # Solicita la opción
    if opcion == '1':  # Opción para agregar evento
        dia = input("Ingrese el día (ej. Lunes): ")  # Solicita el día
        hora = input("Ingrese la hora (ej. 14:30): ")  # Solicita la hora
        evento = input("Ingrese el evento: ")  # Solicita el evento
        agenda[dia,hora] = evento  # Agrega el evento con la tupla como clave
        print(f"Evento '{evento}' agregado para {dia,hora}).")  # Confirma la adición
    elif opcion == '2':  # Opción para consultar evento
        dia = input("Ingrese el día (ej. Lunes): ")  # Solicita el día
        hora = input("Ingrese la hora (ej. 14:30): ")  # Solicita la hora
        if (dia,hora) in agenda:  # Verifica si la tupla existe
            print(f"Evento para {dia,hora}: {agenda[dia,hora]}")  # Muestra el evento
        else:
            print(f"No hay evento programado para {dia,hora}).")  # Indica que no hay evento
    elif opcion == '3':  # Opción para salir
        print("Saliendo del programa.")  # Mensaje de salida
        break  # Sale del bucle del loop
    else:
        print("Opción inválida.")  # Mensaje para opción no válida