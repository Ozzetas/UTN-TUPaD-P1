'''Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y
mostrar el resultado usando esta función.'''

#Definicion de funciones
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return print(f"{segundos} segundos son {horas} horas")

#Programa principal
segundos = int(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)