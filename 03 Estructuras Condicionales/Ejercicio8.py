''' Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
'''

print("Menu:\n1 - Si quiere su nombre en mayusculas. Por ejemplo: PEDRO.\n2 - Si quiere su nombre en minusculas. Por ejemplo: pedro.\n3 - Si quiere su nombre con la primera letra mayuscula. Por ejemplo: Pedro.")
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opcion: "))

if opcion == 1:
    nombre = str.upper(nombre)
    print(f"Su nombre es: {nombre}")
elif opcion == 2:
    nombre = str.lower(nombre)
    print(f"Su nombre es: {nombre}")
elif opcion == 3:
    nombre = str.title(nombre)
    print(f"Su nombre es: {nombre}")
else:
    print("Ha ingresado una opcion incorrecta.")