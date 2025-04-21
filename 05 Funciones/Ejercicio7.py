'''Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado de
sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.'''

#Definicion de funciones
def funcion_suma(num1, num2):
    return print(f"El resultado de sumar {num1} + {num2} = {num1 + num2}")

def funcion_resta(num1, num2):
    return print(f"El resultado de restar {num1} - {num2} = {num1 - num2}")

def funcion_multiplicacion(num1, num2):
    return print(f"El resultado de multiplicar {num1} x {num2} = {num1 * num2}")

def funcion_dividir(num1,num2):
    return print(f"El resultado de dividir {num1} entre {num2} = {num1 / num2}")

def operaciones_basicas(num1, num2):
    funcion_suma(num1, num2)
    funcion_resta(num1, num2)
    funcion_multiplicacion(num1,num2)
    funcion_dividir(num1,num2)
    

#Programa principal
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
operaciones_basicas(numero1, numero2)