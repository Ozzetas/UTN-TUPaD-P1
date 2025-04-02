'''Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
temperatura en Farenheit = (9/5) * temperatura en celsius + 32'''

tempEnCelsius = float(input("Ingrese la temperatura en Celsius: "))
tempEnFarenheit = (9/5 * tempEnCelsius) + 32
print(f"Temperatura en Celsius = {tempEnCelsius} y Temperatura en Farenheit = {tempEnFarenheit}")