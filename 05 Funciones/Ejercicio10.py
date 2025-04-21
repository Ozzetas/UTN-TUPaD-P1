'''Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.'''

#Definicion de funciones
def calcular_promedio(num1, num2, num3):
    sumatoria = num1 + num2 + num3
    return print(f"El promedio es = {sumatoria/3}")


#Programa principal
numero1 = float(input("Ingrese el numero 1: "))
numero2 = float(input("Ingrese el numero 2: "))
numero3 = float(input("Ingrese el numero 3: "))
calcular_promedio(numero1, numero2, numero3)