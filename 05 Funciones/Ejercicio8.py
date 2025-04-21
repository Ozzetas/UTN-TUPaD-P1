'''Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la 
función para mostrar el resultado con dos decimales.'''

#Definicion de funciones
def calcular_imc(peso, altura):
    return print(f"El IMC = {round(peso / altura**2, 2)}")

#Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
calcular_imc(peso, altura)