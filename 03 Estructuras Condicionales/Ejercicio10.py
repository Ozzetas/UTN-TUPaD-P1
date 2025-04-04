'''Utilizando la información aportada en la siguiente tabla sobre las estaciones del año:
[Cuadro que esta en el pdf del trabajo praactico]
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
'''

hemisferio = str.lower(input("En que hemisferio se encuentra? Norte o Sur?\nN/S:"))
mes = input("En que mes se encuentra?: ")
dia = int(input("Que dia es?: "))

if hemisferio == "n":
    if ((dia >= 21 and dia <= 31) and mes == "diciembre") or ((dia >= 1 and dia <= 20) and mes == "marzo"):
        print("Estas en INVIERNO.")
    elif ((dia >= 21 and dia <= 31) and mes == "marzo") or ((dia >= 1 and dia <= 20) and mes == "junio"):
        print("Estas en PRIMAVERA.")
    elif ((dia >= 21 and dia <= 31) and mes == "junio") or ((dia >= 1 and dia <= 20) and mes == "septiembre"):
        print("Estas en VERANO.")
    elif ((dia >= 21 and dia <= 31) and mes == "septiembre") or ((dia >= 1 and dia <= 20) and mes == "diciembre"):
        print("Estas en OTOÑO.")
elif hemisferio == "s":
    if ((dia >= 21 and dia <= 31) and mes == "diciembre") or ((dia >= 1 and dia <= 20) and mes == "marzo"):
        print("Estas en VERANO.")
    elif ((dia >= 21 and dia <= 31) and mes == "marzo") or ((dia >= 1 and dia <= 20) and mes == "junio"):
        print("Estas en OTOÑO.")
    elif ((dia >= 21 and dia <= 31) and mes == "junio") or ((dia >= 1 and dia <= 20) and mes == "septiembre"):
        print("Estas en INVIERNO.")
    elif ((dia >= 21 and dia <= 31) and mes == "septiembre") or ((dia >= 1 and dia <= 20) and mes == "diciembre"):
        print("Estas en PRIMAVERA.")
