'''Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.'''

radio = int(input("Ingrese el radio del circulo: "))
pi = 3.14
area = pi * (radio ** 2)
print(f"El area del circulo es: {area}")