'''Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
'''

frase = str.lower(input("Ingrese una frase:"))
longitud_frase = len(frase) - 1
if frase[longitud_frase] == "a" or frase[longitud_frase] == "e" or frase[longitud_frase] == "i" or frase[longitud_frase] == "o" or frase[longitud_frase] == "u":
    print(f"{frase}!")
else:
    print(f"{frase}")