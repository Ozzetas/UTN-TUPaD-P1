'''Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.'''

numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))
sumatoria = 0

for i in range(numero1 + 1, numero2):
    sumatoria += i

print(sumatoria)