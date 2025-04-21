'''Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.'''

#Definicion de funciones
def celsius_a_fahrenheit(temperatura):
    return print(f"{temperatura} Cº es igual a {(temperatura * 9/5) + 32}º F ")

#Programa principal
temperatura_en_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(temperatura_en_celsius)