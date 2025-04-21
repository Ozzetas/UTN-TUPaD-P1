'''Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro 
y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba 
el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario 
y llamar ambas funciones para mostrar los resultados
'''
#Modulos importados
import math

#Definicion de funciones
def calcular_area_circulo(radio):
    area_circulo = math.pi * (radio ** 2)
    return print(f"El area del circulo es: {area_circulo}")

def calcular_perimetro_circulo(radio):
    perimetro_circulo = 2 * math.pi * radio
    return print(f"El perimetro del circulo es de: {perimetro_circulo}")


#Programa principal
radio = int(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)