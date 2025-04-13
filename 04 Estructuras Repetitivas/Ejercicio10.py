'''Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.'''

numero = int(input("Ingresar un numero para invertir su orden: "))
numero_abs = abs(numero)
numero_invertido = 0

while numero_abs > 0:
    digito = numero_abs % 10
    numero_invertido = numero_invertido * 10 + digito
    numero_abs = numero_abs // 10

if numero < 0:
    numero_invertido = -numero_invertido

print(f"El numero con los digitos invertidos es: {numero_invertido}")