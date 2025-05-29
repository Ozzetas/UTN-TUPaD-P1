'''
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario
'''
#Definicion de funciones

def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

#Menu principal

num = int(input("Ingrese un numero: "))

for i in range(1, num + 1):
    print(f"El factorial del numero {i} es {factorial(i)}")