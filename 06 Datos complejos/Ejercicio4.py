'''4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.
Ejemplo:
contactos = {"Juan": "123456", "Ana": "987654"}
#Consultar : "Juan" -> muestra "123456"
'''

# Creamos un diccionario vacío para almacenar los contactos
agenda_telefonica = {}
# Bucle para permitir al usuario ingresar 5 contactos
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")  # Solicita el nombre
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ")  # Solicita el teléfono
    agenda_telefonica[nombre] = telefono  # Almacena el contacto en el diccionario
# Solicitamos un nombre para buscar su número
nombre_buscar = input("Ingrese un nombre para buscar su número: ")  # Solicita el nombre a buscar
# Verificamos si el nombre existe en el diccionario
if nombre_buscar in agenda_telefonica:
    print(f"El número de {nombre_buscar} es: {agenda_telefonica[nombre_buscar]}")  # Muestra el número
else:
    print(f"El contacto {nombre_buscar} no existe.")  # Indica que no se encontró el contacto